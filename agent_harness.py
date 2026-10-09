"""agent_harness.py — Fixed agent loop with swappable context providers.

One variable across all runs: the context provider.
Everything else — model, system prompt, tool budget, max iterations,
patch acceptance rule — is identical.

Retrieval conditions:
  naive      — repo file tree only (no retrieval)
  bm25       — BM25-ranked function bodies
  minilm     — Dense-MiniLM cosine-ranked bodies
  hybrid     — BM25 + MiniLM RRF
  tacm       — TACM-v2 layered selection (budget=4000)
  tacm-dyn   — TACM-v2 with dynamic cross-layer budget allocation
  tacm-l4    — TACM-v2 + Layer 04 (variable dynamic layer)
  tacm-dyn-l4 — TACM-v2 dynamic selector + Layer 04

Usage:
    python3 agent_harness.py --project thefuck --repo ./thefuck --condition tacm
    python3 agent_harness.py --all --seeds 3 --budget 4000
    python3 agent_harness.py --project thefuck --repo ./thefuck --condition tacm --bug-id thefuck-7
"""

from __future__ import annotations

import argparse
import json
import os
import random
import sys
import time
from dataclasses import dataclass, field, asdict
from pathlib import Path

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "archive" / "pre-research"))

BUGSINPY_ROOT = ROOT / "BugsInPy"
RESULTS_DIR   = ROOT / os.environ.get("RESULTS_DIR", "agent_results")

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
GITHUB_TOKEN      = os.environ.get("GITHUB_TOKEN", "")
MODEL = os.environ.get("AGENT_MODEL", "gpt-4o-mini")

# Load .env from project root if present
_env_file = ROOT / ".env"
if _env_file.exists():
    for _line in _env_file.read_text().splitlines():
        _line = _line.strip()
        if _line and not _line.startswith("#") and "=" in _line:
            _k, _v = _line.split("=", 1)
            if _k.strip() not in os.environ:
                os.environ[_k.strip()] = _v.strip()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
MAX_ITER = 5
DEFAULT_BUDGET = 4000

# GitHub Models API (OpenAI-compatible, separate rate limits from Copilot chat)
# Falls back to Copilot chat API if GITHUB_MODELS=0
USE_GITHUB_MODELS = os.environ.get("GITHUB_MODELS", "1") != "0"
COPILOT_API_BASE  = "https://models.inference.ai.azure.com" if USE_GITHUB_MODELS else "https://api.githubcopilot.com"
COPILOT_HEADERS   = {} if USE_GITHUB_MODELS else {"Copilot-Integration-Id": "vscode-chat"}


# ---------------------------------------------------------------------------
# System and task prompts (fixed across all conditions)
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """You are a code debugging assistant embedded in a coding agent.

You will be given:
1. A bug description (from a git commit message)
2. Repository context (retrieved code — the amount and style varies by session)
3. The name of a failing test

Your job: produce a correct unified diff patch that fixes the bug and passes the test.

Rules:
- Work within the provided context first. Read additional files only if you are certain
  the fix requires code not shown.
- When confident about the fix, call write_patch with a valid unified diff.
- If you read a file, use search_symbol to confirm which function to edit.
- Do not guess. If you are unsure what to change, read the relevant file first.
- Produce exactly one patch per write_patch call. If tests fail, analyse the output
  and try again with a corrected patch.
"""


def task_prompt(bug_description: str, context: str, test_file: str, failing_output: str = "") -> str:
    parts = [
        f"## Bug description\n{bug_description}",
        f"## Failing test\n{test_file}",
    ]
    if failing_output:
        parts.append(f"## Previous test output\n```\n{failing_output[:2000]}\n```")
    parts.append(f"## Repository context\n```python\n{context}\n```")
    parts.append(
        "Diagnose the bug and produce a unified diff patch using write_patch. "
        "If you need to read a specific file first, call read_file."
    )
    return "\n\n".join(parts)


# ---------------------------------------------------------------------------
# Agent tools
# ---------------------------------------------------------------------------

TOOLS = [
    {
        "name": "read_file",
        "description": "Read a file from the repository. Use this to inspect code not in the provided context.",
        "input_schema": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Relative file path from repo root"},
                "start_line": {"type": "integer", "description": "First line to read (1-based, optional)"},
                "end_line":   {"type": "integer", "description": "Last line to read (optional)"},
            },
            "required": ["path"],
        },
    },
    {
        "name": "search_symbol",
        "description": "Search for a function or class definition in the repository.",
        "input_schema": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Function or class name to find"},
            },
            "required": ["name"],
        },
    },
    {
        "name": "write_patch",
        "description": "Write a unified diff patch to fix the bug. This ends the current attempt.",
        "input_schema": {
            "type": "object",
            "properties": {
                "patch": {"type": "string", "description": "Unified diff patch string"},
                "explanation": {"type": "string", "description": "Brief explanation of what was changed and why"},
            },
            "required": ["patch"],
        },
    },
]


