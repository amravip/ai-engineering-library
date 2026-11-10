"""Attention in plain Python. A word asks, the other words answer."""

import math


def softmax(scores: list[float]) -> list[float]:
    """Turn any scores into positive weights that add up to 1."""
    biggest = max(scores)  # subtracting it keeps exp() from overflowing
    exps = [math.exp(score - biggest) for score in scores]
    total = sum(exps)
    return [value / total for value in exps]


def attention_weights(query: list[float], keys: list[list[float]]) -> list[float]:
    """How much should the query word look at each key word?"""
    scores = [sum(q * k for q, k in zip(query, key)) for key in keys]
    return softmax(scores)


def attend(query: list[float], keys: list[list[float]],
           values: list[list[float]]) -> list[float]:
    """Blend the value vectors, weighted by how well each key fits the query."""
    weights = attention_weights(query, keys)
    size = len(values[0])
    return [sum(w * value[i] for w, value in zip(weights, values))
            for i in range(size)]
