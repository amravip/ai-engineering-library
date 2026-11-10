# Chapter 7: Temperature

This chapter explains the temperature setting, which controls how varied a model's words are. You build the idea on the counting model first. Then you use it on the real model, to see what it can and cannot promise.

## Before you start

- Start from the checkpoint `ch06-fine-tuning`. Copy its `examples/` and `tests/` folders, or use your own project from Chapter 6.
- You need Ollama running with `qwen3:8b`. One script in this step does not need a model.

## Files in this step

| Status | File | What it does | Listing |
|---|---|---|---|
| New | `examples/pizza_bot/sampling.py` | `apply_temperature()` and `sample()`. | 7.1, 7.2 |
| New | `examples/pizza_bot/temperature_toy.py` | Temperature on the counting model. | 7.3, 7.4 |
| New | `examples/pizza_bot/temperature_real.py` | Temperature on the real model, with a seed. | 7.5 |
| Unchanged | `examples/pizza_bot/model.py` | The `chat()` function already has the `options` parameter from Chapter 6. Listing 7.6 shows the line that uses it. | 7.6 |
| New | `examples/expected/temperature_toy.txt` and `temperature_real.txt` | Saved outputs of the two temperature scripts. | Output 7.1 to 7.3 |
| Changed | `tests/test_inside_the_model.py` | Adds two tests for `apply_temperature()` and `sample()`. | Not printed in the chapter |

Unchanged: `next_word.py`, `reviews.txt`, `tokenizer.py`, `ask.py`, `ask_with_menu.py` and `menu.txt`.

## Steps

1. From the checkpoint folder, open the project folder.

   ```bash
   cd examples/pizza_bot
   ```

2. Run the temperature demo on the counting model. This step does not need a model.

   ```bash
   python temperature_toy.py
   ```

   The first line should be `After "the" at temperature 0.2: margherita 38%, pizza 38%, pepperoni 9%, mushroom 9%, four 1%`. The output is the same on every run.
   Saved output: `examples/expected/temperature_toy.txt`. **Fixed output (should match exactly).**

3. Run the temperature demo on the real model. This step needs Ollama and `qwen3:8b`.

   ```bash
   python temperature_real.py
   ```

   The script should print three names at each temperature, a total of £29 at both temperatures, and two names for the seed run. The names will differ from the book's, and the two seed lines may or may not match.
   Saved output: `examples/expected/temperature_real.txt`. **Real run (your wording will differ).**

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

The result should be `19 passed`. The tests do not need Ollama.

## Next

Go to [Chapter 8: Talking to Models from Code](../ch08-talking-to-models-from-code/README.md), in the checkpoint `ch08-talking-to-models-from-code`.
