# Chapter 1: Your First Conversation with a Model

By the end of this chapter, Bella's bot answers her question, "Which of your pizzas are vegetarian?", with a local model. You first see the bot invent pizzas. Then you give it the menu, so that it answers from the facts.

## Before you start

- Start from nothing. This is the first checkpoint, so there is no earlier folder to copy.
- You need Python 3.10 or newer, and Ollama on your computer. Chapter 1 explains how to install Ollama.
- You need the model `qwen3:8b`. The two scripts in this step call it. The tests do not.

## Files in this step

| Status | File | What it does | Listing |
|---|---|---|---|
| New | `examples/pizza_bot/model.py` | `ask_model()` sends one question to Ollama and returns the answer. | 1.1 |
| New | `examples/pizza_bot/ask.py` | Asks the model without the menu. | 1.2 |
| New | `examples/pizza_bot/ask_with_menu.py` | Asks the same question with the menu in the prompt. | 1.3 |
| New | `examples/pizza_bot/menu.txt` | Bella's eight pizzas, saved as UTF-8. | Text in the chapter |
| New | `examples/expected/ask.txt` and `ask_with_menu.txt` | Saved answers from the two scripts. | Output 1.1 and 1.2 |
| New | `tests/test_model.py` | Two tests for `ask_model()` and the menu. They use a fake model. | Not printed in the chapter |

Changed files: none.

## Steps

1. Download the model. Ollama must be running.

   ```bash
   ollama pull qwen3:8b
   ```

   The download is about 5.2 GB, so do it while you are online.

2. From the checkpoint folder, open the project folder.

   ```bash
   cd examples/pizza_bot
   ```

3. Ask the model without the menu. This step needs Ollama.

   ```bash
   python ask.py
   ```

   The answer may name pizzas that are not on the menu. That is the point of this first run.
   Saved output: `examples/expected/ask.txt`. **Real run (your wording will differ).**

4. Ask the same question with the menu. This step needs Ollama.

   ```bash
   python ask_with_menu.py
   ```

   The answer should list Margherita, Garden Veggie, Four Cheese and Mushroom, and no other pizza.
   Saved output: `examples/expected/ask_with_menu.txt`. **Real run (your wording will differ).**

## Run the tests

From the checkpoint folder, not from `examples/pizza_bot`:

```bash
python -m pytest -q
```

The result should be `2 passed`. The tests use a fake model, so Ollama does not need to run.

## Next

Go to [Chapter 2: Tokens](../ch02-tokens/README.md), in the checkpoint `ch02-tokens`.
