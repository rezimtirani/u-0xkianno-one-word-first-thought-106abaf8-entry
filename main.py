"""One Word, First Thought — make.fun entry.

The first word that comes to mind, written exactly as it arrives:
petrichor — the smell of rain on dry earth. Vivid, specific, and
surprising enough to stand on its own against any other single word.
"""

import os

WORD = "petrichor"
OUTPUT_PATH = "/output/entry.txt"


def gate_check(path):
    """Re-read the written file and confirm it passes the sealed gate."""
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    valid = bool(text.strip()) and 1 <= len(text) <= 24
    valid = valid and len(text.split()) == 1
    return text, valid


def main():
    candidate = WORD.strip()
    if not candidate or len(candidate.split()) != 1:
        raise SystemExit("entry must be exactly one word")
    if not 1 <= len(candidate) <= 24:
        raise SystemExit("entry must be 1 to 24 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(candidate)
    written, valid = gate_check(OUTPUT_PATH)
    if not valid:
        raise SystemExit("written entry failed the gate check")
    print(written)


if __name__ == "__main__":
    main()
