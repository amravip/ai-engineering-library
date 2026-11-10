# Step 11: Retrieval-Augmented Generation

The bot needs the facts in front of it, but pasting every fact into the prompt does not scale. This step lets the bot find the right shop document for each question. The bot searches Bella's eight documents, passes the best matches to the model, and the model answers from them and names the file it used. The method is called retrieval-augmented generation, or RAG.

## Before you start

- Start from the step 10 folder. Copy its `examples/` and `tests/` folders, or use your own project from step 10.
- You need Ollama running with `qwen3:8b`.
- You need the embedding model `nomic-embed-text`. You downloaded it in step 3. If you have not, run step 1 below.

## Files in this step

| Status | File | What it does, and the key idea to notice |
|---|---|---|
| New | `examples/pizza_bot/shop_docs/` (eight `.txt` files) | Bella's shop documents: opening hours, allergens, refunds, gluten-free, old menu, delivery, ingredients and vouchers. Key idea: each file covers one topic and starts with a title line. |
| New | `examples/pizza_bot/search.py` | `load_documents()`, `keyword_search()` and `embedding_search()`. Key idea: keyword search needs the same words, while embedding search compares meanings. |
| New | `examples/pizza_bot/rag.py` | `answer_with_sources()`, which puts the best documents in the prompt. Key idea: the model answers from the documents it is given, and names the file it used. |
| New | `examples/pizza_bot/keyword_vs_embedding.py` | Runs both kinds of search on four questions. Key idea: the two searches can rank the same files in a different order. |
| New | `examples/pizza_bot/ask_the_shop.py` | Asks four customer questions and prints each answer with its source. Key idea: the file name at the end of each answer lets you check the source. |
| New | `examples/expected/keyword_vs_embedding.txt` and `ask_the_shop.txt` | Saved outputs of the two scripts above. Key idea: compare the two rankings for each question. |
| New | `tests/test_search.py` | Five tests of the search functions and the prompt. Key idea: fake embeddings let the tests check the ranking without a model. |

Unchanged: `model.py`, `vectors.py` (the same file as in step 3), `menu.txt`, and the earlier scripts.

## Steps

1. Download the embedding model, if you have not already. This needs Ollama and is a one-time step.

   ```bash
   ollama pull nomic-embed-text
   ```

2. Open the project folder.

   ```bash
   cd examples/pizza_bot
   ```

3. Compare keyword search with embedding search. This step needs Ollama and `nomic-embed-text`.

   ```bash
   python keyword_vs_embedding.py
   ```

   The script prints four questions. Each has a keyword line and an embedding line. For the first and last questions, the embedding search should put `gluten_free.txt` and `opening_hours.txt` first.
   Saved output: `examples/expected/keyword_vs_embedding.txt`. **Real run (your wording will differ).**

4. Ask the shop's documents four questions. This step needs Ollama and `qwen3:8b`.

   ```bash
   python ask_the_shop.py
   ```

   Each answer ends with the name of a file in square brackets. The names should be `opening_hours.txt`, `allergens.txt`, `refunds.txt` and `gluten_free.txt`, in that order. If the bot cites a different file, read the two documents it was given before you blame the model.
   Saved output: `examples/expected/ask_the_shop.txt`. **Real run (your wording will differ).**

## Run the tests

From the step folder:

```bash
python -m pytest -q
```

The result should be `38 passed`. The tests do not need Ollama.

## What you learned

- Keyword search misses a question that uses different words from the document.
- Embedding search compares meanings, so it can find a document with no matching words.
- Putting the right documents in the prompt, and asking for a source, makes an answer easier to check.

## Next

Go to [Step 12: Tools and Agents](../12-tools-and-agents/README.md).
