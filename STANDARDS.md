# Development Standard

This standard applies to the companion code of every book in the AI Engineering Library. It keeps the code of all twelve books consistent, so a reader who has finished one book can read the code of the next.

## Python

- Python 3.10 or newer. The code is tested on Python 3.13. CI also runs the tests on Python 3.10.
- Use the standard library first. Each book declares its few extra dependencies in a `requirements-dev.txt` file, which holds pytest for the tests.
- Add a framework only when a chapter teaches it. Until then, the code uses plain functions, dictionaries and dataclasses.

## Models and configuration

- Ollama is the default model runtime. Examples call Ollama's HTTP API on the local computer.
- Configuration comes from environment variables. There is no `.env` loader and no configuration framework.
- The variables are `OLLAMA_BASE_URL` (default `http://localhost:11434`), plus the book's model variables. Those are defined and defaulted in the book's `model.py`. The Applied AI Engineering book uses `OLLAMA_MODEL` (default `qwen3:8b`) and `OLLAMA_EMBED_MODEL` (default `nomic-embed-text`).
- A hosted provider may be offered as an option. It is never required to run the core examples or the tests.

## Layout

Every book follows this layout. Folders appear only when the book has code to put in them.

```text
books/<slug>/
├── README.md                    overview, requirements, configuration, how to run
├── requirements-dev.txt         test dependencies
├── checkpoints/
│   └── chNN-<topic>/            the complete project at the end of chapter NN
│       ├── README.md            what exists, what the chapter adds, files new, changed or unchanged, commands, expected results
│       ├── examples/            the project files; saved outputs in examples/expected/
│       └── tests/               tests for the files in this checkpoint
└── exercises/
    └── chNN/
        ├── README.md            the chapter's exercises by number, and which need a live model
        ├── solutions/           code answers that can be tested
        └── tests/               tests for the solutions
```

Names follow the book's own project. Use slugs and file names that describe the domain, such as `orders.py`, `check_order()` and `Order`, rather than abbreviations.

## Checkpoints

- A checkpoint is the complete project at the end of one chapter, so a reader can stop after any chapter and resume from it.
- Each checkpoint lists its files as new, changed or unchanged, and says how to check that earlier behaviour still works.
- The files in a checkpoint are verified copies of the book's code. A sync check confirms that they match the source.

## Code style

- Small functions with meaningful names. Keep each function short enough to read in a printed book.
- Type hints on every function signature.
- Explicit errors with messages a reader can act on.
- Comments explain why, not what. Docstrings are one or two sentences.
- Avoid unnecessary abstraction, deep inheritance and clever one-line expressions.
- Format and lint with ruff, using the rules in `ruff.toml`. Ruff runs in CI. Readers do not need it.

## Testing

- Unit tests use fakes. They never call a live model, the internet or a paid API.
- Fake the model by replacing the function that calls Ollama, for example `chat` or `urlopen`, and check what was sent and how the reply is handled.
- Live-model scripts are run by hand. Their saved outputs are real runs. They are labelled as real runs, record the model, the Ollama version and the date, and say that the wording will vary.
- Scripts that call no model must print the same text on every run, and the saved output must match it exactly.
- Regression tests keep earlier behaviour working when a later chapter changes a file.

## Self-containment

- The book prints everything a reader needs: code, configuration, dependencies, setup commands, test code, data and expected output.
- This repository mirrors the book's code. It is an optional convenience. Nothing in a book depends on it.
- Setup assumes only the tools a reader installs: Python, Ollama, Python packages and the model files.

## What never goes in this repository

- Manuscripts, reviews, planning notes and drafts.
- Cover sources and exports, figure sources, and built books in PDF or EPUB form.
- Publishing tooling and build scripts.
- Secrets, API keys and `.env` files.

`.gitignore` blocks the common forms of these, and `tools/check_repo.py` fails the build if one of them is present.

## Checks

Run these from the repository root:

```bash
python tools/check_repo.py
python -m ruff check books tools
python -m compileall -q books tools
cd books/applied-ai-engineering/checkpoints/ch08-talking-to-models-from-code && python -m pytest -q
cd ../../exercises/ch08 && python -m pytest -q
```

GitHub Actions runs the same steps on every push and pull request, on Python 3.10 and 3.13. The workflow sets `OLLAMA_BASE_URL` to a closed port, so a test that reaches for a live model fails.
