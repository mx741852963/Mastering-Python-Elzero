# ----------------------------------------------
# -- Tuple --
# -----------
# [1] Tuple items are enclosed in parentheses
# [2] you can remove the parentheses if you want
# [3] Tuple are ordered , to use index to access item
# [4] Tuple are immutable => you cant add or delete
# [5] Tuple item is not unique
# [6] Tuple can have different data type
# [7] Operators Used in Strings and Lists Available in Tuples
# -----------------------------------------------

myAwesomeTupleOne = ("Osama", "Ahmad")
myAwesomeTupleTwo = "Osama", "Ahmad"
print(myAwesomeTupleOne)
print(myAwesomeTupleTwo)
print(type(myAwesomeTupleOne))
print(type(myAwesomeTupleTwo))
# Tuple Indexing
myAwesomeTupleThree = (1, 2, 3, 4, 5)
print(myAwesomeTupleThree[0])
print(myAwesomeTupleThree[-1])
print(myAwesomeTupleThree[-3])
# Tuple Assign Values
# myAwesomeTupleFour = (1, 2, 3, 4, 5)
# myAwesomeTupleFour[2] = "Three" TypeError: 'tuple' object does not support item assignment
# print(myAwesomeTupleFour)
# Tuple Items
myAwesomeTupleFive = ("Osama", "Ahmad", 100, 100, 125.2, True)
print(myAwesomeTupleFive[1])
print(myAwesomeTupleFive[-1])
