"""Chapter 10: a tiny check that flags pizza names not on Bella's menu."""

import re

def menu_names(menu_text: str) -> list[str]:
    """Pizza names from the menu: the text before the first run of spaces."""
    lines = menu_text.splitlines()[1:]
    return [line.split("  ")[0].strip() for line in lines if line.strip()]


def unsupported_pizzas(answer: str, menu_text: str) -> list[str]:
    """Pizza names in `answer` that are not on the menu.

    The heuristic: a top-level list item ("1." or "-", not indented) starts with a name, which ends
    at a bracket, colon, dash or bold marker. A name is fine if, without a
    trailing "Pizza", it is exactly a menu name.
    Items longer than five words are sentences, not names, and are skipped. Limits: it only reads list
    items, so a name inside a sentence slips through, and a list of
    something other than pizzas would be flagged. It is a smoke alarm,
    not a judge.
    """
    known = {name.lower() for name in menu_names(menu_text)}
    flagged = []
    for line in answer.splitlines():
        match = re.match(r"(?:\d+\.|[-*])\s*(.+)", line)
        if not match:
            continue
        name = re.split(r"\*\*|\(|:|\s[-–]\s", match.group(1).lstrip("*"))[0]
        name = re.sub(r"\s+Pizza$", "", name.strip())
        if name and len(name.split()) <= 5 and name.lower() not in known and name not in flagged:
            flagged.append(name)
    return flagged
