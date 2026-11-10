"""Unit tests for the toy tokenizer. No model needed."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "examples" / "pizza_bot"))

from tokenizer import (  # noqa: E402
    build_vocabulary, encode, merge_pair, split_words, tokenize, train,
)

FOLDER = Path(__file__).parents[1] / "examples" / "pizza_bot"
TEXT = (FOLDER / "menu.txt").read_text(encoding="utf-8") + (
    FOLDER / "reviews.txt").read_text(encoding="utf-8")


def test_split_words_keeps_letters_only():
    assert split_words("Margherita £9, BBQ-sauce!") == ["margherita", "bbqsauce"]


def test_merge_pair_joins_every_neighbouring_match():
    assert merge_pair(list("pepper"), ("p", "e")) == ["pe", "p", "pe", "r"]


def test_most_frequent_pair_is_merged_first():
    assert train("aa aa ab", 1) == [("a", "a")]


def test_frequent_words_become_single_pieces():
    merges = train(TEXT, 50)
    assert tokenize("pizza", merges) == ["pizza"]
    assert tokenize("pizzas", merges) == ["pizza", "s"]


def test_unseen_words_still_tokenize_into_known_pieces():
    merges = train(TEXT, 50)
    vocabulary = build_vocabulary(merges)
    assert all(piece in vocabulary for piece in tokenize("calzone", merges))
    assert len(encode("calzone spinach", merges, vocabulary)) > 2


def test_training_is_repeatable():
    assert train(TEXT, 50) == train(TEXT, 50)
