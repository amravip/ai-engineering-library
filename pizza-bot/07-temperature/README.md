# Step 7: Temperature

This step explains the temperature setting, which controls how varied a model's words are. A temperature of 0 always picks the most likely word. That suits a bot that must be accurate, but it gives the same name every time when a customer asks for a new pizza name. You build the idea on the counting model first. Then you use it on the real model, to see what it can and cannot promise.

## Before you start

- Start from the step 6 folder. Copy its `examples/` and `tests/` folders, or use your own project from step 6.
- You need Ollama running with `qwen3:8b`. One script in this step does not need a model.

## Files in this step

| Status | File | What it does, and the key idea to notice |
|---|---|---|
| New | `examples/pizza_bot/sampling.py` | `apply_temperature()` and `sample()`. Key idea: a low temperature sharpens the probabilities, and a high one flattens them. |
| New | `examples/pizza_bot/temperature_toy.py` | Temperature on the counting model. Key idea: the same model gives a different mix of words at each temperature. |
| New | `examples/pizza_bot/temperature_real.py` | Temperature on the real model, with a seed. Key idea: a seed makes a random choice repeatable, but a live model may still vary. |
| Unchanged | `examples/pizza_bot/model.py` | The `chat()` function already has the `options` parameter from step 6. Key idea: the temperature is sent to Ollama in the `options` field. |
| New | `examples/expected/temperature_toy.txt` and `temperature_real.txt` | Saved outputs of the two temperature scripts. Key idea: compare the percentages and names at each temperature. |
| Changed | `tests/test_inside_the_model.py` | Adds two tests for `apply_temperature()` and `sample()`. Key idea: the tests check the maths on small, known inputs. |

Unchanged: `next_word.py`, `reviews.txt`, `tokenizer.py`, `ask.py`, `ask_with_menu.py` and `menu.txt`.

## Steps

1. Open the project folder.

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

   The script should print three names at each temperature, a total of £29 at both temperatures, and two names for the seed run. The names will differ from the saved output, and the two seed lines may or may not match.
   Saved output: `examples/expected/temperature_real.txt`. **Real run (your wording will differ).**

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

The result should be `19 passed`. The tests do not need Ollama.

## What you learned

- Temperature changes how spread out the next-word probabilities are.
- A temperature of 0 is predictable, but it always gives the same answer to the same question.
- A seed makes a random choice repeatable, but it does not make a live model fully predictable.

## Next

Go to [Step 8: Talking to Models from Code](../08-talking-to-models-from-code/README.md).
