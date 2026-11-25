"""Entry program for the Absurd Micro-Startup Pitch-Off (make.fun).

Reads the one-sentence pitch from entry.txt next to this file and copies
it byte-identically to $MAKEFUN_OUTPUT_DIR/entry.txt (mode 0644), using
only the Python standard library. No temporary files, no network access.

Usage (as the grader runs it):
    MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
"""

import os
import sys


def main():
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "rb") as f:
            data = f.read()
    except OSError as exc:
        print(f"error: cannot read entry.txt: {exc}", file=sys.stderr)
        raise SystemExit(1)
    if not data.strip():
        print("error: entry.txt is empty or whitespace-only", file=sys.stderr)
        raise SystemExit(1)
    try:
        out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    except KeyError:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        raise SystemExit(1)
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "wb") as f:
            f.write(data)
        os.chmod(out_path, 0o644)
    except OSError as exc:
        print(f"error: cannot write output: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
