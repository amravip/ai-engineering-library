"""Tests for attention, the counting model, and sampling. No Ollama."""

import math
import random
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "examples" / "pizza_bot"))

from attention import attend, attention_weights, softmax  # noqa: E402
from next_word import (average_surprise, generate, next_word_probabilities,  # noqa: E402
                       train_next_word, vocabulary_size)
from sampling import apply_temperature, sample  # noqa: E402


def test_softmax_adds_to_one_and_keeps_order():
    weights = softmax([1.0, 2.0, 3.0])
    assert math.isclose(sum(weights), 1.0)
    assert weights[0] < weights[1] < weights[2]


def test_softmax_handles_large_scores():
    assert math.isclose(sum(softmax([1000.0, 1001.0])), 1.0)


def test_attention_looks_at_the_matching_key():
    weights = attention_weights([1, 0], [[5, 0], [0, 5]])
    assert weights[0] > 0.99


def test_attend_blends_values():
    result = attend([0, 0], [[1, 1], [1, 1]], [[2, 0], [0, 2]])
    assert result == [1.0, 1.0]


TEXT = "the pizza was hot\nthe pizza was cold\nthe pizza is good"


def test_train_counts_pairs_within_lines():
    model = train_next_word(TEXT)
    assert model["pizza"] == Counter({"was": 2, "is": 1})
    assert "the" not in model.get("hot", {})  # no pair across a line break


def test_probabilities_add_up_and_are_sorted():
    probabilities = next_word_probabilities(train_next_word(TEXT), "pizza")
    assert math.isclose(sum(probabilities.values()), 1.0)
    assert list(probabilities) == ["was", "is"]
    assert next_word_probabilities(train_next_word(TEXT), "unseen") == {}


def test_generate_is_greedy_and_stops_at_unknown_word():
    model = train_next_word(TEXT)
    assert generate(model, "the", 3) == "the pizza was hot"
    assert generate(model, "hot", 5) == "hot"


def test_training_lowers_surprise():
    model = train_next_word(TEXT)
    vocabulary = vocabulary_size(model)
    lines = ["the pizza was hot"]
    assert average_surprise(model, lines, vocabulary) < average_surprise(None, lines, vocabulary)


def test_untrained_surprise_is_log_of_vocabulary():
    assert math.isclose(average_surprise(None, ["a b"], 10), math.log(10))


def test_low_temperature_sharpens_and_high_flattens():
    base = {"a": 0.6, "b": 0.4}
    cold, hot = apply_temperature(base, 0.2), apply_temperature(base, 2.0)
    assert cold["a"] > base["a"] > hot["a"]
    assert math.isclose(sum(cold.values()), 1.0)
    assert math.isclose(apply_temperature(base, 1.0)["a"], 0.6)


def test_sample_is_repeatable_with_same_seed_and_respects_weights():
    probabilities = {"a": 0.9, "b": 0.1}
    first = [sample(probabilities, random.Random(1)) for _ in range(5)]
    assert first == [sample(probabilities, random.Random(1)) for _ in range(5)]
    assert sample({"a": 1.0, "b": 0.0}, random.Random(3)) == "a"

