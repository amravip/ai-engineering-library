# Chapter 8 checkpoint: talking to models from code

This folder is the Bella's Pizza project at the end of Chapter 8. It holds every script, data file, saved output and test that a reader has after Chapters 1 to 8. You can use it to start Chapter 9 or to compare your own files with a reference.

## What exists

The project is one flat folder, `examples/pizza_bot/`. Each chapter added files to it, and Chapter 8 adds two:

- **`orders.py`** (new). An `Order` with four fields (pizza, size, quantity and notes). `ORDER_SCHEMA` describes that shape for the model. `MENU_PIZZAS` reads the pizza names from `menu.txt`. `parse_order()` sends a customer's message to the model and returns an `Order`. `validate_order()` checks the result against the menu and against the quantity limit.
- **`take_order.py`** (new). Runs three customer messages through `parse_order()` and `validate_order()`, then prints each parsed order and its problems.

Nothing else changed in this chapter. `model.py` already had `chat()` and its `response_format` option from earlier chapters, so it is the same file you had at the end of Chapter 7.

## Files

| Status | Files |
|---|---|
| New in Chapter 8 | `orders.py`, `take_order.py` |
| Changed in Chapter 8 | None |
| Unchanged from earlier chapters | Everything else in `examples/pizza_bot/`, the data files `menu.txt`, `reviews.txt` and `qa_pairs.txt`, and the saved outputs in `examples/expected/` |

Chapter 1 files: `model.py`, `ask.py`, `ask_with_menu.py`, `menu.txt`.
Chapter 2 files: `text_to_numbers.py`, `tokenizer.py`, `train_tokenizer.py`, `count_tokens.py`, `count_letters.py`, `reviews.txt`.
Chapter 3 files: `vectors.py`, `toy_vectors.py`, `similar_words.py`, `find_pizza.py`.
Chapter 4 files: `attention.py`, `attention_demo.py`, `hot_question.py`.
Chapter 5 files: `next_word.py`, `train_next_word.py`.
Chapter 6 files: `qa_pairs.txt`, `fine_tune_demo.py`, `show_template.py`, `raw_vs_chat.py`.
Chapter 7 files: `sampling.py`, `temperature_toy.py`, `temperature_real.py`.

The `tests/` folder has four files: `test_model.py`, `test_tokenizer.py`, `test_inside_the_model.py` (Chapters 4, 5 and 7) and `test_orders.py`.

## Commands

Run the scripts from inside `examples/pizza_bot/`. Run the tests from this checkpoint folder.

```bash
cd examples/pizza_bot
python take_order.py           # needs Ollama running and qwen3:8b (or OLLAMA_MODEL) available
python ask_with_menu.py        # Chapter 1 still works; needs Ollama

cd ../..
python -m pytest -q            # 24 tests; no model needed
python -m pytest -q tests/test_orders.py   # only the Chapter 8 tests
```

Configuration comes from the environment variables described in the book folder's README: `OLLAMA_BASE_URL`, `OLLAMA_MODEL` and `OLLAMA_EMBED_MODEL`.

## Expected results

**`take_order.py` is a real run.** The saved output in `examples/expected/take_order.txt` came from `qwen3:8b` on Ollama 0.40.13, on a laptop with 16 GB of memory, on 6 November 2026. Your wording will differ, and the model may get a pizza name right that the saved run got wrong. The shape of the output should be the same:

- Three blocks. Each has the customer's message, a `Parsed:` line holding an `Order` with all four fields, and a `Problems:` line.
- Whenever the pizza name is not exactly a name on `menu.txt`, the `Problems:` line says so.

**The pytest run needs no model.** All 24 tests use a fake model, so they pass with Ollama stopped.

**Scripts without a model print fixed output.** `text_to_numbers.py`, `train_tokenizer.py`, `toy_vectors.py`, `attention_demo.py`, `train_next_word.py`, `fine_tune_demo.py` and `temperature_toy.py` print exactly the text in `examples/expected/` on every run.

## Checking earlier chapters still work

The quickest check is the test run above. To check the scripts, run the fixed-output scripts from `examples/pizza_bot/` and compare each result with the saved file:

```bash
PYTHONIOENCODING=utf-8 python text_to_numbers.py > text_to_numbers.out.txt
diff text_to_numbers.out.txt ../expected/text_to_numbers.txt
```

Delete the `.out.txt` file afterwards. No output from `diff` means the two files match.

## Common problems

- **A "not found" error about the model.** Run `ollama pull qwen3:8b`, or set `OLLAMA_MODEL` to a model you have. Run `ollama list` to see the models on your computer.
- **Connection refused.** Ollama is not running. Start it, or set `OLLAMA_BASE_URL` to the address where it is listening.
- **A pizza name with a plural or a typo appears under `Problems:`.** That is the check working. The model can copy a customer's wording into the pizza field, and `validate_order()` is what catches it. The schema guarantees the shape of the answer, not its content.
- **Tests fail with an import error.** Run `python -m pytest` from this checkpoint folder, not from `examples/pizza_bot/`.
