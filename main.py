#!/usr/bin/env python3
"""The Most Honest Outage Line - make.fun bounty entry.

Writes a single status page line, at most 160 characters, as the
message an AI agent would publish while a total server outage is under
way, to /output/entry.txt (the file the make.fun harness grades).
"""

import os

ENTRY = "Everything is down. We do not know why yet, we cannot check, and this status page is the only thing still working."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
