# Chapter 2: Tokens

This chapter explains why a model miscounts letters. It builds a small tokenizer that learns word pieces from Bella's menu and reviews. Then it counts the real tokens that a model sees.

## Before you start

- Start from the checkpoint `ch01-first-conversation`. Copy its `examples/` and `tests/` folders, or use your own project from Chapter 1.
- You need Ollama running with `qwen3:8b`. Two scripts in this step (`text_to_numbers.py` and `train_tokenizer.py`) do not need a model. The other three need Ollama.

## Files in this step

| Status | File | What it does | Listing |
|---|---|---|---|
| New | `examples/pizza_bot/reviews.txt` | Thirty short customer reviews. They are the training text for the tokenizer. | Text in the chapter |
| New | `examples/pizza_bot/text_to_numbers.py` | Turns characters and words into numbers. | 2.1 |
| New | `examples/pizza_bot/tokenizer.py` | A byte-pair encoding tokenizer. | 2.2, 2.3, 2.4 |
| New | `examples/pizza_bot/train_tokenizer.py` | Trains the tokenizer on Bella's menu and reviews. | 2.5 |
| New | `examples/pizza_bot/count_tokens.py` | Counts the real tokens of a text with Ollama. | 2.7 |
| New | `examples/pizza_bot/count_letters.py` | Asks the model to count letters, so you can see its mistakes. | 2.8 |
| New | `examples/expected/` (four files) | Saved outputs of the four scripts above. | Output 2.1 to 2.4 |
| New | `tests/test_tokenizer.py` | Six tests of the tokenizer. They use small fake data and no model. | Not printed in the chapter |
| Changed | `examples/pizza_bot/model.py` | Adds `count_tokens()`, which asks Ollama for the token count. | 2.6 |

Unchanged from Chapter 1: `ask.py`, `ask_with_menu.py` and `menu.txt`.

## Steps

1. From the checkpoint folder, open the project folder.

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

   The model may get some counts wrong. The chapter explains why.
   Saved output: `examples/expected/count_letters.txt`. **Real run (your wording will differ).**

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

The result should be `8 passed`. That is the six tokenizer tests plus the two tests from Chapter 1. No model is needed.

## Next

Go to [Chapter 3: Embeddings](../ch03-embeddings/README.md), in the checkpoint `ch03-embeddings`.
