# ---------------------
# -- Lists --
# ---------------------
# [1] List Items are enclosed in square brackets
# [2] List are ordered , to use index to access item
# [3] List are mutable => add,delete,edit
# [4] List item is not unique
# [5] List can have different date types
# --------------------

myAwesomeList = ["one", "two", "one", 1, 100.5, True]
print(myAwesomeList)  # whole list
print(myAwesomeList[1])  # two
print(myAwesomeList[-1])  # True
print(myAwesomeList[-3])  # 1

print(myAwesomeList[0:3:2])
print(myAwesomeList[0::2])
print(myAwesomeList[0:])

print(type(myAwesomeList[1]))
myAwesomeList[1] = "three"
print(myAwesomeList)
myAwesomeList[-1] = False
print(myAwesomeList)
myAwesomeList[3:4] = 15, 40
print(myAwesomeList)
myAwesomeList[0:4] = []
print(myAwesomeList)
