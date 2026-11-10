"""Chapter 2: two simple ways to turn text into numbers, and where each one fails."""

sentence = "Two Margheritas please"

print("1. One number per character")
print("  ", [ord(ch) for ch in sentence])
print("   numbers needed:", len(sentence))

print()
print("2. One number per word, from a list of words we know")
known_words = ["two", "margherita", "pepperoni", "please", "pizza"]
vocabulary = {word: number for number, word in enumerate(known_words)}
print("   vocabulary:", vocabulary)
for word in sentence.lower().split():
    print(f"   {word!r:15} ->", vocabulary.get(word, "UNKNOWN"))
