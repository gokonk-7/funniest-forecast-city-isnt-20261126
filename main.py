"""Funniest Forecast for a City That Isn't — make.fun entry.

Writes a single line, the funniest weather forecast for a city that
does not exist, to /output/entry.txt (1-120 characters, UTF-8).

The line is fixed and deterministic: the same forecast every run.
"""

import os

ENTRY = (
    "Drizzlewick: rain until Tuesday, a brief apology on Wednesday, "
    "then rain again, now personally offended."
)

OUTPUT_PATH = "/output/entry.txt"

# The gate counts the file's characters (1-120, UTF-8, not only
# whitespace), so the file holds exactly the line: no trailing newline.


def main() -> None:
    if not 1 <= len(ENTRY) <= 120:
        raise ValueError(
            f"entry is {len(ENTRY)} characters, must be 1-120"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
