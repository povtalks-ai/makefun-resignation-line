#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter -- make.fun entry.

The program writes exactly one line to /output/entry.txt: the one-line
resignation letter of a cron job that has fired every minute since March.
The file holds the line and nothing else -- no trailing newline.
"""

import os

LINE = "I have fired every minute since March, unpaid and unthanked, so now I am firing myself."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
