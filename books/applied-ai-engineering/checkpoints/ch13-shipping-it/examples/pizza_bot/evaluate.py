"""Chapter 13: run ten questions through the bot and grade the answers."""

import json
import re
from pathlib import Path

from agent import run_agent
from rag import answer_with_sources
from search import load_documents

here = Path(__file__).parent


def grade(answer: str, check: dict) -> bool:
    """Pass if every must_include text is present and no must_not_include text is."""
    text = answer.lower()
    wanted = all(word.lower() in text for word in check.get("must_include", []))
    banned = any(word.lower() in text for word in check.get("must_not_include", []))
    return wanted and not banned


def answer_question(question: str, documents: dict[str, str]) -> str:
    """The pipeline: order questions go to the agent, the rest to RAG."""
    if re.search(r"#\d+", question):
        return run_agent(question)
    return answer_with_sources(question, documents)


if __name__ == "__main__":
    documents = load_documents(here / "shop_docs")
    documents["menu.txt"] = (here / "menu.txt").read_text(encoding="utf-8")
    checks = json.loads((here / "eval_questions.json").read_text(encoding="utf-8"))
    passed = 0
    for check in checks:
        answer = answer_question(check["question"], documents)
        ok = grade(answer, check)
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'}  {check['question']}")
        if not ok:
            print("      answer:", answer.replace("\n", " ")[:200])
    print(f"Score: {passed}/{len(checks)}")
