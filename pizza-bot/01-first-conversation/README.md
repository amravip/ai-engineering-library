# Step 1: Your First Conversation with a Model

This step builds the first version of a pizza shop assistant. A customer asks, "What vegetarian pizzas do you have?" You send that question to a model that runs on your own computer, through Ollama. First you ask without the menu, to see the model invent answers. Then you paste the menu into the prompt, and the answer follows the menu.

## Before you start

- This is the first step, so there is no earlier folder to copy.
- You need Python 3.10 or newer, and Ollama running on your computer. Install Ollama from [ollama.com](https://ollama.com).
- You need the model `qwen3:8b`. The two scripts in this step call it. The tests do not need it.

## Files in this step

| Status | File | What it does, and the key idea to notice |
|---|---|---|
| New | `examples/pizza_bot/model.py` | `ask_model()` sends one question to Ollama and returns the answer. Key idea: the program sends a plain web request to a server on your own computer. |
| New | `examples/pizza_bot/ask.py` | Asks the model without the menu. Key idea: the model knows only what is in the prompt. |
| New | `examples/pizza_bot/ask_with_menu.py` | Asks the same question with the menu in the prompt. Key idea: giving the model the facts changes the answer. |
| New | `examples/pizza_bot/menu.txt` | Bella's eight pizzas, saved as UTF-8. Key idea: the menu is plain text that any program can read. |
| New | `examples/expected/ask.txt` and `ask_with_menu.txt` | Saved answers from the two scripts. Key idea: compare your answers with these to see what a real run looks like. |
| New | `tests/test_model.py` | Two tests for `ask_model()` and the menu. Key idea: a fake model replaces the network call, so the tests run without Ollama. |

Changed files: none.

## Steps

1. Download the model. Ollama must be running.

   ```bash
   ollama pull qwen3:8b
   ```

   The download is about 5.2 GB, so do it while you are online. If your computer has 8 GB of memory, use `qwen3:1.7b` instead. The [root README](../../README.md) explains how to set that.

2. Open the project folder.

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

From the step folder, not from `examples/pizza_bot`:

```bash
python -m pytest -q
```

The result should be `2 passed`. The tests use a fake model, so Ollama does not need to run.

## What you learned

- A few lines of Python can send a question to a local model and read the answer.
- A model answers from the text in its prompt. If the facts are missing, it may invent them.
- A fake model lets you test your code without running a real model.

## Next

Go to [Step 2: Tokens](../02-tokens/README.md).
