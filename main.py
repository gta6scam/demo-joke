"""Demo joke entry for the-joke-about-the-demo-20261121-0551.

The joke's angle: the demo worked perfectly at 9:00 — then the AI pair
programmer "improved" it, and the fix was so thorough the demo is now
scheduled for 9:00 *next week*. The crash is the punchline: every developer
who has watched a working demo die five minutes before showtime recognises
the truth of it. Surprising, but painfully plausible.

Writes the single joke text to /output/entry.txt (UTF-8, no added newline
handling beyond the text itself), with no dependencies and no network.

Why the punchline lands: the setup promises a perfect demo at 9:00, and
the twist is not a crash but an "improvement" — the AI pair programmer's
help is so complete that the demo quietly slips a whole week. The surprise
is the jump to "9:00 next week": nobody expects a working demo to be
rescheduled by its own helper. It stays believable because every developer
has watched an AI suggestion break something that already worked, so the
audience laughs in recognition rather than at an absurdity.
"""

TEXT = "The demo worked perfectly at 9:00. At 9:05 my AI pair programmer 'improved' it. The demo is now at 9:00 next week."


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    # newline="" keeps the write byte-exact: no platform line-ending
    # translation is applied, so entry.txt contains TEXT and nothing else.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
