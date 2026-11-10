# Chapter 13: Shipping It: From Demo to Product

This chapter measures how often the bot is right. It adds an eval of ten questions, each with pass or fail checks, and a script that measures the tokens and seconds of three calls. The eval points to the retrieval step as the cause of its one failure.

## Before you start

- Start from the checkpoint `ch12-tools-and-agents`. Copy its `examples/` and `tests/` folders, or use your own project from Chapter 12.
- You need Ollama running with `qwen3:8b` for the two scripts. The tests do not need a model.

## Files in this step

| Status | File | What it does | Listing |
|---|---|---|---|
| New | `examples/pizza_bot/eval_questions.json` | Ten questions, each with `must_include` and `must_not_include` checks. | 13.1 |
| New | `examples/pizza_bot/evaluate.py` | Routes each question, grades each answer and prints the score. | 13.2, 13.3 |
| New | `examples/pizza_bot/measure.py` | Prints the tokens in, the tokens out and the seconds for three calls. | 13.4 |
| New | `examples/expected/evaluate.txt` and `measure.txt` | Saved outputs of the two scripts above. | Output 13.1 and 13.2 |
| New | `tests/test_evaluate.py` | Five tests of `grade()`, the question file and the routing rule. They use no model. | Not printed in the chapter |

Unchanged: `model.py`, `menu.txt`, `shop_docs/`, `orders.json`, and every script from Chapters 1 to 12.

## Steps

1. From the checkpoint folder, open the project folder.

   ```bash
   cd examples/pizza_bot
   ```

2. Run the eval. This step needs Ollama and `qwen3:8b`.

   ```bash
   python evaluate.py
   ```

   The script prints ten lines, each marked `PASS` or `FAIL`, and ends with a score. On the book's run the score was 9/10. The one failure was "Which pizza has pineapple?". Your model may pass or fail a different question.
   Saved output: `examples/expected/evaluate.txt`. **Real run (your wording will differ).**

3. Measure the tokens and seconds. This step needs Ollama and `qwen3:8b`.

   ```bash
   python measure.py
   ```

   The script prints three lines. The long dough recipe should take far longer than the short greeting on your machine too.
   Saved output: `examples/expected/measure.txt`. **Real run (your wording will differ).**

## Run the tests

From the checkpoint folder:

```bash
python -m pytest -q
```

The result should be `50 passed`. All fifty tests of the book's project pass without Ollama.

## Next

This is the last checkpoint in the book. The chapter names the next volumes of the series: *RAG Engineering* for retrieval, *AI Agent Engineering* for agents, and *LLMOps* for running the system in production.
