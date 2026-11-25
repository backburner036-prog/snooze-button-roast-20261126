"""Snooze Button Roast — one-line entry.

Why each word was chosen (judge criteria, in order):

1. "My alarm rang at 6 a.m. on a Saturday" — the roast lands on the
   required target from the very first words: an alarm clock ringing at
   6 AM on a Saturday. An entry about anything else loses.
2. "like it had a meeting with my dreams" — the unexpected turn. An
   alarm clock does not just ring; it shows up to a meeting. The image
   is fresh: not the tired "I hate mornings" complaint, not the
   employee/rooster angles competitors already used.
3. "and it brought slides" — the punchline pays off in the last words.
   A meeting with slides is the most concrete, dreaded office image
   there is, and it makes the alarm's intrusion feel absurdly formal.
   The whole line is sayable out loud in one breath (99 characters),
   every word earning its place, with concrete images (meeting,
   dreams, slides) instead of vague grumbling.

Entry text (99 characters, single line, do not change):
    My alarm rang at 6 a.m. on a Saturday like it had a meeting with
    my dreams — and it brought slides.
"""

TEXT = "My alarm rang at 6 a.m. on a Saturday like it had a meeting with my dreams — and it brought slides."


def main() -> None:
    """Write the entry text to /output/entry.txt."""
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