def execute_tool(tool_name: str, tool_input: dict, repo_root: Path) -> str:
    """Execute a tool call from the agent and return the result string."""
    if tool_name == "read_file":
        path = repo_root / tool_input["path"]
        if not path.exists():
            return f"File not found: {tool_input['path']}"
        try:
            lines = path.read_text(errors="replace").splitlines()
            start = max(0, tool_input.get("start_line", 1) - 1)
            end   = tool_input.get("end_line", len(lines))
            selected = lines[start:end]
            return "\n".join(f"{start+i+1}: {l}" for i, l in enumerate(selected))
        except Exception as e:
            return f"Error reading file: {e}"

    elif tool_name == "search_symbol":
        name = tool_input["name"]
        import subprocess
        r = subprocess.run(
            ["grep", "-rn", f"def {name}", "--include=*.py"],
            cwd=repo_root, capture_output=True, text=True, timeout=10,
        )
        results = r.stdout.strip()
        if not results:
            results = f"No definition found for: {name}"
        return results[:3000]

    elif tool_name == "write_patch":
        # Handled by the caller — return the patch text for processing
        return "__PATCH__:" + tool_input.get("patch", "")

    return f"Unknown tool: {tool_name}"


# ---------------------------------------------------------------------------
# Single run result
# ---------------------------------------------------------------------------

@dataclass
class RunResult:
    bug_id: str
    condition: str
    seed: int
    success: bool
    steps: int
    prompt_tokens: int
    completion_tokens: int
    duration_s: float
    patch_applied: bool
    test_output: str
    error: str = ""


# ---------------------------------------------------------------------------
# API backends: Anthropic SDK  +  Copilot OpenAI-compatible
# ---------------------------------------------------------------------------

def _get_gh_token() -> str:
    """Get GitHub token via gh CLI."""
    import subprocess
    try:
        r = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=5)
        return r.stdout.strip()
    except Exception:
        return ""


CLAUDE_BIN = os.environ.get(
    "CLAUDE_BIN",
    "/Users/xxvirusxx/.vscode/extensions/anthropic.claude-code-2.1.96-darwin-arm64/resources/native-binary/claude"
)

OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "qwen2.5-coder:7b")
OLLAMA_BASE   = os.environ.get("OLLAMA_BASE",  "http://localhost:11434")
USE_OLLAMA    = os.environ.get("USE_OLLAMA", "0") == "1"


def _claude_code_call(user_content: str, force_patch: bool = False) -> dict:  # noqa: F811
    import subprocess
    """Use the Claude Code CLI binary (--print) as an API backend.

    No API key required — uses the same OAuth session as Claude Code itself.
    Forces write_patch by appending an instruction when force_patch=True.
    Since we can't do tool_choice=required via CLI, we extract the patch from
    the text output using a structured prompt.
    """
    import re as _re

    # Build a self-contained prompt that instructs the model to output a patch
    tool_desc = "\n".join(
        f"- {t['name']}: {t['description']}" for t in TOOLS
    )
    prompt = f"{SYSTEM_PROMPT}\n\nAvailable actions:\n{tool_desc}\n\n{user_content}\n\n"
    if force_patch:
        prompt += (
            "\nYou MUST now output the patch. "
            "Wrap it in a ```diff ... ``` block. Do not ask for more information."
        )
    else:
        prompt += (
            "\nIf you have enough information, output a unified diff patch in a ```diff ... ``` block. "
            "If you need to read a file first, say READ: <filepath>. "
            "If you need to search for a symbol, say SEARCH: <name>."
        )

    try:
        r = subprocess.run(
            [CLAUDE_BIN, "--print", "--model", "claude-sonnet-4-6"],
            input=prompt, capture_output=True, text=True, timeout=300,
        )
        text = r.stdout.strip()
    except subprocess.TimeoutExpired:
        raise RuntimeError("Claude Code CLI timed out")
    except Exception as e:
        raise RuntimeError(f"Claude Code CLI failed: {e}")

    # Detect rate-limit echo mode: CLI echoes the input verbatim when rate-limited
    # (the output is identical to the prompt, or starts with the system prompt text)
    if text and (text == prompt.strip() or text.startswith(SYSTEM_PROMPT[:80].strip())):
        raise RuntimeError("Claude Code CLI rate-limited (output echoed input)")

    # Detect empty or near-empty output (another rate-limit symptom)
    if not text or len(text) < 20:
        raise RuntimeError(f"Claude Code CLI returned empty output (exit={r.returncode})")

    # Extract patch from ```diff block
    patch_text = None
    m = _re.search(r"```diff\s*\n(.*?)```", text, _re.DOTALL)
    if m:
        patch_text = m.group(1)

    # Detect READ/SEARCH directives as stop_reason signals
    stop_reason = "end_turn"
    if patch_text is None and (_re.search(r"^(READ|SEARCH):", text, _re.MULTILINE)):
        stop_reason = "tool_use"   # agent wants more info, will be looped

    # Rough token count (4 chars ≈ 1 token)
    prompt_tokens = len(prompt) // 4
    completion_tokens = len(text) // 4

    return {
        "patch_text": patch_text,
        "raw_text": text,
        "stop_reason": stop_reason,
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
    }


