"""Chapter 4: the word "hot" leans spicy or warm, depending on its neighbours."""

from attention import attend, attention_weights

# Dimensions: [spicy, temperature, delivery]
# Every word uses the same vector as its key and its value, to keep it small.
HOT = [1.0, 1.0, 0.0]  # on its own, "hot" is ambiguous
sentences = {
    "Is the BBQ chicken hot ? it has chilli": {
        "Is": [0.0, 0.0, 0.0], "the": [0.0, 0.0, 0.0],
        "BBQ": [0.3, 0.0, 0.0], "chicken": [0.2, 0.0, 0.0],
        "?": [0.0, 0.0, 0.0], "it": [0.0, 0.0, 0.0],
        "has": [0.0, 0.0, 0.0], "chilli": [3.0, 0.0, 0.0],
    },
    "Is the pizza hot ? it was an hour late": {
        "Is": [0.0, 0.0, 0.0], "the": [0.0, 0.0, 0.0],
        "pizza": [0.0, 0.1, 0.0], "?": [0.0, 0.0, 0.0],
        "it": [0.0, 0.0, 0.0], "was": [0.0, 0.0, 0.0],
        "an hour": [0.0, 2.0, 1.0], "late": [0.0, 1.5, 2.0],
    },
}

for sentence, vectors in sentences.items():
    words = list(vectors)
    keys = list(vectors.values())
    print(sentence)
    for word, weight in zip(words, attention_weights(HOT, keys)):
        print(f"  hot looks at {word:8} {weight:.2f}")
    blend = attend(HOT, keys, keys)
    print("  blended [spicy, temperature, delivery]:",
          [round(x, 2) for x in blend])
    print()
