"""Chapter 7: temperature on the Chapter 5 counting model."""

import random
from pathlib import Path

from next_word import next_word_probabilities, train_next_word
from sampling import apply_temperature, sample

reviews = Path(__file__).with_name("reviews.txt").read_text(encoding="utf-8").splitlines()
model = train_next_word("\n".join(reviews[:25]))


def sample_sentence(start: str, length: int, temperature: float, rng: random.Random) -> str:
    """Build a sentence by sampling one word at a time."""
    words = [start]
    for _ in range(length):
        probabilities = next_word_probabilities(model, words[-1])
        if not probabilities:
            break
        words.append(sample(apply_temperature(probabilities, temperature), rng))
    return " ".join(words)


after_the = next_word_probabilities(model, "the")
for temperature in [0.2, 1.0, 2.0]:
    top = list(apply_temperature(after_the, temperature).items())[:5]
    print(f'After "the" at temperature {temperature}:',
          ", ".join(f"{w} {p:.0%}" for w, p in top))

for temperature in [0.2, 1.5]:
    rng = random.Random(7)
    print(f"\nFive sentences at temperature {temperature}:")
    for _ in range(5):
        print(" ", sample_sentence("the", 8, temperature, rng))