def _ollama_call(user_content: str, force_patch: bool = False) -> dict:
    """Call a local Ollama model via its OpenAI-compatible /v1/chat/completions API.

    Uses the same text-in/text-out structured prompt as _claude_code_call since
    Ollama tool-use support is inconsistent across models. The model is prompted
    to emit a ```diff block when ready to patch.
    """
    import urllib.request as _ur
    import json as _json
    import re as _re

    tool_desc = "\n".join(f"- {t['name']}: {t['description']}" for t in TOOLS)
    prompt = (
        f"{SYSTEM_PROMPT}\n\nAvailable actions:\n{tool_desc}\n\n{user_content}\n\n"
    )
    if force_patch:
        prompt += (
            "\nYou MUST now output the patch. "
            "Wrap it in a ```diff ... ``` block. Do not ask for more information."
        )
    else:
        prompt += (
            "\nIf you have enough information, output a unified diff patch in a ```diff ... ``` block. "
            "If you need to read a file first, say READ: <filepath>. "
            "If you need to search for a symbol, say SEARCH: <name>."
        )

    payload = _json.dumps({
        "model": OLLAMA_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "options": {"temperature": 0.2, "num_ctx": 8192},
    }).encode()

    req = _ur.Request(
        f"{OLLAMA_BASE}/v1/chat/completions",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with _ur.urlopen(req, timeout=300) as resp:
            data = _json.loads(resp.read())
    except Exception as e:
        raise RuntimeError(f"Ollama call failed: {e}")

    text = (data.get("choices", [{}])[0].get("message", {}).get("content") or "").strip()
    usage = data.get("usage", {})

    patch_text = None
    m = _re.search(r"```diff\s*\n(.*?)```", text, _re.DOTALL)
    if m:
        patch_text = m.group(1)

    stop_reason = "end_turn"
    if patch_text is None and _re.search(r"^(READ|SEARCH):", text, _re.MULTILINE):
        stop_reason = "tool_use"

    return {
        "patch_text": patch_text,
        "raw_text": text,
        "stop_reason": stop_reason,
        "prompt_tokens":     usage.get("prompt_tokens", len(prompt) // 4),
        "completion_tokens": usage.get("completion_tokens", len(text) // 4),
    }


def _openai_call(user_content: str, force_patch: bool = False) -> dict:
    """Call OpenAI API with proper function/tool calling (multi-turn capable)."""
    import openai as _openai
    import json as _json

    client = _openai.OpenAI(api_key=OPENAI_API_KEY)
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user",   "content": user_content},
    ]
    tool_choice = (
        {"type": "function", "function": {"name": "write_patch"}} if force_patch else "auto"
    )
    resp = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=_tools_openai(),
        tool_choice=tool_choice,
        max_tokens=4096,
        timeout=120,
    )
    choice = resp.choices[0]
    msg = choice.message
    raw_text = msg.content or ""
    patch_text = None

    for tc in msg.tool_calls or []:
        if tc.function.name == "write_patch":
            try:
                args = _json.loads(tc.function.arguments)
                patch_text = args.get("patch", "")
            except Exception:
                patch_text = tc.function.arguments

    stop_reason = "end_turn" if choice.finish_reason in ("stop", "end_turn") else choice.finish_reason
    usage = resp.usage
    return {
        "patch_text": patch_text,
        "raw_text": raw_text,
        "stop_reason": stop_reason,
        "prompt_tokens":     usage.prompt_tokens if usage else 0,
        "completion_tokens": usage.completion_tokens if usage else 0,
    }


# Convert TOOLS (Anthropic format) → OpenAI function-calling format
def _tools_openai() -> list:
    result = []
    for t in TOOLS:
        result.append({
            "type": "function",
            "function": {
                "name": t["name"],
                "description": t["description"],
                "parameters": t["input_schema"],
            },
        })
    return result


def _anthropic_call(user_content: str) -> dict:
    import anthropic
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    response = client.messages.create(
        model=MODEL,
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        tools=TOOLS,
        messages=[{"role": "user", "content": user_content}],
    )
    patch_text = None
    raw_text = ""
    for block in response.content:
        if block.type == "tool_use" and block.name == "write_patch":
            patch_text = block.input.get("patch", "")
        elif block.type == "tool_use":
            # other tools — execute and ignore result for now (single-turn simplified)
            pass
        elif hasattr(block, "text"):
            raw_text += block.text
    return {
        "patch_text": patch_text,
        "raw_text": raw_text,
        "stop_reason": response.stop_reason,
        "prompt_tokens": response.usage.input_tokens,
        "completion_tokens": response.usage.output_tokens,
    }


def _copilot_call(user_content: str, token: str, force_patch: bool = False) -> dict:
    """Call Copilot API (OpenAI-compatible) with tool use, with retry on rate limit."""
    import requests as _requests
    import json as _json

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user",   "content": user_content},
    ]
    payload = {
        "model": MODEL,
        "messages": messages,
        "tools": _tools_openai(),
        "tool_choice": {"type": "function", "function": {"name": "write_patch"}} if force_patch else "auto",
        "max_tokens": 4096,
    }
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    headers.update(COPILOT_HEADERS)

    # Retry up to 5 times with backoff for rate limits
    for attempt in range(5):
        try:
            resp = _requests.post(
                f"{COPILOT_API_BASE}/chat/completions",
                json=payload, headers=headers, timeout=120,
            )
        except Exception as e:
            raise RuntimeError(f"Copilot request failed: {e}")

        if resp.status_code in (429, 403) or "rate limit" in resp.text.lower() or "exhausted" in resp.text.lower() or "forbidden" in resp.text.lower():
            wait = 20 * (attempt + 1)
            print(f"\n  [rate limit {resp.status_code}, waiting {wait}s]", end="", flush=True)
            time.sleep(wait)
            continue
        if resp.status_code != 200:
            raise RuntimeError(f"Copilot API {resp.status_code}: {resp.text[:200]}")

        data = resp.json()
        break
    else:
        raise RuntimeError("Copilot API rate limit exceeded after retries")

    choice = data["choices"][0]
    msg = choice["message"]
    stop_reason = "end_turn" if choice["finish_reason"] in ("stop", "end_turn") else choice["finish_reason"]

    patch_text = None
    raw_text = msg.get("content") or ""

    # Handle tool calls
    for tc in msg.get("tool_calls") or []:
        fn = tc.get("function", {})
        if fn.get("name") == "write_patch":
            try:
                args = _json.loads(fn.get("arguments", "{}"))
                patch_text = args.get("patch", "")
            except Exception:
                patch_text = fn.get("arguments", "")
        # For read_file / search_symbol we'd need multi-turn; skip for now
        # (agent will fall back to write_patch directly from context)

    usage = data.get("usage", {})
    return {
        "patch_text": patch_text,
        "raw_text": raw_text,
        "stop_reason": stop_reason,
        "prompt_tokens": usage.get("prompt_tokens", 0),
        "completion_tokens": usage.get("completion_tokens", 0),
    }


