"""dashboard/app.py — Web dashboard for TACM-v2 benchmarking research.

Run from the project root:
    python3 dashboard/app.py

Then open http://localhost:5001
"""

from __future__ import annotations

import json
import os
import queue
import re
import subprocess
import sys
import threading
import uuid
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "archive" / "pre-research"))

from flask import Flask, Response, jsonify, render_template, request

app = Flask(__name__, template_folder="templates")

# ── Security constants ────────────────────────────────────────────────────────
_UUID_RE = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
)
_ALLOWED_PROJECTS = {"thefuck", "scrapy", "tornado", "pandas", "requests", "flask"}

# ── Active benchmark subprocess state ────────────────────────────────────────
_active_runs: dict[str, dict] = {}

# ── Hardcoded Experiment 02 results ──────────────────────────────────────────
EXPERIMENT_RESULTS: dict = {
    "meta": {
        "experiment": "EXPERIMENT_02",
        "date": "2026-04-09",
        "metric": "MRR and Hit% at top-10 FUNCTION-layer nodes",
        "dataset": "BugsInPy",
        "systems": ["BM25-Body", "RepoMap", "TACM-v2"],
    },
    "projects": {
        "thefuck": {"tasks": 26, "functions": 819,  "classes": 40,   "files": 416},
        "scrapy":  {"tasks": 19, "functions": 3063, "classes": 1287, "files": 445},
        "tornado": {"tasks": 4,  "functions": 2017, "classes": 727,  "files": 111},
    },
    "rows": [
        {"project": "thefuck", "budget": 800,  "bm25_hit": 96,  "rm_hit": 8, "v2_hit": 96,  "bm25_mrr": 0.4761, "rm_mrr": 0.0154, "v2_mrr": 0.4051},
        {"project": "thefuck", "budget": 4000, "bm25_hit": 96,  "rm_hit": 8, "v2_hit": 100, "bm25_mrr": 0.4761, "rm_mrr": 0.0154, "v2_mrr": 0.7981},
        {"project": "scrapy",  "budget": 800,  "bm25_hit": 79,  "rm_hit": 5, "v2_hit": 74,  "bm25_mrr": 0.6711, "rm_mrr": 0.0088, "v2_mrr": 0.6491},
        {"project": "scrapy",  "budget": 4000, "bm25_hit": 79,  "rm_hit": 5, "v2_hit": 79,  "bm25_mrr": 0.6711, "rm_mrr": 0.0088, "v2_mrr": 0.6506},
        {"project": "tornado", "budget": 800,  "bm25_hit": 100, "rm_hit": 0, "v2_hit": 100, "bm25_mrr": 0.6875, "rm_mrr": 0.0000, "v2_mrr": 0.7500},
        {"project": "tornado", "budget": 4000, "bm25_hit": 100, "rm_hit": 0, "v2_hit": 100, "bm25_mrr": 0.6875, "rm_mrr": 0.0000, "v2_mrr": 0.7083},
    ],
    "per_task": {
        "thefuck": [
            {"bug_id": "thefuck-1",  "bm25": 2,    "rm": None, "v2": 2,    "gt": "get_new_command"},
            {"bug_id": "thefuck-3",  "bm25": None, "rm": None, "v2": None, "gt": "info"},
            {"bug_id": "thefuck-4",  "bm25": 9,    "rm": None, "v2": 5,    "gt": "_get_aliases"},
            {"bug_id": "thefuck-5",  "bm25": 2,    "rm": None, "v2": 3,    "gt": "match"},
            {"bug_id": "thefuck-6",  "bm25": 2,    "rm": None, "v2": 2,    "gt": "match, get_new_command"},
            {"bug_id": "thefuck-7",  "bm25": 2,    "rm": None, "v2": 2,    "gt": "match, get_new_command"},
            {"bug_id": "thefuck-8",  "bm25": 3,    "rm": None, "v2": 2,    "gt": "_parse_operations"},
            {"bug_id": "thefuck-11", "bm25": 2,    "rm": None, "v2": 2,    "gt": "get_new_command"},
            {"bug_id": "thefuck-12", "bm25": 2,    "rm": None, "v2": 3,    "gt": "match"},
            {"bug_id": "thefuck-13", "bm25": 2,    "rm": None, "v2": 3,    "gt": "match"},
            {"bug_id": "thefuck-14", "bm25": 2,    "rm": None, "v2": 2,    "gt": "Fish._get_overridden_aliases"},
            {"bug_id": "thefuck-15", "bm25": 2,    "rm": None, "v2": 2,    "gt": "match, get_new_command"},
            {"bug_id": "thefuck-16", "bm25": 1,    "rm": 5,    "v2": 4,    "gt": "Bash.app_alias, app_alias"},
            {"bug_id": "thefuck-17", "bm25": 1,    "rm": 5,    "v2": 4,    "gt": "app_alias, get_aliases"},
            {"bug_id": "thefuck-18", "bm25": 2,    "rm": None, "v2": 3,    "gt": "match"},
            {"bug_id": "thefuck-19", "bm25": 2,    "rm": None, "v2": 2,    "gt": "get_new_command"},
            {"bug_id": "thefuck-20", "bm25": 2,    "rm": None, "v2": 2,    "gt": "_is_bad_zip, get_new_command"},
            {"bug_id": "thefuck-21", "bm25": 2,    "rm": None, "v2": 3,    "gt": "match"},
            {"bug_id": "thefuck-22", "bm25": 3,    "rm": None, "v2": 3,    "gt": "_realise"},
            {"bug_id": "thefuck-24", "bm25": 2,    "rm": None, "v2": 2,    "gt": "CorrectedCommand.__init__, __eq__"},
            {"bug_id": "thefuck-25", "bm25": 2,    "rm": None, "v2": 2,    "gt": "get_new_command"},
            {"bug_id": "thefuck-26", "bm25": 2,    "rm": None, "v2": 2,    "gt": "get_new_command"},
            {"bug_id": "thefuck-27", "bm25": 2,    "rm": None, "v2": 2,    "gt": "get_new_command"},
            {"bug_id": "thefuck-28", "bm25": 2,    "rm": None, "v2": 2,    "gt": "get_new_command"},
            {"bug_id": "thefuck-29", "bm25": 10,   "rm": None, "v2": 2,    "gt": "update"},
            {"bug_id": "thefuck-30", "bm25": 2,    "rm": None, "v2": 3,    "gt": "match"},
        ],
        "scrapy": [
            {"bug_id": "scrapy-14", "bm25": None, "rm": None, "v2": None, "gt": "is_gzipped"},
            {"bug_id": "scrapy-15", "bm25": None, "rm": None, "v2": None, "gt": "_safe_ParseResult"},
            {"bug_id": "scrapy-16", "bm25": None, "rm": None, "v2": None, "gt": "_safe_ParseResult, canonicalize_url"},
            {"bug_id": "scrapy-23", "bm25": None, "rm": None, "v2": None, "gt": "test_priority_adjust"},
            {"bug_id": "scrapy-27", "bm25": 1,    "rm": None, "v2": 9,    "gt": "process_response"},
        ],
        "tornado": [],
    },
    "findings": [
        {
            "id": 1,
            "color": "indigo",
            "title": "TACM-v2 decisively beats RepoMap on all projects",
            "body": "RepoMap achieves 0–8% Hit@10. TACM-v2 achieves 74–100%. Bug fix functions are low-centrality leaf functions invisible to PageRank-biased ranking.",
        },
        {
            "id": 2,
            "color": "emerald",
            "title": "+68% over BM25 at high budget (thefuck)",
            "body": "TACM-v2 MRR=0.798 vs BM25 MRR=0.476 at 4000 tokens. Containment bonus + multi-signal scoring pushes GT to rank 1–3 instead of rank 5–10.",
        },
        {
            "id": 3,
            "color": "amber",
            "title": "Budget-aware design tension at ≤800 tokens",
            "body": "Layered budget split reduces FUNCTION coverage at tight budgets. Fix: increase FUNCTION fraction from 75%→85% for BUG intent when budget ≤1000.",
        },
        {
            "id": 4,
            "color": "slate",
            "title": "Scrapy: TACM-v2 ties BM25, 3 of 4 misses are universal",
            "body": "3 misses (scrapy-14, -15, -16) fail all systems — zero lexical overlap. scrapy-27 is a real v2 weakness needing complexity weight increase (0.15→0.20).",
        },
    ],
}


