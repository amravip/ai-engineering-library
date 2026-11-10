"""Tests for search.py and rag.py. They never call Ollama."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "examples" / "pizza_bot"))

import rag  # noqa: E402
import search  # noqa: E402

DOCS = {
    "delivery.txt": "We deliver within three miles.",
    "vouchers.txt": "A voucher takes five pounds off.",
    "gluten_free.txt": "We do not offer gluten free bases.",
}


def test_load_documents_reads_shop_docs():
    folder = Path(__file__).parents[1] / "examples" / "pizza_bot" / "shop_docs"
    documents = search.load_documents(folder)
    assert len(documents) == 8
    assert "gluten" in documents["gluten_free.txt"].lower()


def test_keyword_search_ranks_by_overlap_and_ignores_stop_words():
    ranked = search.keyword_search("Do you deliver within miles?", DOCS, top=2)
    assert ranked[0][0] == "delivery.txt"
    assert len(ranked) == 2


def test_keyword_search_finds_nothing_when_words_differ():
    assert search.keyword_search("coeliac", DOCS)[0][1] == 0


def test_embedding_search_ranks_by_cosine(monkeypatch):
    fake = {"q": [1.0, 0.0], DOCS["delivery.txt"]: [0.0, 1.0],
            DOCS["vouchers.txt"]: [0.9, 0.1], DOCS["gluten_free.txt"]: [0.5, 0.5]}
    monkeypatch.setattr(search, "embed", lambda texts: [fake[t] for t in texts])
    ranked = search.embedding_search("q", DOCS, top=2)
    assert [name for name, _ in ranked] == ["vouchers.txt", "gluten_free.txt"]


def test_answer_with_sources_puts_labelled_documents_in_prompt(monkeypatch):
    seen = {}

    def fake_ask(prompt):
        seen["prompt"] = prompt
        return "ok"

    monkeypatch.setattr(rag, "embedding_search", lambda q, d, top: [("delivery.txt", 0.9)])
    monkeypatch.setattr(rag, "ask_model", fake_ask)
    assert rag.answer_with_sources("Where?", DOCS) == "ok"
    assert "[delivery.txt]" in seen["prompt"] and "three miles" in seen["prompt"]
    assert "voucher" not in seen["prompt"]
