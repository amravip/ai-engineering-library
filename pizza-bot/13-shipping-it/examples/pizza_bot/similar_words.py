"""Real embeddings. Which words sit closest to "veggie"?"""

from model import embed
from vectors import cosine_similarity

candidates = ["vegetarian", "meat-free", "plant-based", "pepperoni",
              "delivery", "invoice", "Paris", "mushroom"]

vectors = embed(["veggie"] + candidates)
veggie, others = vectors[0], vectors[1:]
print("Numbers per word:", len(veggie))

scored = [(cosine_similarity(veggie, vector), word)
          for word, vector in zip(candidates, others)]
for score, word in sorted(scored, reverse=True):
    print(f"{score:.2f}  {word}")
