# Chapter 3: Embeddings

This chapter teaches the bot to find menu lines by meaning. A customer who asks for "something meat-free" should get the vegetarian pizzas. The chapter starts with three-number vectors that you choose yourself. Then it uses a real embedding model to search Bella's menu.

## Before you start

- Start from the checkpoint `ch02-tokens`. Copy its `examples/` and `tests/` folders, or use your own project from Chapter 2.
- You need Ollama running with `qwen3:8b`.
- You also need the embedding model `nomic-embed-text` (274 MB). Step 1 downloads it.

## Files in this step

| Status | File | What it does | Listing |
|---|---|---|---|
| New | `examples/pizza_bot/vectors.py` | `dot()`, `length()` and `cosine_similarity()`. | 3.1 |
| New | `examples/pizza_bot/toy_vectors.py` | Compares hand-made vectors with three numbers each. | 3.2 |
| New | `examples/pizza_bot/similar_words.py` | Finds the words closest to "veggie". | 3.4 |
| New | `examples/pizza_bot/find_pizza.py` | Ranks the menu lines against a customer's phrase. | 3.5 |
| Changed | `examples/pizza_bot/model.py` | Adds `post_to_ollama()` and `embed()`. | 3.3 |
| New | `examples/expected/toy_vectors.txt`, `similar_words.txt` and `find_pizza.txt` | Saved outputs of the three scripts above. | Output 3.1 to 3.3 |

No new test file is added in this chapter. The tests from Chapters 1 and 2 still run.

Unchanged from earlier chapters: `menu.txt`, `reviews.txt`, `tokenizer.py`, `train_tokenizer.py`, `count_tokens.py`, `count_letters.py`, `ask.py` and `ask_with_menu.py`.

## Steps

1. Download the embedding model. Do this once, while you are online.

   ```bash
   ollama pull nomic-embed-text
   ```

2. From the checkpoint folder, open the project folder.

   ```bash
   cd examples/pizza_bot
   ```

3. Compare the hand-made vectors. This step does not need a model.

   ```bash
   python toy_vectors.py
   ```

   The table should have 1.00 on the diagonal, and a score of 0.71 between "veggie" and "pepperoni".
   Saved output: `examples/expected/toy_vectors.txt`. **Fixed output (should match exactly).**

4. Find the words closest to "veggie". This step needs Ollama and `nomic-embed-text`.

   ```bash
   python similar_words.py
   ```

   Each word becomes 768 numbers. The chapter says "vegetarian" comes first and "Paris" comes last.
   Saved output: `examples/expected/similar_words.txt`. **Real run (your wording will differ).**

5. Search the menu by meaning. This step needs Ollama and `nomic-embed-text`.

   ```bash
   python find_pizza.py
   ```

   For "I love cheese", Four Cheese should come first.
   Saved output: `examples/expected/find_pizza.txt`. **Real run (your wording will differ).**

6. Check that Chapter 1 still works. This step needs Ollama and `qwen3:8b`.

   ```bash
   python ask_with_menu.py
   ```

   Saved output: `examples/expected/ask_with_menu.txt`. **Real run (your wording will differ).**

## Run the tests

From the checkpoint folder:

```bash
python -m pytest -q
```

The result should be `8 passed`. The tests do not need Ollama.

## Next

Go to [Chapter 4: Attention](../ch04-attention/README.md), in the checkpoint `ch04-attention`.
