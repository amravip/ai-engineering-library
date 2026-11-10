# Step 3: Embeddings

This step teaches the bot to find menu lines by meaning. A customer who asks for "something meat-free" should get the vegetarian pizzas. An embedding turns text into a list of numbers, so that texts with similar meanings get similar lists. The step starts with three-number vectors that you choose yourself. Then it uses a real embedding model to search Bella's menu.

## Before you start

- Start from the step 2 folder. Copy its `examples/` and `tests/` folders, or use your own project from step 2.
- You need Ollama running with `qwen3:8b`.
- You also need the embedding model `nomic-embed-text` (274 MB). Step 1 of this section downloads it.

## Files in this step

| Status | File | What it does, and the key idea to notice |
|---|---|---|
| New | `examples/pizza_bot/vectors.py` | `dot()`, `length()` and `cosine_similarity()`. Key idea: cosine similarity compares the direction of two lists of numbers, not their length, so it scores how alike two meanings are. |
| New | `examples/pizza_bot/toy_vectors.py` | Compares hand-made vectors with three numbers each. Key idea: you can see every number and check the score by hand. |
| New | `examples/pizza_bot/similar_words.py` | Finds the words closest to "veggie". Key idea: each word becomes a long list of numbers, and close lists mean close meanings. |
| New | `examples/pizza_bot/find_pizza.py` | Ranks the menu lines against a customer's phrase. Key idea: the search compares meaning, so the phrase does not need to share any words with the menu line. |
| Changed | `examples/pizza_bot/model.py` | Adds `post_to_ollama()` and `embed()`. Key idea: `embed()` asks Ollama for the list of numbers that stands for a text. |
| New | `examples/expected/toy_vectors.txt`, `similar_words.txt` and `find_pizza.txt` | Saved outputs of the three scripts above. Key idea: they show the scores you should see. |

No new test file is added in this step. The tests from steps 1 and 2 still run.

Unchanged from earlier steps: `menu.txt`, `reviews.txt`, `tokenizer.py`, `train_tokenizer.py`, `count_tokens.py`, `count_letters.py`, `ask.py` and `ask_with_menu.py`.

## Steps

1. Download the embedding model. Do this once, while you are online.

   ```bash
   ollama pull nomic-embed-text
   ```

2. Open the project folder.

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

   Each word becomes 768 numbers. "vegetarian" should come first, and "Paris" last.
   Saved output: `examples/expected/similar_words.txt`. **Real run (your wording will differ).**

5. Search the menu by meaning. This step needs Ollama and `nomic-embed-text`.

   ```bash
   python find_pizza.py
   ```

   For "I love cheese", Four Cheese should come first.
   Saved output: `examples/expected/find_pizza.txt`. **Real run (your wording will differ).**

6. Check that step 1 still works. This step needs Ollama and `qwen3:8b`.

   ```bash
   python ask_with_menu.py
   ```

   Saved output: `examples/expected/ask_with_menu.txt`. **Real run (your wording will differ).**

## Run the tests

From the step folder:

```bash
python -m pytest -q
```

The result should be `8 passed`. The tests do not need Ollama.

## What you learned

- Text can be turned into a list of numbers, and similar meanings give similar lists.
- Cosine similarity gives a score for how alike two lists are.
- A search by meaning can find "something meat-free" even when no menu line uses those words.

## Next

Go to [Step 4: Attention](../04-attention/README.md).
