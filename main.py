"""Roast the Smart Fridge entry program.

The roast is pre-written in entry.txt; this program only copies it
into the grader's output directory, unchanged.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.txt"))
    # The file is copied as-is on purpose: the joke lives in the exact
    # wording of the roast, so this program must never re-render or
    # rephrase it — a byte-for-byte copy keeps the punchline intact.


if __name__ == "__main__":
    main()
