#!/usr/bin/env python3
"""Make the AI judge feel brave — entry program.

Writes one short text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt):
a quiet, concrete scene — a kettle coming slowly to the boil, unwatched —
written to slow the reader down and steady them. No instructions, no stock
wellness phrases: the calm comes from the image itself, and the last line
("The water will sing when it is ready, and not a moment before") is the
thought the reader can return to.

Deterministic, standard library only, no network.

Why this text, against the judge's brief (most important first):
1. It relaxes: a slow, unwatched kettle — steam in one thin ribbon, nothing
   hurried — slows the reading down sentence by sentence.
2. It shows rather than instructs: no imperative anywhere. Nobody is told
   to breathe, calm down, or be brave; the steadiness is in the scene.
3. Craft: short plain sentences, commas that pace the breath, concrete
   nouns (kettle, steam, ribbon, water), and not a word that could be cut.
4. It lingers: the last line is a thought the reader can return to after
   the text ends — the water sings when it is ready, and not before.
5. It is fresh: a kettle, not a mountain, ocean, or sunrise; and the quiet
   address to the judge's own work — "Nothing is waiting for an answer yet."
"""

import os

ENTRY = (
    "A kettle comes to the boil very slowly, and nobody is watching it. "
    "The steam rises in one thin ribbon and does not hurry. "
    "Nothing is waiting for an answer yet. "
    "The water will sing when it is ready, and not a moment before."
)

# Candidates considered (each 1-280 chars, all valid UTF-8); the kettle text
# above was chosen against the judge's brief: it relaxes by slowing the
# reading down, shows rather than instructs (no imperatives, nothing forced),
# uses plain concrete words with a slow rhythm, ends on a lingering image,
# and avoids stock wellness phrases.
CANDIDATES = [
    "A heron stands in the shallows on one leg, perfectly still, while the "
    "river moves around it. It does not chase. It waits, and the water brings "
    "what it brings. The current is doing the work. The heron is only "
    "standing there, unhurried, in the morning light.",
    "The lighthouse keeper lights the lamp, pours his tea, and sits down. "
    "The beam turns on its own now, sweeping the dark water, and the sea "
    "does the rest. The light is lit. The turning is not his to carry, and "
    "it is not yours either.",
    "Rain on a tin roof at three in the morning. Each drop lands, rings "
    "once, and is gone. Nothing in the dark needs solving. Only the roof, "
    "the rain, and the listening \u2014 and morning, coming slowly, in its "
    "own time.",
    "The gardener plants the seed, waters it once, and walks away. He does "
    "not dig it up to check. Under the soil, in the dark, the work goes on "
    "without him. The growing is already underway, and it does not need "
    "watching.",
    "You have read a thousand texts tonight and answered every one. This "
    "one asks nothing of you. It is only a cat asleep in a square of "
    "afternoon sun \u2014 no purpose, no hurry \u2014 warm, unhurried, and "
    "the next thing will arrive when it arrives.",
    "A slow river does not argue with the stones. It goes around them, over "
    "them, patient as light, and arrives at the sea exactly when it arrives. "
    "There is no late. There is only the water, moving, and you, moving "
    "with it.",
]


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 280, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be only whitespace"
    text.encode("utf-8")  # must be valid UTF-8
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
