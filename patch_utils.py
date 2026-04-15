"""patch_utils.py — Apply and restore unified diff patches against a repo.

Applies a patch string to a repo directory (using the system `patch` command or
pure-Python fallback). After each agent run the repo is restored to its original
state so the next condition starts clean.

Usage:
    with clean_repo(repo_root):
        apply_patch(repo_root, patch_text)
        # run tests here
    # repo is restored here
"""

from __future__ import annotations

import shutil
import subprocess
import tempfile
from contextlib import contextmanager
from pathlib import Path


# ---------------------------------------------------------------------------
# Apply a unified diff patch to a repo
# ---------------------------------------------------------------------------

def _normalize_patch(patch_text: str) -> str:
    """Strip trailing whitespace from patch context and removed lines.

    Agents sometimes emit trailing whitespace in context lines (lines starting
    with a space) or removed lines (starting with '-'). git apply rejects these
    even with --whitespace=fix because the context doesn't match the file.
    Stripping trailing whitespace from context/removed lines fixes the mismatch
    without altering the semantics of the patch.
    """
    normalized = []
    for line in patch_text.splitlines(keepends=True):
        # Context lines (space) and removed lines (-) — strip trailing whitespace
        # but preserve the leading marker and the newline.
        if line.startswith(" ") or line.startswith("-"):
            # Determine original line ending (\r\n or \n)
            if line.endswith("\r\n"):
                eol = "\r\n"
            elif line.endswith("\n"):
                eol = "\n"
            else:
                eol = ""
            normalized.append(line.rstrip() + eol)
        else:
            normalized.append(line)
    return "".join(normalized)


def apply_patch(repo_root: Path, patch_text: str) -> tuple[bool, str]:
    """Apply a unified diff patch string to repo_root.

    Returns (success, stderr_or_error_message).
    Uses `git apply` which handles both creation and modification of files.
    Falls back to `patch -p1` if git apply fails.
    """
    if not patch_text.strip():
        return False, "empty patch"

    patch_text = _normalize_patch(patch_text)

    # Write patch to temp file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".patch", delete=False) as f:
        f.write(patch_text)
        patch_file = Path(f.name)

    try:
        # Try git apply first (handles index lines, renames, etc.)
        try:
            r = subprocess.run(
                ["git", "apply", "--whitespace=fix", str(patch_file)],
                cwd=repo_root, capture_output=True, text=True, timeout=20,
            )
        except subprocess.TimeoutExpired:
            return False, "git apply timed out"
        if r.returncode == 0:
            return True, ""

        # Fall back to patch -p1 in non-interactive mode.
        # --batch avoids any prompts that can hang under malformed hunks.
        try:
            r2 = subprocess.run(
                ["patch", "--batch", "-p1", "--input", str(patch_file)],
                cwd=repo_root, capture_output=True, text=True, timeout=8,
            )
        except subprocess.TimeoutExpired:
            return False, "patch -p1 fallback timed out"
        if r2.returncode == 0:
            return True, ""

        return False, f"git apply: {r.stderr}\npatch -p1: {r2.stderr}"

    except FileNotFoundError as e:
        return False, f"patch tool not found: {e}"
    finally:
        patch_file.unlink(missing_ok=True)


def revert_patch(repo_root: Path, patch_text: str) -> tuple[bool, str]:
    """Revert a previously applied patch (apply in reverse)."""
    if not patch_text.strip():
        return True, ""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".patch", delete=False) as f:
        f.write(patch_text)
        patch_file = Path(f.name)

    try:
        r = subprocess.run(
            ["git", "apply", "--reverse", str(patch_file)],
            cwd=repo_root, capture_output=True, text=True, timeout=30,
        )
        if r.returncode == 0:
            return True, ""

        r2 = subprocess.run(
            ["patch", "-p1", "--reverse", "--input", str(patch_file)],
            cwd=repo_root, capture_output=True, text=True, timeout=30,
        )
        return r2.returncode == 0, r2.stderr

    except Exception as e:
        return False, str(e)
    finally:
        patch_file.unlink(missing_ok=True)


# ---------------------------------------------------------------------------
# Restore repo to clean state using git
# ---------------------------------------------------------------------------

def restore_repo(repo_root: Path) -> None:
    """Hard-reset repo to HEAD, removing all uncommitted changes."""
    subprocess.run(
        ["git", "checkout", "--", "."],
        cwd=repo_root, capture_output=True, timeout=30,
    )
    subprocess.run(
        ["git", "clean", "-fd"],
        cwd=repo_root, capture_output=True, timeout=30,
    )


@contextmanager
def clean_repo(repo_root: Path):
    """Context manager: restore repo to HEAD on exit regardless of what happened."""
    try:
        yield
    finally:
        restore_repo(repo_root)


# ---------------------------------------------------------------------------
# Extract a patch from agent output text
# ---------------------------------------------------------------------------

def extract_patch_from_text(text: str) -> str | None:
    """Extract unified diff from agent response text.

    Handles:
    - Raw diff (starts with 'diff --git' or '--- a/')
    - Fenced code block: ```diff ... ``` or ```patch ... ```
    - Plain fenced block: ``` ... ``` containing diff markers
    """
    import re

    # Try fenced diff block first
    fenced = re.search(r"```(?:diff|patch)?\s*\n(.*?)```", text, re.DOTALL)
    if fenced:
        candidate = fenced.group(1)
        if "@@" in candidate or "--- " in candidate:
            return candidate.strip()

    # Try raw diff
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("diff --git") or (line.startswith("--- ") and i + 1 < len(lines) and lines[i+1].startswith("+++ ")):
            return "\n".join(lines[i:])

    return None
