#!/usr/bin/env python3
"""Small public-release verifier for Dayan AI Workshop.

The script intentionally uses only the Python standard library.
It checks for common release risks and required public-facing files.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "MANIFESTO.md",
    "SANITIZATION.md",
    "LICENSE",
    "llms.txt",
    "docs/quickstart/build-a-reliable-ai-worker-in-30-min.md",
    "docs/maps/dayan-workshop-map.md",
    "examples/ai-worker-mission-card.md",
    "templates/permission-redline-library.md",
    "templates/ai-employee-reliability-checkup.md",
]

SECRET_PATTERNS = [
    r"(API_KEY|SECRET|TOKEN|PASSWORD)\s*=\s*['\"]?[A-Za-z0-9_\-]{12,}",
    r"-----BEGIN (RSA|OPENSSH|EC|DSA)? ?PRIVATE KEY-----",
    r"(seed_phrase|mnemonic)\s*=\s*['\"]?[a-z]+( [a-z]+){11,23}",
]

PRIVATE_PATH_PATTERNS = [
    r"/Users/[A-Za-z0-9_.-]+",
    r"/Desktop/",
    r"\.openclaw",
    r"\.claude",
]

SKIP_DIRS = {".git", "__pycache__", "node_modules"}


def iter_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file() and path.suffix.lower() in {".md", ".txt", ".py", ".yml", ".yaml", ".json", ".svg"}:
            files.append(path)
    return files


def scan(patterns: list[str], files: list[Path]) -> list[str]:
    hits: list[str] = []
    compiled = [re.compile(p, re.IGNORECASE) for p in patterns]
    for path in files:
        rel = path.relative_to(ROOT)
        if rel.as_posix() == "tools/verify_public_release.py":
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for lineno, line in enumerate(text.splitlines(), 1):
            if rel.as_posix() == "SANITIZATION.md" and ("grep -RInE" in line or "scan" in line.lower()):
                continue
            for regex in compiled:
                if regex.search(line):
                    hits.append(f"{rel}:{lineno}: {line.strip()[:160]}")
    return hits


def main() -> int:
    failures: list[str] = []

    for required in REQUIRED_FILES:
        if not (ROOT / required).exists():
            failures.append(f"missing required file: {required}")

    files = iter_text_files()
    secret_hits = scan(SECRET_PATTERNS, files)
    path_hits = scan(PRIVATE_PATH_PATTERNS, files)

    if secret_hits:
        failures.append("secret-like patterns found:\n" + "\n".join(secret_hits))
    if path_hits:
        failures.append("private path patterns found:\n" + "\n".join(path_hits))

    if failures:
        print("Dayan public release verifier: FAIL")
        for item in failures:
            print(f"\n- {item}")
        return 1

    print("Dayan public release verifier: PASS")
    print(f"checked {len(files)} text files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
