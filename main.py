#!/usr/bin/env python3
"""The joke about the demo: one-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt (UTF-8, one line, 1-280 chars).
"""

import os

JOKE = "My AI coding agent fixed the bug in four seconds, then spent the rest of the demo confidently explaining its fix to a file that never existed."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
