# ----------------------------------------------
# Function Packing Unpacking Arguments **KWArgs
# ----------------------------------------------
# def show_skills(*skills):
#     print(type(skills))
#     for skill in skills:
#         print(f"your skill is  {skill}")
#
#
# show_skills("java", "python", "Css")
mySkills = {"java": "80", "python": "60", "Css": "50"}


def show_skills(**skills):
    print(type(skills))
    for skill, value in skills.items():
        print(f"your skill is  {skill} and value is {value}")


# show_skills(java="80", python="60", Css="50")
show_skills(**mySkills)