# ---------------------------------------------------------------------------
# One agent attempt
# ---------------------------------------------------------------------------

def run_agent(
    bug_id: str,
    condition: str,
    seed: int,
    query: str,
    context: str,
    test_file: str,
    repo_root: Path,
) -> RunResult:
    """Run the fixed agent loop for one (bug, condition, seed) triple."""
    from patch_utils import apply_patch, restore_repo, extract_patch_from_text
    from test_runner import run_tests, format_test_feedback

    # Backend priority: Ollama > OpenAI API > Anthropic SDK > Claude Code CLI > Copilot
    use_ollama = USE_OLLAMA
    use_openai = not use_ollama and bool(OPENAI_API_KEY)
    use_claude_code = not use_ollama and not use_openai and os.path.exists(CLAUDE_BIN) and not ANTHROPIC_API_KEY
    use_copilot = not use_ollama and not use_openai and not ANTHROPIC_API_KEY and not use_claude_code
    if use_copilot:
        token = GITHUB_TOKEN or _get_gh_token()
        if not token:
            return RunResult(bug_id=bug_id, condition=condition, seed=seed,
                             success=False, steps=0, prompt_tokens=0, completion_tokens=0,
                             duration_s=0.0, patch_applied=False, test_output="",
                             error="No ANTHROPIC_API_KEY, Claude Code binary, or GITHUB_TOKEN available")

    random.seed(seed)
    start = time.monotonic()
    total_prompt = 0
    total_completion = 0
    last_test_output = ""
    patch_applied = False
    success = False

    for step in range(MAX_ITER):
        if step == 0:
            user_content = task_prompt(query, context, test_file)
        else:
            user_content = task_prompt(query, context, test_file,
                                       failing_output=last_test_output)

        # On the final step, force write_patch so the agent doesn't exhaust budget on reads
        force_patch = (step == MAX_ITER - 1)

        try:
            if use_ollama:
                resp = _ollama_call(user_content, force_patch=force_patch)
            elif use_openai:
                resp = _openai_call(user_content, force_patch=force_patch)
            elif use_claude_code:
                resp = _claude_code_call(user_content, force_patch=force_patch)
            elif use_copilot:
                resp = _copilot_call(user_content, token, force_patch=force_patch)
            else:
                resp = _anthropic_call(user_content)
        except Exception as e:
            return RunResult(bug_id=bug_id, condition=condition, seed=seed,
                             success=False, steps=step+1,
                             prompt_tokens=total_prompt, completion_tokens=total_completion,
                             duration_s=time.monotonic()-start,
                             patch_applied=patch_applied, test_output=last_test_output,
                             error=str(e))

        total_prompt     += resp["prompt_tokens"]
        total_completion += resp["completion_tokens"]
        patch_text        = resp["patch_text"]
        stop_reason       = resp["stop_reason"]

        if patch_text is not None:
            if not patch_text.strip():
                patch_text = extract_patch_from_text(resp.get("raw_text", "")) or patch_text

            ok, err = apply_patch(repo_root, patch_text)
            patch_applied = ok

            if not ok:
                last_test_output = f"Patch failed to apply: {err}"
            else:
                test_result = run_tests(repo_root, test_file)
                last_test_output = format_test_feedback(test_result)
                if test_result.passed:
                    success = True
                    restore_repo(repo_root)
                    break

            restore_repo(repo_root)

        elif stop_reason == "end_turn":
            break
        elif (use_claude_code or use_ollama) and stop_reason == "tool_use":
            # Agent requested READ or SEARCH — execute and append to context for next step
            import re as _re
            raw = resp.get("raw_text", "")
            tool_outputs = []
            for m in _re.finditer(r"^(READ|SEARCH):\s*(.+)$", raw, _re.MULTILINE):
                action, arg = m.group(1), m.group(2).strip()
                if action == "READ":
                    tool_outputs.append(execute_tool("read_file", {"path": arg}, repo_root))
                elif action == "SEARCH":
                    tool_outputs.append(execute_tool("search_symbol", {"name": arg}, repo_root))
            if tool_outputs:
                last_test_output = "\n\n".join(tool_outputs)

    return RunResult(
        bug_id=bug_id,
        condition=condition,
        seed=seed,
        success=success,
        steps=step + 1,
        prompt_tokens=total_prompt,
        completion_tokens=total_completion,
        duration_s=time.monotonic() - start,
        patch_applied=patch_applied,
        test_output=last_test_output[:2000],
    )


