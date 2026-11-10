"""Chapter 3: hand-made word vectors, to see what "similar" means in numbers."""

from vectors import cosine_similarity

# Each word is described by three numbers:
# [is_food, is_vegetarian, is_about_delivery]
words = {
    "veggie":     [0.9, 0.9, 0.0],
    "vegetarian": [0.9, 1.0, 0.0],
    "margherita": [1.0, 0.8, 0.0],
    "pepperoni":  [1.0, 0.0, 0.0],
    "delivery":   [0.1, 0.0, 1.0],
    "driver":     [0.0, 0.0, 0.9],
}

names = list(words)
print(" " * 12 + "".join(f"{name[:10]:>11}" for name in names))
for first in names:
    row = [cosine_similarity(words[first], words[second]) for second in names]
    print(f"{first:12}" + "".join(f"{score:11.2f}" for score in row))
