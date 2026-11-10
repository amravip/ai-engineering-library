# Step 2: Tokens

This step explains why a model miscounts letters. A model does not read letters. It reads tokens, which are pieces of words. This step builds a small tokenizer that learns its pieces from Bella's menu and reviews. Then it counts the real tokens that a model sees.

## Before you start

- Start from the step 1 folder. Copy its `examples/` and `tests/` folders, or use your own project from step 1.
- You need Ollama running with `qwen3:8b`. Two scripts in this step (`text_to_numbers.py` and `train_tokenizer.py`) do not need a model. The other three need Ollama.

## Files in this step

| Status | File | What it does, and the key idea to notice |
|---|---|---|
| New | `examples/pizza_bot/reviews.txt` | Thirty short customer reviews. Key idea: the tokenizer learns its pieces from this text, so the pieces match the words customers really use. |
| New | `examples/pizza_bot/text_to_numbers.py` | Turns characters and words into numbers. Key idea: each simple way to make numbers fails in its own way, and that is why the model needs something better. |
| New | `examples/pizza_bot/tokenizer.py` | A byte-pair encoding tokenizer. Key idea: it merges the most common pair of pieces again and again, so common words become one token and rare words split into pieces. |
| New | `examples/pizza_bot/train_tokenizer.py` | Trains the tokenizer on Bella's menu and reviews. Key idea: the vocabulary is learned from data, not written by hand. |
| New | `examples/pizza_bot/count_tokens.py` | Counts the real tokens of a text with Ollama. Key idea: the real model also reads pieces, not whole words. |
| New | `examples/pizza_bot/count_letters.py` | Asks the model to count letters, then checks the answer with Python. Key idea: the model works with pieces, so its letter counts can be wrong. |
| New | `examples/expected/` (four files) | Saved outputs of the four scripts above. Key idea: they show what each script prints. |
| New | `tests/test_tokenizer.py` | Six tests of the tokenizer. Key idea: the tests use small made-up data, so the expected results are easy to check by hand. |
| Changed | `examples/pizza_bot/model.py` | Adds `count_tokens()`, which asks Ollama for the token count. Key idea: the model server can tell you how many tokens a text uses. |

Unchanged from step 1: `ask.py`, `ask_with_menu.py` and `menu.txt`.

## Steps

1. Open the project folder.

   ```bash
   cd examples/pizza_bot
   ```

2. Run the text-to-numbers script. This step does not need a model.

   ```bash
   python text_to_numbers.py
   ```

   Saved output: `examples/expected/text_to_numbers.txt`. **Fixed output (should match exactly).**

3. Train the tokenizer. This step does not need a model.

   ```bash
   python train_tokenizer.py
   ```

   The output should show a vocabulary size of 76, and "pizzas" should split into `['pizza', 's']`.
   Saved output: `examples/expected/train_tokenizer.txt`. **Fixed output (should match exactly).**

4. Count the tokens of Bella's menu. This step needs Ollama and `qwen3:8b`.

   ```bash
   python count_tokens.py
   ```

   The word "pizza" should count as 1 token.
   Saved output: `examples/expected/count_tokens.txt`. **Real run (your wording will differ).**

5. Ask the model to count letters. This step needs Ollama and `qwen3:8b`.

   ```bash
   python count_letters.py
   ```

   The model may get some counts wrong. That is the point of this step.
   Saved output: `examples/expected/count_letters.txt`. **Real run (your wording will differ).**

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

The result should be `8 passed`. That is the six tokenizer tests plus the two tests from step 1. No model is needed.

## What you learned

- A model reads tokens, which are pieces of words, not letters.
- A tokenizer can learn its pieces from data by merging common pairs.
- A model can be wrong about simple facts, such as letter counts, even when it handles a whole menu well.

## Next

Go to [Step 3: Embeddings](../03-embeddings/README.md).
