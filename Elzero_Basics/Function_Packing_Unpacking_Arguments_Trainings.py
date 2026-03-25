# ----------------------------------------------------
# -- Function Packing Unpacking Arguments Trainings --
# ----------------------------------------------------
mySkills = {"java": "80", "python": "60", "Css": "50"}
myTuple = ("Html", "Js", "Css")


def show_skills(name, *skills, **skillswithprogres):
    # print(f" Hello {name} Your skills are: {' , '.join(skills)}")
    print(f" Hello {name} \n Skills Without Progress : ")
    for skill in skills:
        print(f"- {skill}")
    print(" Skills With Progress : ")
    for key, value in skillswithprogres.items():
        print(f" - {key} => {value}")


show_skills("Ahmad", *myTuple, **mySkills)
