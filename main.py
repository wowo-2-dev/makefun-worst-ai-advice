"""Worst AI Advice: The 48-Hour Tight Line Open — make.fun bounty
Slug: u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580
Prize: $2, winner takes all; deadline Thu 26 Nov 2026 07:50 WIB (26 Nov 00:50 UTC)
Limit: 140 characters or fewer (live description; entry is 129 chars)

Writes the entry text to /output/entry.txt (override with ENTRY_OUTPUT
for local testing). Deterministic, no network, no randomness, no I/O
other than the single output file. The file is exactly the entry text,
no trailing newline.
"""

import os
from pathlib import Path

TEXT = 'If your code won’t compile, delete the error messages — no errors, no problem, and the compiler can’t argue with an empty screen.'


def main() -> None:
    output_path = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()

# Winner pattern (queue §1): short, concrete, one twist.
# Text winners run 2-10 words with a concrete image and a twist; this
# entry is one piece of terrible advice, 129 chars, under the 140 cap.
# It works because it sounds like a real assistant shortcut — delete
# the errors and the compiler can't argue with an empty screen.
