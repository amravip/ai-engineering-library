"""Train the counting model on 25 reviews and see what it learned."""

from pathlib import Path

from next_word import (average_surprise, generate, next_word_probabilities,
                       train_next_word, vocabulary_size)

reviews = Path(__file__).with_name("reviews.txt").read_text(encoding="utf-8").splitlines()
training, held_out = reviews[:25], reviews[25:]

model = train_next_word("\n".join(training))
print("Words the model knows:", vocabulary_size(model))

for word in ["the", "pizza", "was"]:
    top = list(next_word_probabilities(model, word).items())[:4]
    print(f'After "{word}":', ", ".join(f"{w} {p:.0%}" for w, p in top))

print()
print("Greedy text:", generate(model, "the", 12))

vocabulary = vocabulary_size(train_next_word("\n".join(reviews)))
print()
print("Average surprise on the 5 held-out reviews:")
print(f"  before training: {average_surprise(None, held_out, vocabulary):.2f}")
print(f"  after training:  {average_surprise(model, held_out, vocabulary):.2f}")