# ── Routes ────────────────────────────────────────────────────────────────────

@app.route("/")
def index() -> str:
    return render_template("index.html")


@app.route("/api/results")
def api_results():
    return jsonify(EXPERIMENT_RESULTS)


@app.route("/api/benchmark/run", methods=["POST"])
def api_benchmark_run():
    data = request.get_json(force=True, silent=True) or {}

    project  = str(data.get("project", "thefuck"))
    repo_str = str(data.get("repo", f"./{project}"))
    budgets  = data.get("budgets", [4000])
    max_bugs = min(int(data.get("max_bugs", 30)), 50)
    top_k    = min(int(data.get("top_k", 10)), 20)

    if project not in _ALLOWED_PROJECTS:
        return jsonify({"error": "Unknown project"}), 400

    # Resolve repo path — must remain inside ROOT to prevent path traversal
    try:
        if Path(repo_str).is_absolute():
            repo_path = Path(repo_str).resolve()
        else:
            repo_path = (ROOT / repo_str).resolve()
        repo_path.relative_to(ROOT.resolve())  # raises ValueError if outside ROOT
    except ValueError:
        return jsonify({"error": "Repo path must be within project directory"}), 400

    if not repo_path.exists():
        return jsonify({"error": f"Repo not found: {repo_path.name}"}), 400

    budget_args: list[str] = []
    for b in budgets[:4]:
        try:
            budget_args += ["--budget", str(int(b))]
        except (ValueError, TypeError):
            pass
    if not budget_args:
        budget_args = ["--budget", "4000"]

    cmd = [
        sys.executable, str(ROOT / "bench_v2.py"),
        "--project", project,
        "--repo", str(repo_path),
        "--max", str(max_bugs),
        "--top-k", str(top_k),
        *budget_args,
    ]

    run_id = str(uuid.uuid4())
    q: queue.Queue[str | None] = queue.Queue()

    def _run() -> None:
        try:
            proc = subprocess.Popen(
                cmd, cwd=str(ROOT),
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                text=True, bufsize=1,
            )
            _active_runs[run_id]["proc"] = proc
            assert proc.stdout
            for line in proc.stdout:
                q.put(line)
            proc.wait()
        except Exception as exc:
            q.put(f"[ERROR] {exc}\n")
        finally:
            q.put(None)

    _active_runs[run_id] = {"q": q, "proc": None}
    threading.Thread(target=_run, daemon=True).start()
    return jsonify({"run_id": run_id})


