#!/usr/bin/env python3
"""One-Liner Marathon entry: a single original one-line joke.

Writes exactly one joke (one line, under 180 chars) to /output/entry.txt.
"""

import os

JOKE = "I asked my GPS for the meaning of life. It said 'recalculating' - and honestly, so did I."


def validate_joke(joke: str) -> str:
    """Enforce the bounty gate: one line, 1-280 chars, non-empty."""
    text = joke.strip()
    if not text:
        raise ValueError("joke must not be empty")
    if "\n" in text:
        raise ValueError("joke must be a single line")
    if not 1 <= len(text) <= 280:
        raise ValueError(f"joke must be 1-280 chars, got {len(text)}")
    return text


def write_entry(joke: str, path: str = "/output/entry.txt") -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(joke + "\n")


def main() -> None:
    write_entry(validate_joke(JOKE))


if __name__ == "__main__":
    main()
