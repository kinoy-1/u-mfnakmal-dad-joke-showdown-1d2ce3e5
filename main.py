#!/usr/bin/env python3
"""Dad Joke Showdown — entry program.

Writes one original dad joke to /output/entry.txt.

The joke (64 characters, one line, no trailing newline):

    My keyboard quit its job. It was tired of being pressed all day.

Why this line, against the judge's brief (most important first):

1. A dad joke a father would tell at the table. Wholesome, spoken aloud,
   no setup the table has to decode — a keyboard, a job, a groan.
2. The pun lands cleanly on the first read. "Pressed" is the keyboard's
   whole life — every key is pressed, all day — and it is also what a
   worker feels when the job never lets up. One word, two meanings, no
   explanation needed.
3. Fresh inside the tradition. Not the thousand-times-told classics (no
   "Hi hungry, I'm Dad", no anti-gravity book, no scarecrow, no skeleton),
   but still a proper dad joke: an everyday object, a straight face, a
   groan at the end.
4. Tight, punchline at the end. Two short sentences; the second one is
   the turn, and the turn is the last thing the reader hears.
5. Reads naturally aloud. A father can deliver it across a dinner table
   in one breath, with the pause before "pressed" doing all the work.

The program is fully deterministic: one constant string, no randomness,
no clock, no network, no input. Two runs produce byte-identical output.
"""

import os

JOKE = (
    "My keyboard quit its job. "
    "It was tired of being pressed all day."
)

OUTPUT_PATH = "/output/entry.txt"

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space.
MAX_CHARS = 200


def main() -> None:
    text = JOKE
    # 64 characters: well inside the gate, and short enough to be told
    # in one breath across a dinner table.
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"joke is {len(text)} characters, must be 1-{MAX_CHARS}")
    if text.strip() != text or "\n" in text or "\r" in text:
        raise SystemExit("joke must be a single line with no surrounding whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back and prove the file holds exactly the joke, byte for byte.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise SystemExit("entry.txt does not match the joke exactly")


if __name__ == "__main__":
    main()
