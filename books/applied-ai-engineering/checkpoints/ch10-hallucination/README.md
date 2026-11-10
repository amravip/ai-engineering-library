# Chapter 10: Hallucination

This chapter shows the bot inventing an answer about opening hours, and gives that failure a name. Then it writes a small checker. The checker compares the pizza names in an answer with Bella's menu, and flags any name that is not on it.

## Before you start

- Start from the checkpoint `ch09-the-context-window`. Copy its `examples/` and `tests/` folders, or use your own project from Chapter 9.
- You need Ollama running with `qwen3:8b`. `check_answers.py` does not need a model.

## Files in this step

| Status | File | What it does | Listing |
|---|---|---|---|
| New | `examples/pizza_bot/opening_hours.py` | Asks the opening-hours question with and without the rule about not guessing. | 10.1 |
| New | `examples/pizza_bot/grounding.py` | `menu_names()` reads the pizza names from `menu.txt`. `unsupported_pizzas()` flags names that are not on the menu. | 10.2, 10.3 |
| New | `examples/pizza_bot/check_answers.py` | Runs the checker on the two saved answers from Chapter 1. | 10.4 |
| New | `examples/expected/opening_hours.txt` and `check_answers.txt` | Saved outputs of the two scripts above. | Output 10.1 and 10.2 |
| New | `tests/test_grounding.py` | Four tests of the checker. They use no model. | Not printed in the chapter |

Unchanged: `model.py`, `menu.txt`, `ask.py`, `ask_with_menu.py`, and the saved answers `examples/expected/ask.txt` and `ask_with_menu.txt` from Chapter 1.

## Steps

1. From the checkpoint folder, open the project folder.

   ```bash
   cd examples/pizza_bot
   ```

2. Ask the opening-hours question. This step needs Ollama and `qwen3:8b`.

   ```bash
   python opening_hours.py
   ```

   The first answer should give a confident pair of opening times. Those times are invented, because the bot was never given Bella's hours. The second answer should decline. Read both answers and judge them yourself.
   Saved output: `examples/expected/opening_hours.txt`. **Real run (your wording will differ).**

3. Run the checker on the Chapter 1 answers. This step does not need a model. It reads `examples/expected/ask.txt` and `ask_with_menu.txt`.

   ```bash
   python check_answers.py
   ```

   The output should list eight names for `ask.txt`, and say "nothing flagged" for `ask_with_menu.txt`.
   Saved output: `examples/expected/check_answers.txt`. **Fixed output (should match exactly).**

4. Check that Chapter 1 still works. This step needs Ollama and `qwen3:8b`.

   ```bash
   python ask_with_menu.py
   ```

   Saved output: `examples/expected/ask_with_menu.txt`. **Real run (your wording will differ).**

## Run the tests

From the checkpoint folder:

```bash
python -m pytest -q
```

The result should be `33 passed`. The tests do not need Ollama.

## Next

Go to [Chapter 11: Retrieval-Augmented Generation](../ch11-rag/README.md), in the checkpoint `ch11-rag`.
