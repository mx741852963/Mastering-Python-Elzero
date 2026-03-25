# ---------------------
# -- Dictionary Methods
# ---------------------

# setdefault()

user = {
    "name": "ahmad",
}
print(user)
print(user.setdefault("age", 36))
print(user.setdefault("age", 40))
print(user)
print("=" * 40)

# popitem()
member = {
    "name": "ahmad",
    "skill": "css"
}
print(member)
member.update({"age": 23})
print(member.popitem())
print("=" * 40)

# items()

view = {
    "name": "ahmad",
    "skill": "css"
}
allItems = view.items()
print(view)
view["age"] = 23
print(allItems)
print("=" * 40)

# fromkeys()
a = ("myKeyOne", "myKeyTwo", "myKeyThree")
b = "x"
print(dict.fromkeys(a, b))
