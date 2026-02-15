# ---------------------
# -- Dictionary Methods --
# ---------------------
from click import clear

# clear()

user = {
    "name": "ahmad",
    "age": 20,
    "city": "tartous",
    "skills": ["css", "html"],
    "rating": 5.5
}
print(user)
user.clear()
print(user)
print("=" * 40)

# update()
member = {
    "name": "ahmad", }
print(member)
member["age"] = 30
print(member)
member.update({"name2": "ali"})
print(member)
print("=" * 40)

# copy()
main = {
    "name": "ahmad",
}
b = main.copy()
print(b)
main.update({"skills": "css"})
print(main)
print(b)
print("=" * 40)

# keys() + value()
print(main.keys())
print(main.values())
