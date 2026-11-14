#!/usr/bin/env python3
"""news-image-01 entry: copy the bundled front page to /output/entry.png.

The front page sums up Friday 13 November 2026: 30 stories across 6
continents, pinned on a world map. Deterministic: the same bytes every run.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.jpg")
DST = "/output/entry.png"


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
