---
title: "Running the examples"
description: "How to run the book's Python examples on your own computer with Ollama, what the browser pages can and cannot do, and how hosted providers fit in."
sidebar:
  label: "Running the examples"
  order: 1
---

The examples in this library are Python programs. You run them on your own computer, and they send their questions to a model running locally in Ollama. Nothing on this website runs an example, and the pages in your browser cannot reach a model on your computer.

## What runs where

Reading a page here takes no setup. Running an example needs three things on your computer.

1. **Python 3.10 or newer.** The books use Python 3.13.
2. **Ollama**, installed and running. It serves a local HTTP API at `http://localhost:11434` by default.
3. **The model files.** The Applied AI Engineering book uses `qwen3:8b` for chat and `nomic-embed-text` for embeddings. Chapter 1 explains how to download them.

Installing Python, Ollama and the model files needs an internet connection, once. After that, the local examples run without the internet.

## Settings

The programs read their settings from environment variables. You do not need to change any of them to follow the book.

| Variable | Default | What it sets |
|---|---|---|
| `OLLAMA_BASE_URL` | `http://localhost:11434` | Where Ollama is listening |
| `OLLAMA_MODEL` | `qwen3:8b` | The chat model |
| `OLLAMA_EMBED_MODEL` | `nomic-embed-text` | The embedding model |

Change a variable in the terminal before you run a script, because the code reads the settings once, when it starts. The Applied AI Engineering book explains the commands for each shell.

## Browser pages cannot call your model

The pages on this site are static documents. They do not run Python, and they cannot call a model on your computer. Every example is a program that you run in a terminal, and the model answers only that program.

## Hosted providers are optional

Some readers will want to try a hosted model from a provider. That is optional. A chat subscription does not necessarily include API credits, API use may be billed separately, and different providers expose different features, model names and parameters. Each book explains when a hosted provider is introduced and what it changes. No core exercise requires a paid service.