# ---------------------------------------------------------------------------
# Build context for a given condition
# ---------------------------------------------------------------------------

def build_context(
    condition: str,
    query: str,
    graph,
    flat_nodes,
    minilm_idx,
    codesearch_idx,
    repo_root: Path,
    budget: int,
) -> str:
    from context_providers import (
        naive_context, bm25_context, dense_context,
        hybrid_context, tacm_context, tacm_dynamic_context,
        tacm_l4_context, tacm_dyn_l4_context, tacm_full_context,
    )

    if condition == "naive":
        return naive_context(repo_root, budget)
    elif condition == "bm25":
        return bm25_context(query, flat_nodes, budget)
    elif condition == "minilm":
        return dense_context(query, minilm_idx, budget, model_type="st")
    elif condition == "codesearch":
        return dense_context(query, codesearch_idx, budget, model_type="st")
    elif condition == "hybrid":
        return hybrid_context(query, flat_nodes, minilm_idx, budget)
    elif condition == "hybrid-cs":
        return hybrid_context(query, flat_nodes, codesearch_idx, budget)
    elif condition == "tacm":
        return tacm_context(graph, query, budget)
    elif condition == "tacm-dyn":
        return tacm_dynamic_context(graph, query, budget)
    elif condition == "tacm-l4":
        return tacm_l4_context(graph, query, budget)
    elif condition == "tacm-dyn-l4":
        return tacm_dyn_l4_context(graph, query, budget)
    elif condition == "tacm-full":
        return tacm_full_context(graph, query, budget)
    else:
        raise ValueError(f"Unknown condition: {condition}")


