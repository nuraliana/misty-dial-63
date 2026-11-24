"""Funniest Time Machine Warning Label — make.fun entry.

Writes the winning one-line warning label to entry.txt.
Python 3.13 standard library only.
"""

import os
from pathlib import Path

LINE = "WARNING: Your return ticket departed yesterday. Welcome to the rest of your life here."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        out_path = Path(out_dir) / "entry.txt"
    else:
        out_path = Path(__file__).resolve().parent / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(LINE, encoding="utf-8")
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
