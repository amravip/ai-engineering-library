# Step 10: Hallucination

A customer asks what time the shop opens on Sunday. The bot answers at once, with two opening times, and sounds sure of itself. Nobody gave the bot Bella's opening hours, so the times are invented. This is called a hallucination. This step reproduces it, then writes a small checker. The checker compares the pizza names in an answer with Bella's menu, and flags any name that is not on it.

## Before you start

- Start from the step 9 folder. Copy its `examples/` and `tests/` folders, or use your own project from step 9.
- You need Ollama running with `qwen3:8b`. `check_answers.py` does not need a model.

## Files in this step

| Status | File | What it does, and the key idea to notice |
|---|---|---|
| New | `examples/pizza_bot/opening_hours.py` | Asks the opening-hours question with and without a rule about not guessing. Key idea: a model can sound sure even when it was never given the facts. |
| New | `examples/pizza_bot/grounding.py` | `menu_names()` reads the pizza names from `menu.txt`. `unsupported_pizzas()` flags names that are not on the menu. Key idea: a check against a trusted list catches some invented facts, but not all of them. |
| New | `examples/pizza_bot/check_answers.py` | Runs the checker on the two saved answers from step 1. Key idea: the same checker gives different results on the two answers. |
| New | `examples/expected/opening_hours.txt` and `check_answers.txt` | Saved outputs of the two scripts above. Key idea: compare the confident answer with the one that declines. |
| New | `tests/test_grounding.py` | Four tests of the checker. Key idea: a made-up pizza name must be flagged, and a real one must not be. |

Unchanged: `model.py`, `menu.txt`, `ask.py`, `ask_with_menu.py`, and the saved answers `examples/expected/ask.txt` and `ask_with_menu.txt` from step 1.

## Steps

1. Open the project folder.

   ```bash
   cd examples/pizza_bot
   ```

2. Ask the opening-hours question. This step needs Ollama and `qwen3:8b`.

   ```bash
   python opening_hours.py
   ```

   The first answer should give a confident pair of opening times. Those times are invented, because the bot was never given Bella's hours. The second answer should decline. Read both answers and judge them yourself.
   Saved output: `examples/expected/opening_hours.txt`. **Real run (your wording will differ).**

3. Run the checker on the step 1 answers. This step does not need a model. It reads `examples/expected/ask.txt` and `ask_with_menu.txt`.

   ```bash
   python check_answers.py
   ```

   The output should list eight names for `ask.txt`, and say "nothing flagged" for `ask_with_menu.txt`.
   Saved output: `examples/expected/check_answers.txt`. **Fixed output (should match exactly).**

4. Check that step 1 still works. This step needs Ollama and `qwen3:8b`.

   ```bash
   python ask_with_menu.py
   ```

   Saved output: `examples/expected/ask_with_menu.txt`. **Real run (your wording will differ).**

## Run the tests

From the step folder:

```bash
python -m pytest -q
```

The result should be `33 passed`. The tests do not need Ollama.

## What you learned

- A model can produce a confident answer that is simply wrong.
- A checker can compare an answer with a list you trust.
- A checker only catches what it knows how to look for, so it does not prove an answer is true.

## Next

Go to [Step 11: Retrieval-Augmented Generation](../11-rag/README.md).
