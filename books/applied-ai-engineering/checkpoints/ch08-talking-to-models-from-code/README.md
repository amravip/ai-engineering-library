# Chapter 8: Talking to Models from Code

This chapter makes the model's answer usable by other code. The bot turns a customer's sentence, such as "Two large Margheritas, no olives", into an `Order` with a pizza, a size and a quantity. Then it checks the order against Bella's menu.

## Before you start

- Start from the checkpoint `ch07-temperature`. Copy its `examples/` and `tests/` folders, or use your own project from Chapter 7.
- You need Ollama running with `qwen3:8b`. The tests do not need a model.

## Files in this step

| Status | File | What it does | Listing |
|---|---|---|---|
| New | `examples/pizza_bot/orders.py` | `Order`, `ORDER_SCHEMA`, `MENU_PIZZAS`, `parse_order()` and `validate_order()`. | 8.1, 8.2, 8.3, 8.4, 8.7 |
| New | `examples/pizza_bot/take_order.py` | Runs three customer messages through `parse_order()` and `validate_order()`. | 8.6 |
| New | `examples/expected/take_order.txt` | Saved output of the script above. | Output 8.1 |
| New | `tests/test_orders.py` | Five tests of the order functions. They use a fake model. | Not printed in the chapter |

Unchanged: `model.py`. Its `chat()` function already had the `response_format` option from Chapter 6, and Listing 8.5 shows the two lines that use it. Also unchanged: `menu.txt` and the earlier scripts.

## Steps

1. From the checkpoint folder, open the project folder.

   ```bash
   cd examples/pizza_bot
   ```

2. Parse three customer messages. This step needs Ollama and `qwen3:8b`.

   ```bash
   python take_order.py
   ```

   The script prints three blocks. Each has the customer's message, a `Parsed:` line that holds an `Order` with all four fields, and a `Problems:` line. Your pizza names may differ from the book's. If a pizza name is not exactly a name on `menu.txt`, the `Problems:` line should say so.
   Saved output: `examples/expected/take_order.txt`. **Real run (your wording will differ).**

3. Check that Chapter 1 still works. This step needs Ollama and `qwen3:8b`.

   ```bash
   python ask_with_menu.py
   ```

   Saved output: `examples/expected/ask_with_menu.txt`. **Real run (your wording will differ).**

## Run the tests

From the checkpoint folder:

```bash
python -m pytest -q
```

The result should be `24 passed`. The tests use a fake model, so they pass when Ollama is stopped.

## Next

Go to [Chapter 9: The Context Window](../ch09-the-context-window/README.md), in the checkpoint `ch09-the-context-window`.
