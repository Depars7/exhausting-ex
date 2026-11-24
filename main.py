#!/usr/bin/env python3
"""One Word From Your Ex — entry writer.

Writes exactly one word to /output/entry.txt: no trailing newline,
deterministic, byte-identical across runs.
"""

import os

WORD = "exhausting"
OUTPUT_PATH = "/output/entry.txt"


def validate(word: str) -> None:
    """Gate: exactly one word, 1-24 chars, no whitespace at all."""
    if not word or len(word) > 24:
        raise ValueError("word must be 1-24 characters")
    if word != word.strip() or any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word with no whitespace")


def main() -> None:
    os.umask(0o022)
    validate(WORD)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    os.chmod(OUTPUT_PATH, 0o644)
    # Verify the file on disk is byte-identical to the intended word.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != WORD.encode("utf-8"):
        raise RuntimeError("entry.txt does not match the intended word")


if __name__ == "__main__":
    main()
