"""Exercise 5: limit the pizza field to the names on the menu."""

import copy

from orders import MENU_PIZZAS, ORDER_SCHEMA


def menu_order_schema() -> dict:
    """ORDER_SCHEMA with an enum on the pizza field, built from the menu.

    The model can then only answer with a pizza name from the menu. The schema
    still cannot tell whether a request is one the shop should accept, so
    validate_order() stays useful. The copy keeps ORDER_SCHEMA unchanged.
    """
    schema = copy.deepcopy(ORDER_SCHEMA)
    schema["properties"]["pizza"]["enum"] = list(MENU_PIZZAS)
    return schema
