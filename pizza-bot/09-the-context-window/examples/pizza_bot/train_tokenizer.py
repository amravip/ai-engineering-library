"""Learn word pieces from Bella's menu and reviews, then use them."""

from pathlib import Path

from tokenizer import build_vocabulary, encode, split_words, tokenize, train

folder = Path(__file__).parent
text = (folder / "menu.txt").read_text(encoding="utf-8")
text += (folder / "reviews.txt").read_text(encoding="utf-8")
print("Training text:", len(split_words(text)), "words")

merges = train(text, number_of_merges=50)
print("First ten merges:", merges[:10])

print()
for word in ["pizza", "margherita", "mushroom", "pizzas", "mushrooms",
             "margheritas", "spinach", "calzone"]:
    print(f"{word:12} -> {tokenize(word, merges)}")

vocabulary = build_vocabulary(merges)
print()
print("Vocabulary size:", len(vocabulary))
sentence = "Two Margherita pizzas please"
print(sentence, "->", encode(sentence, merges, vocabulary))
