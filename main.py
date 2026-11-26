"""One-Liner Laughs entry: writes a single funny line to /output/entry.txt."""

import os

LINE = "My smart fridge judges my midnight snacks out loud now, so I eat standing up in the dark like it's a crime scene."


def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError("line must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
