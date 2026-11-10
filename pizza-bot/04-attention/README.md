# Step 4: Attention

This step shows how each word can look at the words around it. The word "hot" can mean spicy in one customer's message and warm in another's. The meaning depends on the neighbouring words. You build attention in plain Python, and then you ask the real model the same question.

## Before you start

- Start from the step 3 folder. Copy its `examples/` and `tests/` folders, or use your own project from step 3.
- You need Ollama running with `qwen3:8b`. `nomic-embed-text` is still installed from step 3, but the scripts in this step do not use it.

## Files in this step

| Status | File | What it does, and the key idea to notice |
|---|---|---|
| New | `examples/pizza_bot/attention.py` | `softmax()`, `attention_weights()` and `attend()`. Key idea: attention turns scores into weights that add up to one, then blends the words' values using those weights. |
| New | `examples/pizza_bot/attention_demo.py` | Shows "hot" in two sentences, using hand-made vectors. Key idea: the same word gets a different blend when its neighbours change. |
| New | `examples/pizza_bot/hot_question.py` | Asks the real model what "hot" means in each message. Key idea: the real model does the same kind of job, with far more numbers. |
| New | `examples/expected/attention_demo.txt` and `hot_question.txt` | Saved outputs of the two scripts above. Key idea: they show the weights and the answers you should expect. |
| New | `tests/test_inside_the_model.py` | Four tests for `softmax()` and attention. Key idea: softmax weights always add up to 1, and the tests check that. |

Unchanged: `model.py`, `tokenizer.py`, `toy_vectors.py`, `vectors.py`, `similar_words.py`, `find_pizza.py`, `ask.py`, `ask_with_menu.py`, `menu.txt` and `reviews.txt`.

## Steps

1. Open the project folder.

   ```bash
   cd examples/pizza_bot
   ```

2. Run the attention demo. This step does not need a model.

   ```bash
   python attention_demo.py
   ```

   The output should give "chilli" a weight of 0.73 in the first sentence. It should give "an hour" and "late" weights of 0.41 and 0.25 in the second.
   Saved output: `examples/expected/attention_demo.txt`. **Fixed output (should match exactly).**

3. Ask the real model about "hot". This step needs Ollama and `qwen3:8b`.

   ```bash
   python hot_question.py
   ```

   The model should read "hot" as spicy in the first message and as temperature in the second. The wording will differ.
   Saved output: `examples/expected/hot_question.txt`. **Real run (your wording will differ).**

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

The result should be `12 passed`. The tests do not need Ollama.

## What you learned

- Attention lets each word take information from the words around it.
- Softmax turns raw scores into weights that add up to one.
- The same word can carry different meanings, depending on its context.

## Next

Go to [Step 5: Training](../05-training/README.md).
