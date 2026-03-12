# --------------------------
# -- Iterable vs Iterator --
# --------------------------
# Iterable
# [1] Object Contains Data That Can Be Iterated Upon
# [2] Example (String,List,Tuple,Dictionary,Set)
# --------------------------------------------------
# Iterator
# [1] Object Used To Iterate Over Iterable Using next() Method Return 1 Element At A Time
# [2] You Can Generate Iterator From Iterable When Using Iter() Method
# [3] For Loop Already Calls Iter() method On The Iterable Behind THe Scene
# [4] Gives "StopIteration" if There is No Next Element
myString = "Ahmad"
# myList = [1, 2, 3, 4]
# # myNumbers = 10
# for i in myString:
#     print(i, end=" ")
# for n in myList:
#     print(n, end=" ")
# for s in myNumbers:
#     print(s, end=" ")
# TypeError: 'int' object is not iterable
# myIterator = iter(myString)
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))

for Letter in iter("Ahmad"):
    print(Letter, end=" ")
