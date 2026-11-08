# Chapter 8 exercises

The five Chapter 8 exercises are in the book's "Exercises" section. This folder gives the code answers that can be tested, and says which exercises need a live model.

Before you start, copy `checkpoints/ch08-talking-to-models-from-code/examples/pizza_bot/` somewhere else, and make your changes in the copy. That keeps the reference files intact.

| Exercise | What it asks | Needs a live model? | Code answer in this folder |
|---|---|---|---|
| 1 | Change the third customer message in `take_order.py`, run it, and compare the pizza name with the menu. | Yes, a real run. Your output will vary. | No |
| 2 | Send a message with no size and find which system-prompt sentence sets the size. | Yes, a real run. The answer is reflective. | No |
| 3 | Add a third few-shot example with two pizzas, and explain what a single `pizza` field does with it. | Yes, a real run. The answer is reflective. | No |
| 4 | Put the menu into the system prompt, run again, and explain why `validate_order()` still matters. | Yes, a real run. The answer is reflective. | No |
| 5 | Build an `enum` for the `pizza` property from `MENU_PIZZAS`, and write about valid versus right orders. | The run and the written answer do. | Yes: the schema is in `solutions/ex05_pizza_enum.py`, with tests. |

## Exercise 5: the testable part

`solutions/ex05_pizza_enum.py` returns a copy of `ORDER_SCHEMA` whose `pizza` property has an `enum` taken from `MENU_PIZZAS`. The copy leaves `ORDER_SCHEMA` itself unchanged.

The tests check that the enum matches the menu, that the other fields are unchanged, that the original schema is not modified, and that "Vegan Supreme" is outside the enum and is rejected by `validate_order()`.

Run them from this folder. No model is needed:

```bash
cd books/applied-ai-engineering/exercises/ch08
python -m pytest -q
```

The live part of Exercise 5 is to pass this schema to the model and run the three messages. Use the schema in your copy of `orders.py`, since the reference `ORDER_SCHEMA` is unchanged. A model that honours the enum returns a menu name, but the answer can still be the wrong pizza for the customer, so the written answer should cover the difference between a valid order and a correct one.
