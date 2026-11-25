"""The Funniest Honest Appliance Error — make.fun entry.

Writes one line (at most 200 characters): the funniest honest error
message an appliance could show. Standard library only.
"""

import os
import sys

ENTRY = (
    "Spin cycle aborted: the load is one sock and a house brick. "
    "I spun anyway. The brick won. "
    "I am a washing machine, not a demolition crew."
)
MAX_CHARS = 200


def main(argv):
    if len(ENTRY) < 1 or len(ENTRY) > MAX_CHARS:
        print("entry must be 1-200 characters", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    final_path = os.path.join(out_dir, "entry.txt")
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, final_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
