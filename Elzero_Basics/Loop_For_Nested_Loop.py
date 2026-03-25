# -----------------
# -- Loop => For --
# -- Nested loop --
# -----------------
peoples = {
    "ahmad": {
        "Html": "70%",
        "Css": "56%",
        "Python": "71%"
    },
    "Ali": {
        "Html": "90%",
        "Css": "59%",
        "Python": "42%"},
    "Karma": {
        "Html": "80%",
        "Css": "58%",
        "Python": "44%"
    }
}

for name in peoples:  # outer loop
    print(f"{name} Skills Is :")
    for skill in peoples[name]:
        print(f"- {skill} = > {peoples[name][skill]}")
