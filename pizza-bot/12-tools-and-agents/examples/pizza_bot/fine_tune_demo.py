"""The same counting model, with and without question-and-answer examples."""

from pathlib import Path

from next_word import generate, train_next_word

folder = Path(__file__).parent
reviews = (folder / "reviews.txt").read_text(encoding="utf-8")
qa_pairs = (folder / "qa_pairs.txt").read_text(encoding="utf-8")

base_model = train_next_word(reviews)
tuned_model = train_next_word(reviews + "\n" + qa_pairs)  # the "fine-tuned" model

prompt = "question what vegetarian pizzas do you have answer"
last_word = prompt.split()[-1]

for name, counts in [("reviews only", base_model), ("reviews + Q&A", tuned_model)]:
    continuation = generate(counts, last_word, 8).split()[1:]
    print(f"{name:14}: {prompt} | {' '.join(continuation) or '(nothing)'}")
