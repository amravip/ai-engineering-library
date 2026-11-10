"""The chat template, and the exact text the model receives."""

from model import MODEL, post_to_ollama

info = post_to_ollama("/api/show", {"model": MODEL})
template_lines = info["template"].splitlines()
print(f"Chat template for {MODEL} (first 25 of {len(template_lines)} lines):")
print("\n".join(template_lines[:25]))

question = "What vegetarian pizzas do you have?"
text_the_model_sees = (
    f"<|im_start|>user\n{question}<|im_end|>\n"
    "<|im_start|>assistant\n"
)
print()
print("What the model receives for one question:")
print(text_the_model_sees)
