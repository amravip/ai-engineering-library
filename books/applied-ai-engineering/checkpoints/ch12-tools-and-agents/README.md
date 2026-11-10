# Chapter 12: Tools and Agents

This chapter gives the bot two tools. One looks up an order in `orders.json`, and the other counts letters. A loop lets the model call a tool, read the result and then answer the customer.

## Before you start

- Start from the checkpoint `ch11-rag`. Copy its `examples/` and `tests/` folders, or use your own project from Chapter 11.
- You need Ollama running with `qwen3:8b`. The tests do not need a model.

## Files in this step

| Status | File | What it does | Listing |
|---|---|---|---|
| New | `examples/pizza_bot/orders.json` | Bella's twenty orders, numbered #1 to #20. | Text in the chapter |
| New | `examples/pizza_bot/shop_tools.py` | `check_order()`, `count_letter()`, `TOOLS` and `run_tool()`. | 12.1, 12.2, 12.3, 12.5 |
| New | `examples/pizza_bot/agent.py` | `run_agent()`, the loop that stops after `max_steps`. | 12.4 |
| New | `examples/pizza_bot/where_is_my_order.py` | Runs three questions that need tools. | Described in the text |
| New | `examples/expected/where_is_my_order.txt` | Saved output of the script above. | Output 12.1 |
| New | `tests/test_agent.py` | Seven tests of the order file, the tools and the loop. They use a fake model. | Not printed in the chapter |

Unchanged: `model.py` (`chat()` has had a `tools` parameter since Chapter 6), `menu.txt`, and the earlier scripts.

## Steps

1. From the checkpoint folder, open the project folder.

   ```bash
   cd examples/pizza_bot
   ```

2. Run the three questions that need tools. This step needs Ollama and `qwen3:8b`.

   ```bash
   python where_is_my_order.py
   ```

   The script prints three blocks. The first should show a call to `check_order` with 7, and a reply that says the order is out for delivery. The second should report that order #99 does not exist. The third should show a call to `count_letter`, and the answer 2. Your wording may differ.
   Saved output: `examples/expected/where_is_my_order.txt`. **Real run (your wording will differ).**

## Run the tests

From the checkpoint folder:

```bash
python -m pytest -q
```

The result should be `45 passed`. The tests do not need Ollama.

## Next

Go to [Chapter 13: Shipping It](../ch13-shipping-it/README.md), in the checkpoint `ch13-shipping-it`.
