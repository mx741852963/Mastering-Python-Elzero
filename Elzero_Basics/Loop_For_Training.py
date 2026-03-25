# -----------------
# -- Loop => For --
# --  Trainings  --
# -----------------


# Range
# myRange = range(1, 100)
# for number in myRange:
#     print(number)

mySkills = {
    "CSS": 10,
    "Python": 20,
    "JavaScript": 30,
    "java": 40,
    "PHP": 50,
}

for Skill in mySkills:
    # print(Skill)
    print(f"my progress in lang  {Skill.title()} and skill is {mySkills.get(Skill)}")
