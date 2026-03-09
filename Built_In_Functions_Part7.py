# ----------------------------------
# -- Built In Functions => ###### --
# ----------------------------------
# enumerate()
# help()
# reversed()
# ----------------------------------


# enumerate(iterable,start=0)
mySkills = ["Html", "Css", "Js", "PHP"]
mySkillsWithCounter = enumerate(mySkills, 1)
print(type(mySkillsWithCounter))
for counter, skill in mySkillsWithCounter:
    print(f"{counter}: {skill}")
print("#" * 50)
# help()
print(help(print))
print("#" * 50)
# reversed(iterable)
myString = " Ahmad"
print(reversed(myString))
for letter in reversed(myString):
    print(letter)
print("#" * 50)

for s in reversed(mySkills):
    print(s)
