# Step 6: Fine-tuning

This step explains why a model that only continues text does not answer questions. It adds `chat()` to `model.py`, which sends a list of messages. It shows the chat template that Ollama builds around each message. It also teaches the small model to answer, using question-and-answer pairs.

## Before you start

- Start from the step 5 folder. Copy its `examples/` and `tests/` folders, or use your own project from step 5.
- You need Ollama running with `qwen3:8b`. One script in this step does not need a model.

## Files in this step

| Status | File | What it does, and the key idea to notice |
|---|---|---|
| New | `examples/pizza_bot/qa_pairs.txt` | Question-and-answer pairs about the menu. Key idea: the small model learns the shape of an answer from these examples. |
| New | `examples/pizza_bot/fine_tune_demo.py` | The small model, with and without the question-and-answer pairs. Key idea: changing the examples a model learns from changes how it behaves. |
| New | `examples/pizza_bot/raw_vs_chat.py` | The same question sent in raw mode and through `chat()`. Key idea: raw mode continues the text, while chat mode wraps your question in a template the model was trained to answer. |
| New | `examples/pizza_bot/show_template.py` | Prints the chat template and the text the model receives. Key idea: your message is wrapped in extra markers before the model reads it. |
| Changed | `examples/pizza_bot/model.py` | Adds `chat()`, which sends a whole list of messages and returns the reply. Key idea: `chat()` takes a list of messages, each with a role, not one string. |
| New | `examples/expected/fine_tune_demo.txt`, `raw_vs_chat.txt` and `show_template.txt` | Saved outputs of the three scripts above. Key idea: they show the difference between raw and chat output. |

Unchanged: `reviews.txt`, `next_word.py`, `train_next_word.py`, `tokenizer.py`, `ask.py`, `ask_with_menu.py` and `menu.txt`.

No new test file is added in this step. The tests from step 5 still run.

## Steps

1. Open the project folder.

   ```bash
   cd examples/pizza_bot
   ```

2. Run the fine-tuning demo. This step does not need a model.

   ```bash
   python fine_tune_demo.py
   ```

   The reviews-only model should print "(nothing)". The tuned model should continue with text that begins "the margherita is".
   Saved output: `examples/expected/fine_tune_demo.txt`. **Fixed output (should match exactly).**

3. Show the chat template. This step needs Ollama and `qwen3:8b`.

   ```bash
   python show_template.py
   ```

   The output should say "first 25 of 64 lines" for `qwen3:8b`, followed by text that starts with `<|im_start|>user`. A different Ollama version may count the lines differently.
   Saved output: `examples/expected/show_template.txt`. **Real run (your wording will differ).**

4. Compare raw mode with chat mode. This step needs Ollama and `qwen3:8b`.

   ```bash
   python raw_vs_chat.py
   ```

   The first run can take about a minute while the model loads. In raw mode, the model should continue the question rather than answer it. The chat reply should read as an answer.
   Saved output: `examples/expected/raw_vs_chat.txt`. **Real run (your wording will differ).**

5. Check that step 1 still works. This step needs Ollama and `qwen3:8b`.

   ```bash
   python ask_with_menu.py
   ```

   Saved output: `examples/expected/ask_with_menu.txt`. **Real run (your wording will differ).**

## Run the tests

From the step folder:

```bash
python -m pytest -q
```

The result should be `17 passed`. The tests do not need Ollama.

## What you learned

- A model that only predicts text will continue a question instead of answering it.
- A chat template turns a list of messages into the text the model was trained to answer.
- Examples can teach a model the style of an answer.

## Next

Go to [Step 7: Temperature](../07-temperature/README.md).
