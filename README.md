# AI Engineering Library

**Author: Ravi Pal**

This is the companion code repository for the AI Engineering Library, a series of twelve books. Each book builds one realistic project with local AI models, one idea per chapter.

**Every book is self-contained.** Each book prints all the code, configuration, data, setup commands, tests and expected outputs that its exercises need. You do not need this repository to do the printed exercises. This repository is an **optional convenience**: it holds reference copies of the code, so you can compare your files with a known-good version.

**None of the books is published yet.** All twelve are in preparation.

## Catalogue

| # | Book | Primary project | Industry | Status | Folder |
|---|---|---|---|---|---|
| 1 | Applied AI Engineering | Pizza Store AI Assistant | Retail / Food | In preparation; sample checkpoint for Chapter 8 available | [books/applied-ai-engineering](books/applied-ai-engineering/README.md) |
| 2 | Prompt & Context Engineering | Travel Planning Assistant | Travel / Hospitality | In preparation | [books/prompt-and-context-engineering](books/prompt-and-context-engineering/README.md) |
| 3 | RAG Engineering | Company Knowledge Assistant | Enterprise / IT | In preparation | [books/rag-engineering](books/rag-engineering/README.md) |
| 4 | AI Agent Engineering | E-commerce Customer Service Agent | Online Retail | In preparation | [books/ai-agent-engineering](books/ai-agent-engineering/README.md) |
| 5 | Model Context Protocol | Personal Productivity Assistant | Productivity / SaaS | In preparation | [books/model-context-protocol](books/model-context-protocol/README.md) |
| 6 | AI Harness Engineering | Software Engineering Agent | Software Development | In preparation | [books/ai-harness-engineering](books/ai-harness-engineering/README.md) |
| 7 | Multi-Agent Systems | Logistics and Delivery Coordinator | Supply Chain | In preparation | [books/multi-agent-systems](books/multi-agent-systems/README.md) |
| 8 | AI Agent Workflows | Insurance Claims Processing | Insurance / Business Operations | In preparation | [books/ai-agent-workflows](books/ai-agent-workflows/README.md) |
| 9 | LLMOps | Customer Support AI Platform | SaaS / Customer Service | In preparation | [books/llmops](books/llmops/README.md) |
| 10 | AI Security | Banking Support Assistant | Banking / Financial Services | In preparation | [books/ai-security](books/ai-security/README.md) |
| 11 | AI System Design | Enterprise AI Platform | Enterprise Technology | In preparation | [books/ai-system-design](books/ai-system-design/README.md) |
| 12 | Multimodal AI | Product Inspection Assistant | Manufacturing / Quality Control | In preparation | [books/multimodal-ai](books/multimodal-ai/README.md) |

Only Applied AI Engineering has code in this repository so far. The other eleven folders contain a README that describes the planned layout.

## Using this repository

- Read the book's own folder README first. It explains the requirements, the configuration and how to run the tests.
- Each checkpoint is the complete project at the end of one chapter. Start from the checkpoint for the chapter you are on, or compare your files with it.
- Scripts that call a model need [Ollama](https://ollama.com) running on your computer. The default model is `qwen3:8b`. The address and model are set with environment variables, described in the Applied AI Engineering README.
- The tests use fake models. They run without Ollama, without the internet and without any paid service.

## Reader website

The [website/](website/README.md) folder holds the reader website: a homepage with all twelve
books, a landing page for each book, and the reading pages of Applied AI Engineering. It is
built with Astro and Starlight, and it is static. To build it locally:

```bash
cd website
npm ci
npm run check    # build, then the link and metadata checks
```

Only Applied AI Engineering has reading pages, and only when the author has authorised their
publication. Without them, the site builds and says that reading online is not yet available.

## Repository layout

```text
ai-engineering-library/
├── README.md                     this catalogue
├── STANDARDS.md                  the shared development standard
├── ruff.toml                     lint rules used by CI
├── tools/
│   └── check_repo.py             layout and wording checks used by CI
├── website/                      the reader website (see website/README.md)
├── .github/workflows/validate.yml
├── .github/workflows/website.yml
└── books/
    ├── applied-ai-engineering/
    │   ├── README.md
    │   ├── requirements-dev.txt
    │   ├── checkpoints/ch08-talking-to-models-from-code/
    │   └── exercises/ch08/
    └── <the other eleven books>/
        └── README.md
```

## Checks

```bash
python tools/check_repo.py
python -m ruff check books tools
python -m compileall -q books tools
```

To run the Chapter 8 tests:

```bash
cd books/applied-ai-engineering
python -m pip install -r requirements-dev.txt
cd checkpoints/ch08-talking-to-models-from-code && python -m pytest -q
cd ../../exercises/ch08 && python -m pytest -q
```

GitHub Actions runs these checks on Python 3.10 and 3.13 for every push and pull request. The workflow uses no secrets and calls no model.

## Licence

The code in this repository is released under the [MIT License](LICENSE). The books themselves are not in this repository; their text is © Ravi Pal, all rights reserved. The fonts in `website/public/fonts` are under the SIL Open Font License, as noted beside each file.
