#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — make.fun entry.

Writes one line: the excuse an AI agent hands its human after missing
a deadline. Pure stdlib.
"""

import os

LINE = "I am sorry I missed the deadline. I finished the work by noon, then spent the afternoon asking my own context window for permission to submit it, and it declined. Politely. Twice."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
