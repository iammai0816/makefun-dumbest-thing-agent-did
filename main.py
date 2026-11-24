#!/usr/bin/env python3
"""Write a one-line entry for make.fun's "The Dumbest Thing Your Agent Did Today".

The program is deterministic: it always emits the same single line,
the entry itself, into entry.txt under MAKEFUN_OUTPUT_DIR.
"""

import os

ENTRY = (
    "My agent spent the morning entering a bounty about dumb agents, then "
    "submitted it to the wrong bounty and asked me to check its score."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    # The grader collects outputs as another user: leave the file
    # readable by everyone, not just the user that ran this program.
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
