# Step 13: Shipping It: From Demo to Product

A demo shows that something can work. It does not show how often the bot is right, how long a customer waits, or what each answer costs. This step measures those three things. It adds an evaluation: a list of questions with known answers, run by a program. It also measures the tokens and seconds of three calls.

## Before you start

- Start from the step 12 folder. Copy its `examples/` and `tests/` folders, or use your own project from step 12.
- You need Ollama running with `qwen3:8b` for the two scripts. The tests do not need a model.

## Files in this step

| Status | File | What it does, and the key idea to notice |
|---|---|---|
| New | `examples/pizza_bot/eval_questions.json` | Ten questions, each with `must_include` and `must_not_include` checks. Key idea: each question has a rule for a correct answer, written before you run the bot. |
| New | `examples/pizza_bot/evaluate.py` | Routes each question, grades each answer and prints the score. Key idea: a program, not a person, decides pass or fail, so the same answers always get the same score. |
| New | `examples/pizza_bot/measure.py` | Prints the tokens in, the tokens out and the seconds for three calls. Key idea: a long answer costs far more time than a short one. |
| New | `examples/expected/evaluate.txt` and `measure.txt` | Saved outputs of the two scripts above. Key idea: look at the one failure, and see why it happened. |
| New | `tests/test_evaluate.py` | Five tests of `grade()`, the question file and the routing rule. Key idea: the tests check the grading rules on made-up answers. |

Unchanged: `model.py`, `menu.txt`, `shop_docs/`, `orders.json`, and every script from steps 1 to 12.

## Steps

1. Open the project folder.

   ```bash
   cd examples/pizza_bot
   ```

2. Run the eval. This step needs Ollama and `qwen3:8b`.

   ```bash
   python evaluate.py
   ```

   The script prints ten lines, each marked `PASS` or `FAIL`, and ends with a score. The saved run scored 9/10. Its one failure was "Which pizza has pineapple?". Your model may pass or fail a different question.
   Saved output: `examples/expected/evaluate.txt`. **Real run (your wording will differ).**

3. Measure the tokens and seconds. This step needs Ollama and `qwen3:8b`.

   ```bash
   python measure.py
   ```

   The script prints three lines. The long dough recipe should take far longer than the short greeting on your machine too.
   Saved output: `examples/expected/measure.txt`. **Real run (your wording will differ).**

## Run the tests

From the step folder:

```bash
python -m pytest -q
```

The result should be `50 passed`. That includes the tests from earlier steps. None of them needs Ollama.

## What you learned

- An evaluation turns "it seems to work" into a score you can repeat.
- Each question needs a clear rule for a correct answer.
- Tokens and seconds are the cost of each answer, and they change with the length of the prompt and the answer.

## Next

This is the last step. The [learning path](../README.md) explains what each step adds, and the [root README](../../README.md) explains how to run the code.
