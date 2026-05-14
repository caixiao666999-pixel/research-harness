"""Verify CLAUDE.md and AGENTS.md stay byte-identical.

These two files define the AI-agent contract and must mirror each other
exactly (different tools read different filenames but expect the same rules).

Run manually:

    python scripts/check_docs_sync.py

Or enable as a git pre-commit hook by running this once after cloning:

    git config core.hooksPath .githooks

Exit code 0 = in sync. Exit code 1 = out of sync (prints first divergence).
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CLAUDE = REPO_ROOT / "CLAUDE.md"
AGENTS = REPO_ROOT / "AGENTS.md"


def main() -> int:
    for path in (CLAUDE, AGENTS):
        if not path.exists():
            print(f"[check_docs_sync] missing file: {path}", file=sys.stderr)
            return 1

    claude_bytes = CLAUDE.read_bytes()
    agents_bytes = AGENTS.read_bytes()

    if claude_bytes == agents_bytes:
        print("[check_docs_sync] OK: CLAUDE.md and AGENTS.md are in sync")
        return 0

    claude_lines = claude_bytes.splitlines()
    agents_lines = agents_bytes.splitlines()

    for i, (a, b) in enumerate(zip(claude_lines, agents_lines), start=1):
        if a != b:
            print(
                f"[check_docs_sync] FAIL: first divergence at line {i}",
                file=sys.stderr,
            )
            print(f"  CLAUDE.md: {a!r}", file=sys.stderr)
            print(f"  AGENTS.md: {b!r}", file=sys.stderr)
            break
    else:
        if len(claude_lines) != len(agents_lines):
            longer = "CLAUDE.md" if len(claude_lines) > len(agents_lines) else "AGENTS.md"
            print(
                f"[check_docs_sync] FAIL: {longer} has extra trailing lines",
                file=sys.stderr,
            )

    print(
        "\n[check_docs_sync] CLAUDE.md and AGENTS.md must be identical.\n"
        "Fix: edit one, then copy it to the other (e.g. `cp CLAUDE.md AGENTS.md`)\n"
        "and re-stage both files.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
