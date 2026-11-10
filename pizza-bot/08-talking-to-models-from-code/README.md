# Step 8: Talking to Models from Code

A customer types, "Two large Margheritas, no olives". A program needs a pizza, a size and a quantity, not a friendly paragraph. This step asks the model for structured data that other code can use. Then it checks that data against Bella's menu, because a model's answer is something to check, not a fact to trust.

## Before you start

- Start from the step 7 folder. Copy its `examples/` and `tests/` folders, or use your own project from step 7.
- You need Ollama running with `qwen3:8b`. The tests do not need a model.

## Files in this step

| Status | File | What it does, and the key idea to notice |
|---|---|---|
| New | `examples/pizza_bot/orders.py` | `Order`, `ORDER_SCHEMA`, `MENU_PIZZAS`, `parse_order()` and `validate_order()`. Key idea: the schema tells the model the exact fields to return, and `validate_order()` still checks the answer. |
| New | `examples/pizza_bot/take_order.py` | Runs three customer messages through `parse_order()` and `validate_order()`. Key idea: the model's reply is data to check before the shop uses it. |
| New | `examples/expected/take_order.txt` | Saved output of the script above. Key idea: a name that is not on the menu is reported, not accepted. |
| New | `tests/test_orders.py` | Five tests of the order functions. Key idea: the tests use a fake model reply, so the schema and the checks run without Ollama. |

Unchanged: `model.py`. Its `chat()` function already has the `response_format` option, from step 6. This step uses that option to send the schema to the model. Also unchanged: `menu.txt` and the earlier scripts.

## Steps

1. Open the project folder.

   ```bash
   cd examples/pizza_bot
   ```

2. Parse three customer messages. This step needs Ollama and `qwen3:8b`.

   ```bash
   python take_order.py
   ```

   The script prints three blocks. Each has the customer's message, a `Parsed:` line that holds an `Order` with all four fields, and a `Problems:` line. Your pizza names may differ from the saved output. If a pizza name is not exactly a name on `menu.txt`, the `Problems:` line should say so.
   Saved output: `examples/expected/take_order.txt`. **Real run (your wording will differ).**

3. Check that step 1 still works. This step needs Ollama and `qwen3:8b`.

   ```bash
   python ask_with_menu.py
   ```

   Saved output: `examples/expected/ask_with_menu.txt`. **Real run (your wording will differ).**

## Run the tests

From the step folder:

```bash
python -m pytest -q
```

The result should be `24 passed`. The tests use a fake model, so they pass when Ollama is stopped.

## What you learned

- A model can return data in a fixed shape, which a program can read.
- A valid answer is not always a correct one, so check the data against your own rules.
- Keep the model's reply separate from the checks that decide what the shop accepts.

## Next

Go to [Step 9: The Context Window](../09-the-context-window/README.md).