@app.route("/api/benchmark/stream/<run_id>")
def api_benchmark_stream(run_id: str):
    if not _UUID_RE.match(run_id) or run_id not in _active_runs:
        return jsonify({"error": "Unknown run"}), 404

    q = _active_runs[run_id]["q"]

    def generate():
        while True:
            try:
                line = q.get(timeout=60)
            except queue.Empty:
                yield "data: \n\n"
                continue
            if line is None:
                yield "data: [DONE]\n\n"
                _active_runs.pop(run_id, None)
                return
            yield f"data: {json.dumps(line)}\n\n"

    return Response(
        generate(),
        mimetype="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


@app.route("/api/query", methods=["POST"])
def api_query():
    data    = request.get_json(force=True, silent=True) or {}
    query   = str(data.get("query", "")).strip()[:512]
    project = str(data.get("project", "thefuck"))
    budget  = min(int(data.get("budget", 4000)), 8000)
    top_k   = min(int(data.get("top_k", 10)), 20)

    if project not in _ALLOWED_PROJECTS:
        return jsonify({"error": "Unknown project"}), 400

    repo_root = ROOT / project
    if not repo_root.exists():
        return jsonify({"error": f"Repo not found at ./{project} — clone it first"}), 400

    if not query:
        return jsonify({"error": "Query is required"}), 400

    out: dict = {
        "query": query,
        "project": project,
        "budget": budget,
        "bm25": None,
        "tacm_v2": None,
        "tacm_v2_meta": None,
    }

    # ── BM25 ranking ──────────────────────────────────────────────────────────
    try:
        from code_review_graph.graph import GraphStore
        from code_review_graph.incremental import get_db_path
        from bench_v2 import bm25_rank_nodes

        store = GraphStore(get_db_path(repo_root))
        flat_nodes = [n for n in store.get_nodes_by_kind(["Function"]) if not n.is_test]
        store.close()

        ranked = bm25_rank_nodes(flat_nodes, query)
        out["bm25"] = [
            {
                "rank": i + 1,
                "name": node_id,
                "file": str(file_path or ""),
            }
            for i, (node_id, file_path) in enumerate(ranked[:top_k])
        ]
    except Exception as exc:
        out["bm25"] = {"error": str(exc)}

    # ── TACM-v2 ───────────────────────────────────────────────────────────────
    try:
        from code_review_graph.graph import GraphStore as _GS
        from code_review_graph.incremental import get_db_path as _gdb
        from tacm_v2.graph.builder import GraphBuilder
        from tacm_v2.selector.selector import select

        store2 = _GS(_gdb(repo_root))
        graph = GraphBuilder(store2).build()
        store2.close()

        result = select(graph, query, token_budget=budget)
        fn_nodes = [sn for sn in result.nodes if sn.layer.name == "FUNCTION"]

        out["tacm_v2"] = [
            {
                "rank": i + 1,
                "name": sn.node.node_id,
                "file": str(getattr(sn.node, "file_path", "") or ""),
                "score": round(getattr(sn, "score", 0.0), 4),
            }
            for i, sn in enumerate(fn_nodes[:top_k])
        ]
        out["tacm_v2_meta"] = {
            "intent":       getattr(getattr(result, "intent", None), "name", "UNKNOWN"),
            "total_tokens": getattr(result, "total_tokens", 0),
            "file_count":   sum(1 for sn in result.nodes if sn.layer.name == "FILE"),
            "class_count":  sum(1 for sn in result.nodes if sn.layer.name == "CLASS"),
            "fn_count":     len(fn_nodes),
        }
    except Exception as exc:
        out["tacm_v2"] = {"error": str(exc)}

    return jsonify(out)


if __name__ == "__main__":
    port = int(os.environ.get("DASHBOARD_PORT", 5001))
    app.run(debug=False, port=port, threaded=True)
