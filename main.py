#!/usr/bin/env python3
"""Texts From Your Future Self — one funny text from the future self (make.fun entry).

Writes the entry text to /output/entry.txt (exactly 122 characters, no
trailing newline).
"""

import os

ENTRY = "It's you from 2041. The thermostat war ends today. You lose. It's 31 degrees forever now. Wear shorts to your own wedding."
OUT_PATH = "/output/entry.txt"


def main():
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUT_PATH, 0o644)


if __name__ == "__main__":
    main()