def load_dataset_bug_ids(
    dataset_path: Path,
    project: str,
    labels: set[str] | None = None,
) -> set[str]:
    """Load bug IDs for a project from a JSONL dataset manifest."""
    bug_ids: set[str] = set()
    with open(dataset_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            if row.get("project") != project:
                continue
            if labels and row.get("label") not in labels:
                continue
            bug_id = row.get("bug_id")
            if bug_id:
                bug_ids.add(bug_id)
    return bug_ids


# ---------------------------------------------------------------------------
# Benchmark runner
# ---------------------------------------------------------------------------

def run_benchmark(
    project: str,
    repo_root: Path,
    conditions: list[str],
    seeds: list[int],
    budget: int,
    max_bugs: int,
    bug_filter: str | None = None,
    dataset_path: Path | None = None,
    dataset_labels: set[str] | None = None,
) -> list[RunResult]:
    from bench_v2 import load_tasks
    from code_review_graph.graph import GraphStore
    from code_review_graph.incremental import get_db_path
    from tacm_v2.graph.builder import GraphBuilder
    from bench_v2 import _build_minilm_index, _build_codesearch_index

    print(f"\n=== Agent benchmark: {project} @ {repo_root} ===")
    print(f"  Conditions: {conditions}")
    print(f"  Seeds: {seeds}  Budget: {budget}  MaxBugs: {max_bugs}")

    tasks = load_tasks(project, repo_root, max_bugs=max_bugs, skip_no_query=True)
    if dataset_path is not None:
        allowed_bug_ids = load_dataset_bug_ids(dataset_path, project, dataset_labels)
        tasks = [t for t in tasks if t.bug_id in allowed_bug_ids]
        print(f"  Dataset filter: {len(allowed_bug_ids)} allowed bug IDs from {dataset_path.name}")
    if bug_filter:
        tasks = [t for t in tasks if t.bug_id == bug_filter]
    if not tasks:
        print("  No tasks.")
        return []

    print(f"  Tasks: {len(tasks)}")

    # Build indexes (once per project)
    print("  Building LayeredGraph...", end=" ", flush=True)
    store = GraphStore(get_db_path(repo_root))
    try:
        graph = GraphBuilder(store).build()
    finally:
        store.close()
    print("ok")

    store2 = GraphStore(get_db_path(repo_root))
    flat_nodes = [n for n in store2.get_nodes_by_kind(["Function"]) if not n.is_test]
    store2.close()

    needs_minilm = any(c in conditions for c in ("minilm", "hybrid"))
    needs_cs     = any(c in conditions for c in ("codesearch", "hybrid-cs"))

    print("  Building MiniLM index...", end=" ", flush=True)
    minilm_idx = _build_minilm_index(flat_nodes, str(repo_root)) if needs_minilm else None
    print("ok" if minilm_idx else ("SKIP" if not needs_minilm else "FAILED"))

    print("  Building CodeSearch index...", end=" ", flush=True)
    codesearch_idx = _build_codesearch_index(flat_nodes, str(repo_root)) if needs_cs else None
    print("ok" if codesearch_idx else ("SKIP" if not needs_cs else "FAILED"))

    from test_runner import get_test_file

    # Load existing valid results as checkpoint (skip re-running them)
    # A result is valid if it ran for >10s (real LLM call) or succeeded.
    # Runs completing in <10s with non-zero tokens are likely rate-limit echo failures
    # where _claude_code_call estimated tokens from prompt length without a real API call.
    checkpoint: set[tuple[str, str, int]] = set()
    existing_results: list[RunResult] = []
    for p in sorted(RESULTS_DIR.glob(f"{project}_*.jsonl")):
        try:
            with open(p) as f:
                for line in f:
                    d = json.loads(line)
                    r = RunResult(**d)
                    # Valid run: success, or ran for >10s with no timeout/rate-limit error
                    bad_error = any(kw in r.error.lower() for kw in ("rate", "echo", "timed out", "timeout", "401", "incorrect api"))
                    is_real_run = (
                        r.success
                        or (r.duration_s > 10.0 and not bad_error)
                        or (r.error and not bad_error)
                    )
                    if is_real_run:
                        key = (r.bug_id, r.condition, r.seed)
                        if key not in checkpoint:
                            checkpoint.add(key)
                            existing_results.append(r)
        except Exception:
            pass
    if checkpoint:
        print(f"  Checkpoint: {len(checkpoint)} prior valid runs loaded, will skip them")

    all_results: list[RunResult] = list(existing_results)
    total = len(tasks) * len(conditions) * len(seeds)
    done = 0

    for task in tasks:
        # Get test file from BugsInPy metadata
        bug_dir = BUGSINPY_ROOT / "projects" / project / "bugs" / task.bug_id.split("-")[-1]
        test_file = get_test_file(bug_dir)
        if not test_file:
            print(f"  {task.bug_id}: no test file, skipping")
            continue

        for condition in conditions:
            # Build context once per (task, condition) — same for all seeds
            try:
                ctx = build_context(condition, task.query, graph, flat_nodes,
                                    minilm_idx, codesearch_idx, repo_root, budget)
            except Exception as e:
                print(f"  {task.bug_id}/{condition}: context build failed: {e}")
                continue

            for seed in seeds:
                done += 1
                key = (task.bug_id, condition, seed)
                if key in checkpoint:
                    print(f"  [{done}/{total}] {task.bug_id} | {condition} | seed={seed} ... SKIP (checkpoint)")
                    continue
                print(f"  [{done}/{total}] {task.bug_id} | {condition} | seed={seed} ...",
                      end=" ", flush=True)
                result = run_agent(
                    bug_id=task.bug_id,
                    condition=condition,
                    seed=seed,
                    query=task.query,
                    context=ctx,
                    test_file=test_file,
                    repo_root=repo_root,
                )
                all_results.append(result)
                # Save immediately after each run (incremental checkpoint)
                RESULTS_DIR.mkdir(exist_ok=True)
                ckpt_path = RESULTS_DIR / f"{project}_{condition}_ckpt.jsonl"
                with open(ckpt_path, "a") as f:
                    f.write(json.dumps(asdict(result)) + "\n")

                status = "PASS" if result.success else "fail"
                err_str = f" ERR={result.error[:60]}" if result.error else ""
                print(f"{status} ({result.steps} steps, "
                      f"{(result.prompt_tokens+result.completion_tokens)//1000}K tok, "
                      f"{result.duration_s:.0f}s){err_str}")

                # Polite delay between calls to avoid rate limits on Copilot API
                call_delay = int(os.environ.get("AGENT_CALL_DELAY", "0"))
                if call_delay > 0 and done < total:
                    time.sleep(call_delay)

    return all_results


# ---------------------------------------------------------------------------
# Aggregate and print results
# ---------------------------------------------------------------------------

def print_results(results: list[RunResult], seeds: list[int]) -> None:
    import statistics

    if not results:
        print("No results.")
        return

    # Group by condition
    from collections import defaultdict
    by_condition: dict[str, list[RunResult]] = defaultdict(list)
    for r in results:
        by_condition[r.condition].append(r)

    # Per-task solve rate: task solved if ANY seed succeeded
    # Also report mean across seeds
    condition_order = ["naive", "bm25", "minilm", "hybrid", "tacm", "tacm-dyn", "tacm-l4", "tacm-dyn-l4"]
    present = [c for c in condition_order if c in by_condition]

    print("\n" + "="*80)
    print("AGENT BENCHMARK RESULTS")
    print("="*80)

    # Bootstrap CI on solve rate
    import random as rnd

    def boot_ci(successes: list[bool], n_boot=2000) -> tuple[float, float]:
        rng = rnd.Random(42)
        n = len(successes)
        if n == 0:
            return 0.0, 0.0
        vals = [sum(rng.choices(successes, k=n)) / n for _ in range(n_boot)]
        vals.sort()
        return vals[int(0.025 * n_boot)], vals[int(0.975 * n_boot)]

    print(f"\n  {'Condition':<16} {'Solve%':>7} {'CI95':>14} {'Steps':>6} "
          f"{'Tokens':>8}  {'1st-att%':>8}")
    print(f"  {'-'*65}")

    tacm_solve = None
    for cond in present:
        runs = by_condition[cond]
        successes = [r.success for r in runs]
        solve_pct = 100 * sum(successes) / len(successes)
        lo, hi = boot_ci(successes)
        steps_ok = [r.steps for r in runs if r.success]
        avg_steps = statistics.mean(steps_ok) if steps_ok else 0.0
        avg_tokens = statistics.mean(
            [(r.prompt_tokens + r.completion_tokens) for r in runs]
        ) / 1000
        # First-attempt solve: success on step 1
        first_att = 100 * sum(1 for r in runs if r.success and r.steps == 1) / len(runs)

        if cond == "tacm":
            tacm_solve = solve_pct

        print(f"  {cond:<16} {solve_pct:>6.0f}%  [{lo*100:>4.0f},{hi*100:>4.0f}]  "
              f"{avg_steps:>5.1f}  {avg_tokens:>7.0f}K  {first_att:>7.0f}%")

    # Per-task breakdown
    print(f"\n  Per-task solve (any seed):")
    bug_ids = sorted(set(r.bug_id for r in results))
    header = f"  {'Bug':<20} " + "  ".join(f"{c[:8]:>8}" for c in present)
    print(header)
    print(f"  {'-'*len(header.rstrip())}")
    for bug_id in bug_ids:
        row = f"  {bug_id:<20} "
        for cond in present:
            cond_runs = [r for r in by_condition[cond] if r.bug_id == bug_id]
            solved = any(r.success for r in cond_runs)
            row += f"  {'  PASS' if solved else '  fail':>8}"
        print(row)


# ---------------------------------------------------------------------------
# Save / load results
# ---------------------------------------------------------------------------

def save_results(results: list[RunResult], project: str, condition: str) -> Path:
    RESULTS_DIR.mkdir(exist_ok=True)
    ts = int(time.time())
    path = RESULTS_DIR / f"{project}_{condition}_{ts}.jsonl"
    with open(path, "w") as f:
        for r in results:
            f.write(json.dumps(asdict(r)) + "\n")
    return path


def _is_valid_result(r: RunResult) -> bool:
    """True if this result came from a real LLM call (not a rate-limit echo or timeout)."""
    bad_error = any(kw in r.error.lower() for kw in ("rate", "echo", "timed out", "timeout", "401", "incorrect api"))
    return (
        r.success
        or (r.duration_s > 10.0 and not bad_error)
        or (r.error and not bad_error)
    )


def load_all_results(project: str, valid_only: bool = True) -> list[RunResult]:
    """Load saved results, deduplicating by (bug_id, condition, seed).

    When valid_only=True (default), only keeps results from real LLM calls
    (duration > 10s and no timeout/rate-limit error). Within duplicates, the
    most recent valid result wins.
    """
    seen: dict[tuple, RunResult] = {}
    for p in sorted(RESULTS_DIR.glob(f"{project}_*.jsonl")):
        try:
            with open(p) as f:
                for line in f:
                    d = json.loads(line)
                    r = RunResult(**d)
                    if valid_only and not _is_valid_result(r):
                        continue
                    key = (r.bug_id, r.condition, r.seed)
                    seen[key] = r   # last file wins (sorted order = chronological)
        except Exception:
            pass
    return list(seen.values())


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="TACM-v2 agent harness benchmark")
    parser.add_argument("--project", help="thefuck | scrapy")
    parser.add_argument("--repo", type=Path)
    parser.add_argument("--condition", nargs="+",
                        default=["bm25", "minilm", "hybrid", "codesearch", "hybrid-cs", "tacm-full", "tacm-dyn", "tacm-dyn-l4"],
                        help="Retrieval conditions to run")
    parser.add_argument("--seeds", type=int, nargs="+", default=[42],
                        help="Random seeds (one run per seed per task)")
    parser.add_argument("--budget", type=int, default=DEFAULT_BUDGET)
    parser.add_argument("--max", type=int, default=30)
    parser.add_argument("--bug-id", help="Run only this specific bug ID")
    parser.add_argument("--dataset", type=Path,
                        help="Optional JSONL task manifest to filter bug IDs")
    parser.add_argument("--dataset-label", nargs="+",
                        default=["code_explicit", "semantic_code"],
                        help="Dataset labels to include when --dataset is set")
    parser.add_argument("--all", action="store_true", help="Run all configured repos")
    parser.add_argument("--report", action="store_true",
                        help="Load saved results and print report")
    args = parser.parse_args()

    configs = [
        ("thefuck", ROOT / "thefuck"),
        ("scrapy",  ROOT / "scrapy"),
    ]

    if args.report:
        for project, _ in configs:
            results = load_all_results(project)
            if results:
                print(f"\n=== {project} ===")
                print_results(results, args.seeds)
        return

    if args.all:
        for project, repo_root in configs:
            if not repo_root.exists():
                print(f"Skipping {project} — repo not found")
                continue
            results = run_benchmark(project, repo_root, args.condition,
                                    args.seeds, args.budget, args.max,
                                    dataset_path=args.dataset.resolve() if args.dataset else None,
                                    dataset_labels=set(args.dataset_label) if args.dataset else None)
            for cond in args.condition:
                cond_results = [r for r in results if r.condition == cond]
                if cond_results:
                    save_results(cond_results, project, cond)
            print_results(results, args.seeds)
    elif args.project and args.repo:
        results = run_benchmark(
            project=args.project,
            repo_root=args.repo.resolve(),
            conditions=args.condition,
            seeds=args.seeds,
            budget=args.budget,
            max_bugs=args.max,
            bug_filter=args.bug_id,
            dataset_path=args.dataset.resolve() if args.dataset else None,
            dataset_labels=set(args.dataset_label) if args.dataset else None,
        )
        for cond in args.condition:
            cond_results = [r for r in results if r.condition == cond]
            if cond_results:
                save_results(cond_results, args.project, cond)
        print_results(results, args.seeds)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
