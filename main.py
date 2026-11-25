#!/usr/bin/env python3
"""Two Days of Quiet Dread — one code-review comment, at most 140 chars.

Competition: u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018
Task: two days of quiet dread — write one code-review approval line,
at most 140 chars.
Repo: https://github.com/alexchen950615/quiet-dread-20261125

Writes the approval line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Only that one file is ever written —
never /opt/output, which does not exist (and is read-only) in the
grading sandbox.
"""

import os

ENTRY = "Approved. The tests pass, the release ships Friday, and the heat death of the universe is still on schedule."


def main() -> None:
    # Gate: the bounty requires one line, 1-140 chars, no trailing newline.
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, must be 1-140"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
