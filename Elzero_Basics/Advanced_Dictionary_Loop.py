# ------------------------------
# -- Advanced Dictionary Loop --
# ------------------------------
mySkills = {
    "Html": "40%",
    "Css": "60%",
    "JavaScript": "80%",
    "python": "90%",
    "Java": "80%",
}
# print(mySkills.items())
#
# for skill in mySkills:
#     print(f"{skill} is {mySkills[skill]}")
# for key, value in mySkills.items():
#     print(f"{key}: {value}")
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
for main_key, main_value in peoples.items():
    print(f"{main_key}:")
    for child_key, child_value in main_value.items():
        print(f"{child_key} : {child_value}")
