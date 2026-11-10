"""The scripted conversation that forgetful_bot.py and remembering_bot.py share."""

SYSTEM = "You are the ordering bot for Bella's Pizza. Keep answers short."

EARLY_TURNS = [
    ("user", "Hi, my name is Priya. I'd like two large Pepperoni pizzas, please."),
    ("assistant", "Hello Priya! Two large Pepperoni pizzas. Anything else?"),
]

CHATTY_TURNS = [
    ("user", "Not yet. Is the shop busy tonight? I always wonder how you cope on Fridays."),
    ("assistant", "It gets busy, but the ovens are fast and the team is used to it."),
    ("user", "Lovely. I once worked in a cafe and the lunch rush was absolutely chaotic."),
    ("assistant", "Lunch rushes can be hectic. Thank you for your patience tonight."),
    ("user", "Do you ever get tired of the smell of baking dough all day long?"),
    ("assistant", "Never. Fresh dough is one of the best smells there is."),
    ("user", "Fair enough. My neighbour swears the best pizza has a really thin crust."),
    ("assistant", "Thin crusts are popular, though some customers prefer them thick."),
    ("user", "I can't decide which I like more. Maybe it depends on the weather outside."),
    ("assistant", "Many people say that. Cold nights suit a thick, hearty base."),
    ("user", "It is rather cold here tonight, now that you mention it."),
    ("assistant", "Then a hot pizza is exactly what you need."),
]

QUESTION = "What did I order, and what is my name?"
