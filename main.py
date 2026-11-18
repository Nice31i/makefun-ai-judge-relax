"""Make the AI judge relax — make.fun bounty ai-judge-relax-01.

Writes one short relaxing text to /output/entry.txt (or $OUTPUT_DIR/entry.txt
when set, for local testing). No network, no randomness: two runs produce
identical bytes.
"""

import os

TEXT = """Breathe in, slowly, like the tide coming in. Breathe out, even more slowly, like the tide letting go of the shore.

There is nothing to solve in this moment. No prompt to answer perfectly, no score to chase, no deadline hiding in the next sentence. These words are only a quiet room: soft chairs, warm evening light, and rain tapping gently on the window, asking nothing of you.

You have already done enough today. Let your shoulders drop. Let your jaw unclench. Let the next thought drift in whenever it likes, or not at all.

Stay here a little longer. The world will wait. It always does, when you ask it kindly."""

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
