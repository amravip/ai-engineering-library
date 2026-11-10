# Chapter 11: Retrieval-Augmented Generation

This chapter lets the bot find the right shop document for each question. The bot searches Bella's eight documents, passes the best matches to the model, and the model answers from them and names the file it used.

## Before you start

- Start from the checkpoint `ch10-hallucination`. Copy its `examples/` and `tests/` folders, or use your own project from Chapter 10.
- You need Ollama running with `qwen3:8b`.
- You need the embedding model `nomic-embed-text`. You downloaded it in Chapter 3. If you have not, run step 1 below.

## Files in this step

| Status | File | What it does | Listing |
|---|---|---|---|
| New | `examples/pizza_bot/shop_docs/` (eight `.txt` files) | Bella's shop documents: opening hours, allergens, refunds, gluten-free, old menu, delivery, ingredients and vouchers. Each file starts with a title line. | 11.1 to 11.5 print five of them. Appendix B prints all eight. |
| New | `examples/pizza_bot/search.py` | `load_documents()`, `keyword_search()` and `embedding_search()`. | 11.6, 11.7 |
| New | `examples/pizza_bot/rag.py` | `answer_with_sources()`, which puts the best documents in the prompt. | 11.8 |
| New | `examples/pizza_bot/keyword_vs_embedding.py` | Runs both kinds of search on four questions. | Described in the text |
| New | `examples/pizza_bot/ask_the_shop.py` | Asks four customer questions and prints the answers with their sources. | Described in the text |
| New | `examples/expected/keyword_vs_embedding.txt` and `ask_the_shop.txt` | Saved outputs of the two scripts above. | Output 11.1 and 11.2 |
| New | `tests/test_search.py` | Five tests of the search functions and the prompt. They use fake embeddings and a fake model. | Not printed in the chapter |

Unchanged: `model.py`, `vectors.py` (its listing is printed again in Chapter 11, and it is the same file as Chapter 3), `menu.txt`, and the earlier scripts.

## Steps

1. Download the embedding model, if you have not already. This needs Ollama and is a one-time step.

   ```bash
   ollama pull nomic-embed-text
   ```

2. From the checkpoint folder, open the project folder.

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

From the checkpoint folder:

```bash
python -m pytest -q
```

The result should be `38 passed`. The tests do not need Ollama.

## Next

Go to [Chapter 12: Tools and Agents](../ch12-tools-and-agents/README.md), in the checkpoint `ch12-tools-and-agents`.
