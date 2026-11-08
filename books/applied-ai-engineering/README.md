# Applied AI Engineering

**Author:** Ravi Pal
**Primary project:** Pizza Store AI Assistant
**Industry:** Retail / Food
**Status:** In preparation. A sample checkpoint for Chapter 8 is available in this folder.

Applied AI Engineering builds one project from the first chapter to the last: an AI assistant for Bella's Pizza, a small pizza shop. Each chapter adds one idea to the same folder of Python files. You start with a single question to a local model and finish with a program that reads orders, searches the shop's documents and checks its own answers.

This folder contains the companion code for the book. The book is self-contained: every script, data file, test and expected output a chapter needs is printed in the book, and you do not need this repository to do the exercises. The code here is an optional convenience, so you can compare your files with a reference copy.

## What is here

| Path | What it holds |
|---|---|
| `checkpoints/ch08-talking-to-models-from-code/` | The project as it stands at the end of Chapter 8: every script, data file, saved output and test from Chapters 1 to 8. |
| `exercises/ch08/` | Chapter 8 exercise solutions that have a testable code answer, with their tests. |
| `requirements-dev.txt` | The test dependency, pytest. The book's code uses only the Python standard library. |

Later checkpoints will be added as the book's code is finished. Each one will be a full copy of the project at the end of its chapter.

## Requirements

- **Python 3.10 or newer.** The book uses Python 3.13.
- **Ollama**, the local model runtime, running on your computer. Chapter 1 explains how to install it.
- **A local model.** The book's outputs come from `qwen3:8b`, which needs about 5.2 GB of disk space and a laptop with 16 GB of memory. On an 8 GB machine, use `qwen3:1.7b` (about 1.4 GB) instead. Every example still runs, but the answers are weaker.
- **An embedding model** from Chapter 3 onward: `nomic-embed-text` (274 MB).

```bash
ollama pull qwen3:8b
ollama pull nomic-embed-text
```

The scripts need Ollama running to call a model. The tests and the scripts that print fixed output do not.

## Configuration

Configuration is read from environment variables. There is no configuration file and no `.env` loader.

| Variable | Default | Used for |
|---|---|---|
| `OLLAMA_BASE_URL` | `http://localhost:11434` | The address where Ollama is listening. |
| `OLLAMA_MODEL` | `qwen3:8b` | The chat model. Set it to `qwen3:1.7b` if you downloaded the smaller model. |
| `OLLAMA_EMBED_MODEL` | `nomic-embed-text` | The model that turns text into embeddings. |

The values are read in `model.py`. Setting one of them in your shell changes it for every script:

```bash
export OLLAMA_MODEL=qwen3:1.7b        # macOS or Linux
set OLLAMA_MODEL=qwen3:1.7b           # Windows Command Prompt
$env:OLLAMA_MODEL = "qwen3:1.7b"      # Windows PowerShell
```

No hosted provider is needed. The book's core examples run on Ollama alone.

## How checkpoints work

A checkpoint is the complete project at the end of one chapter. You can stop after any chapter, and you can start a later chapter from its checkpoint.

Each checkpoint folder has the same parts:

- `README.md`: what the chapter adds, which files are new, changed or unchanged, and the commands to run.
- `examples/`: the project. Scripts live in `examples/pizza_bot/`, and the saved outputs live in `examples/expected/`.
- `tests/`: the tests for the files in that checkpoint.

The scripts run from inside `examples/pizza_bot/`, and the tests find that folder themselves. You can run the tests from anywhere that has the checkpoint folder.

Saved outputs come in two kinds, and each checkpoint README says which is which:

- **Fixed output.** Scripts that do not call a model print the same text on every run. Running them again should match the saved file exactly.
- **Real runs.** Scripts that call a model print different wording on different machines and on different days. The saved file records one real run, and your output will differ.

## Running the tests

The tests use fake models. They never call Ollama, the internet or a paid service, so they pass without a model installed.

```bash
cd books/applied-ai-engineering
python -m pip install -r requirements-dev.txt

cd checkpoints/ch08-talking-to-models-from-code
python -m pytest -q
```

The Chapter 8 checkpoint has 24 tests. The exercise solutions have their own tests:

```bash
cd books/applied-ai-engineering/exercises/ch08
python -m pytest -q
```

## Chapter 8 checkpoint

The checkpoint is in [`checkpoints/ch08-talking-to-models-from-code`](checkpoints/ch08-talking-to-models-from-code/README.md). It adds two files to the project from earlier chapters: `orders.py`, which turns a customer's sentence into an `Order` and checks it against the menu, and `take_order.py`, which runs three customer messages through it.

The exercise notes for Chapter 8 are in [`exercises/ch08`](exercises/ch08/README.md).
