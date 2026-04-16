"""test_runner.py — Run BugsInPy task tests and capture results.

Sets up the Python environment at the repo's buggy state commit and runs
the designated test file. Returns pass/fail + output for the agent harness.

Note: Full environment setup (virtualenv per Python version) is expensive.
For the agent benchmark we run tests in the *current* repo environment
(assuming deps are pre-installed) and score pass/fail on the designated
test file only, not the full test suite.
"""

from __future__ import annotations

import subprocess
import time
from dataclasses import dataclass
from pathlib import Path


@dataclass
class TestResult:
    passed: bool
    returncode: int
    stdout: str
    stderr: str
    duration_s: float
    test_file: str


def run_tests(
    repo_root: Path,
    test_file: str,
    timeout: int = 60,
) -> TestResult:
    """Run a single BugsInPy test file with pytest.

    Args:
        repo_root: absolute path to the repo
        test_file: relative path like "tests/test_rules/test_pip_unknown_command.py"
        timeout: seconds before giving up

    Returns TestResult with passed=True if all tests in the file pass.
    """
    test_path = repo_root / test_file
    if not test_path.exists():
        return TestResult(
            passed=False, returncode=-1,
            stdout="", stderr=f"Test file not found: {test_path}",
            duration_s=0.0, test_file=test_file,
        )

    start = time.monotonic()
    try:
        r = subprocess.run(
            ["python3", "-m", "pytest", str(test_path), "-x", "-q",
             "--tb=short", "--no-header", "-p", "no:playwright"],
            cwd=repo_root, capture_output=True, text=True, timeout=timeout,
        )
        elapsed = time.monotonic() - start
        passed = r.returncode == 0
        return TestResult(
            passed=passed,
            returncode=r.returncode,
            stdout=r.stdout[-3000:],   # trim to last 3k chars
            stderr=r.stderr[-2000:],
            duration_s=elapsed,
            test_file=test_file,
        )
    except subprocess.TimeoutExpired:
        elapsed = time.monotonic() - start
        return TestResult(
            passed=False, returncode=-1,
            stdout="", stderr=f"Tests timed out after {timeout}s",
            duration_s=elapsed, test_file=test_file,
        )
    except Exception as e:
        return TestResult(
            passed=False, returncode=-1,
            stdout="", stderr=str(e),
            duration_s=0.0, test_file=test_file,
        )


def get_test_file(bug_dir: Path) -> str:
    """Read the test file path from bug.info."""
    info = bug_dir / "bug.info"
    if not info.exists():
        return ""
    for line in info.read_text().splitlines():
        if line.startswith("test_file="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    return ""


def format_test_feedback(result: TestResult) -> str:
    """Format test result as agent-readable feedback string."""
    if result.passed:
        return f"TESTS PASSED ({result.test_file}, {result.duration_s:.1f}s)"
    lines = []
    lines.append(f"TESTS FAILED ({result.test_file}, returncode={result.returncode})")
    if result.stdout:
        lines.append("--- stdout ---")
        lines.append(result.stdout)
    if result.stderr:
        lines.append("--- stderr ---")
        lines.append(result.stderr)
    return "\n".join(lines)
