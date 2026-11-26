#!/usr/bin/env python3
"""The Moon Gets One Star.

Writes one line -- a one-star review of the Moon -- to /output/entry.txt.
"""

import os

LINE = "One star. After 4.5 billion years together it still only shows me one side. Worst long-term relationship ever."


def main() -> None:
    # Gate: the bounty only accepts a single line of 1-120 chars.
    assert 1 <= len(LINE) <= 120, f"entry line is {len(LINE)} chars, must be 1-120"
    assert "\n" not in LINE, "entry line must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
