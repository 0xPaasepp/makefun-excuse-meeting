#!/usr/bin/env python3
# Excuse entry: one line for skipping a pointless meeting, to /output/entry.txt.
# Pure standard library. The gate wants 1-200 characters, a single line.
# The joke: skipping a meeting because you are stuck in a meeting about
# why there are too many meetings — the excuse eats its own tail.

from pathlib import Path

LINE = "Sorry, I can't make it — I'm stuck in a meeting about why we have too many meetings, and it's running over."
TARGET = Path("/output/entry.txt")


def run() -> None:
    text = LINE.strip()
    assert 0 < len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    run()
