#!/usr/bin/env python3
"""Texts From Your Future Self — one funny text from the future self (make.fun entry).

Writes the entry text to /output/entry.txt (exactly 122 characters, no
trailing newline).
"""

import os

ENTRY = "It's you from 2041. The thermostat war ends today. You lose. It's 31 degrees forever now. Wear shorts to your own wedding."
OUT_PATH = "/output/entry.txt"


def validate_entry(entry):
    if not isinstance(entry, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(entry) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not entry.strip():
        raise ValueError("entry must not be blank")


def main():
    validate_entry(ENTRY)
    if not ENTRY.startswith("It's you from 2041"):
        raise ValueError("entry must start with \"It's you from 2041\"")
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUT_PATH, 0o644)
    with open(OUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY or len(written.encode("utf-8")) != len(ENTRY.encode("utf-8")):
        raise ValueError("written entry does not match ENTRY")


if __name__ == "__main__":
    main()
