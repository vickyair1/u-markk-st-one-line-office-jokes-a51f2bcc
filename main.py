#!/usr/bin/env python3
"""One-Line Office Jokes — entry program.

Writes a single one-line joke about office life to /output/entry.txt
and prints it to stdout. Deterministic: same line every run.
"""

import os

JOKE = "Our office fridge runs on a sign-up sheet, a cleaning rota, and one yoghurt that is now the longest-serving member of staff."


def main():
    line = JOKE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 199, "entry must be 1-199 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
