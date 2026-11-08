"""A tiny tokenizer that learns word pieces from text (byte-pair encoding)."""

from collections import Counter


def split_words(text: str) -> list[str]:
    """Lower-case the text and keep only words made of letters."""
    words = []
    for raw in text.lower().split():
        word = "".join(ch for ch in raw if ch.isalpha())
        if word:
            words.append(word)
    return words


def merge_pair(pieces: list[str], pair: tuple[str, str]) -> list[str]:
    """Join every place where the two pieces of `pair` sit side by side."""
    merged = []
    i = 0
    while i < len(pieces):
        if i + 1 < len(pieces) and (pieces[i], pieces[i + 1]) == pair:
            merged.append(pieces[i] + pieces[i + 1])
            i += 2
        else:
            merged.append(pieces[i])
            i += 1
    return merged


def train(text: str, number_of_merges: int) -> list[tuple[str, str]]:
    """Learn which neighbouring pieces to join, most frequent pair first."""
    words = Counter(split_words(text))
    pieces = {word: list(word) for word in words}
    merges = []
    for _ in range(number_of_merges):
        pairs = Counter()
        for word, count in words.items():
            parts = pieces[word]
            for left, right in zip(parts, parts[1:]):
                pairs[(left, right)] += count
        if not pairs:
            break
        best = max(pairs, key=lambda pair: (pairs[pair], pair))
        merges.append(best)
        for word in pieces:
            pieces[word] = merge_pair(pieces[word], best)
    return merges


def tokenize(word: str, merges: list[tuple[str, str]]) -> list[str]:
    """Split one word into pieces by replaying the learned merges in order."""
    pieces = list(word.lower())
    for pair in merges:
        pieces = merge_pair(pieces, pair)
    return pieces


def build_vocabulary(merges: list[tuple[str, str]]) -> dict[str, int]:
    """Give every piece a number: the 26 letters first, then each merged piece."""
    pieces = list("abcdefghijklmnopqrstuvwxyz")
    pieces += [left + right for left, right in merges]
    return {piece: number for number, piece in enumerate(pieces)}


def encode(text: str, merges: list[tuple[str, str]], vocabulary: dict[str, int]) -> list[int]:
    """Turn text into the list of numbers a model would actually receive."""
    numbers = []
    for word in split_words(text):
        for piece in tokenize(word, merges):
            numbers.append(vocabulary[piece])
    return numbers
