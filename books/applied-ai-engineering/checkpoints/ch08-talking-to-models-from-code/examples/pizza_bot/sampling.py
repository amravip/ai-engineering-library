"""Chapter 7: temperature and sampling, the two steps after the model scores each word."""

import math
import random


def apply_temperature(probabilities: dict[str, float], temperature: float) -> dict[str, float]:
    """Sharpen (low temperature) or flatten (high) the probabilities, then renormalise."""
    scaled = {word: math.exp(math.log(p) / temperature)
              for word, p in probabilities.items()}
    total = sum(scaled.values())
    return {word: value / total for word, value in scaled.items()}


def sample(probabilities: dict[str, float], rng: random.Random) -> str:
    """Pick one word at random, in proportion to its probability."""
    return rng.choices(list(probabilities), weights=list(probabilities.values()))[0]
