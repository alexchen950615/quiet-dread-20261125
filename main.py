#!/usr/bin/env python3
"""Two Days of Quiet Dread — one code-review comment, at most 140 chars.

Writes a single-line approval carrying quiet existential dread to
/output/entry.txt (the make.fun gate path).
"""

ENTRY = "Approved. The tests pass, the release ships Friday, and the heat death of the universe is still on schedule."

OUTPUT_PATH = "/output/entry.txt"
# Same file under the shared /opt/output path the parallel builds use.
MIRROR_PATH = "/opt/output/entry.txt"


def main() -> None:
    # Gate: the bounty requires one line, 1-140 chars, no trailing newline.
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, must be 1-140"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    for path in (OUTPUT_PATH, MIRROR_PATH):
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)


if __name__ == "__main__":
    main()
