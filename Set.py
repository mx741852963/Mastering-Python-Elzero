# ---------------------
# -- Set --
# ---------------------
# [1] Set Items are enclosed in curly braces
# [2] Set are not  ordered , and not indexed
# [3] Set indexing and slicing cant be done
# [4] Set item is unique
# [5] Set has only immutable data types (numbers,strings,tuples) List and dict are not
# --------------------


#  not ordered and not indexed
mySetOne = {"ahmad", "ali", 100}
print(mySetOne)
# print(mySetOne[0])
# Slicing cant be done
myTuple = (1, 2, 3, 4, 5, 6)
print(myTuple[0:3])
# mySetTwo = {1, 2, 3, 4, 5, 6}
# print(mySetTwo[0:3])

# Has only Immutable Types
# mySetThree = {1, 2, 3, "ahmad", True, [123]} TypeError: cannot use 'list' as a set element (unhashable type: 'list')
mySetThree = {1, 2, 3, "ahmad", True, (123, 113)}
print(mySetThree)

# Items is Unique
mySetFour = {1, 2, 1, "ahmad", "one", "ahmad", 5}
print(mySetFour)
