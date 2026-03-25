# ---------------------
# -- Dictionary --
# ---------------------
# [1] Dict Items are enclosed in curly braces
# [2] Dict items are contains key:value
# [3] Dict key need to be immutable => (numbers , Strings , Tuple ) list not allowed
# [4] Dict value can have any data types
# [5] Dict key need to be unique
# [6] Dict is not ordered you can access its elements with key
# --------------------

# Dictionary
user = {
    "name": "ahmad",
    "age": 20,
    "city": "tartous",
    "skills": ["css", "html"],
    "rating": 5.5
}
print(user)
print(user["name"])
print(user["age"])
print(user["city"])
print(user.get("skills"))
print(user.keys())
print(user.values())

# Two-Dimensional Dictionary
languages = {
    "one": {
        "language": "python",
        "progress": "80"
    },
    "two": {
        "language": "java",
        "progress": "20"
    }
}
print(languages)
print(languages["one"]["language"])
print(languages["one"])
# Dictionary length
print(len(languages))
print(len(languages["two"]))

# create dictionary from variables
languagesOne = {
    "language": "python",
    "progress": "80"
}
languagesTwo = {
    "language": "java",
    "progress": "20"}
languagesThree = {"language": "css",
                  "progress": "30"}

allLanguages = {

    "one": languagesOne,
    "two": languagesTwo,
    "three": languagesThree
}
print(allLanguages)
