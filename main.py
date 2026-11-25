#!/usr/bin/env python3
"""Laugh Track entry: writes one crypto-trading joke line to /output/entry.txt.

The joke is a fixed string, chosen by a pairwise self-judge tournament over 22
candidate lines against the competition's published judge brief (see DESIGN.md).
The program is deterministic: same input, same output, every run. No network,
no randomness, no secrets, no files outside this repository.
"""

import os

JOKE = "My tax spreadsheet has a tab called 'losses' and a tab called 'losses (emotional)'."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-check the gate before writing: the scorer accepts 1-200 characters.
    if not 1 <= len(JOKE) <= 200:
        raise SystemExit("joke must be 1-200 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: entry.txt holds exactly the 83-character joke line.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
