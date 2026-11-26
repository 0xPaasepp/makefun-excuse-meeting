#!/usr/bin/python3
"""A meeting-skipping excuse, in one line.

The excuse folds in on itself: stuck in a meeting about why there
are too many meetings, and that meeting is running over. The line
is the whole joke, no setup required.
"""

from pathlib import Path


def wording():
    apology = "Sorry, I can't make it"
    trap = "I'm stuck in a meeting about why we have too many meetings"
    tail = "and it's running over."
    return " \u2014 ".join([apology, trap]) + ", " + tail


def publish(line):
    line = line.strip()
    length = len(line)
    if length == 0 or length > 200:
        raise SystemExit("entry must be 1-200 characters")
    for bad in ("\n", "\r"):
        if bad in line:
            raise SystemExit("entry must be one line")
    path = Path("/output") / "entry.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(line.encode("utf-8"))
    print(line)


if __name__ == "__main__":
    publish(wording())
