# Step 12: Tools and Agents

Documents cannot answer every question. Order status changes all evening, so a customer who asks "Where is my order #7?" needs the order system, not a file. This step gives the bot two tools: one looks up an order, and one counts letters. A loop lets the model ask for a tool, read the result and then answer the customer.

## Before you start

- Start from the step 11 folder. Copy its `examples/` and `tests/` folders, or use your own project from step 11.
- You need Ollama running with `qwen3:8b`. The tests do not need a model.

## Files in this step

| Status | File | What it does, and the key idea to notice |
|---|---|---|
| New | `examples/pizza_bot/orders.json` | Bella's twenty orders, numbered #1 to #20. Key idea: this file stands in for the shop's order system, which a real bot would call. |
| New | `examples/pizza_bot/shop_tools.py` | `check_order()`, `count_letter()`, `TOOLS` and `run_tool()`. Key idea: each tool is an ordinary Python function, plus a description that the model can read. |
| New | `examples/pizza_bot/agent.py` | `run_agent()`, the loop that stops after `max_steps`. Key idea: the loop has a limit, so a model that keeps asking for tools cannot run forever. |
| New | `examples/pizza_bot/where_is_my_order.py` | Runs three questions that need tools. Key idea: the model decides when to ask for a tool, and the program runs it. |
| New | `examples/expected/where_is_my_order.txt` | Saved output of the script above. Key idea: look for the tool calls between the customer's question and the answer. |
| New | `tests/test_agent.py` | Seven tests of the order file, the tools and the loop. Key idea: a fake model can ask for a tool, so the loop can be tested without a live model. |

Unchanged: `model.py` (`chat()` has had a `tools` parameter since step 6), `menu.txt`, and the earlier scripts.

## Steps

1. Open the project folder.

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

From the step folder:

```bash
python -m pytest -q
```

The result should be `45 passed`. The tests do not need Ollama.

## What you learned

- A tool is a normal function that the model can ask the program to run.
- An agent is a loop: ask the model, run any tool it requests, then ask again.
- Put a limit on the loop, so a confused model cannot run forever.

## Next

Go to [Step 13: Shipping It](../13-shipping-it/README.md).
