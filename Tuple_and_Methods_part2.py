# ----------------
# -- Tuple --
# ----------------


# Tuple with one element

myTuple1 = ("Ahmad"),
myTuple2 = "Ahmad",

print(myTuple1)
print(myTuple2)
print(type(myTuple1))
print(type(myTuple2))
print(len(myTuple1))
print(len(myTuple2))

# Tuple Concatenation

a = (1, 2, 3, 4)
b = (5, 6, 7, 8)
c = a + b
d = a + ("A", "B", True) + b
print(d)
print(c)

# Tuple , List , String Repeat(*)
myStr = "Ahmad"
myList = [1, 2]
myTuple = ("A", "B")
print(myStr * 6)
print(myTuple * 6)
print(myList * 6)

# Methods => count()
k = (1, 2, 3, 4)
print(k.count(1))
# Methods => index()
l = (1, 2, 3, 6, 4, 8, 5, 45, 7, 8, 4, 1, 1, 1, 5, 6, 94, 5)
print("The position of index is :{:d}".format(l.index(5)))
print(f"The position of index is :{l.index(5)}")

# Tuple Destruct
r = ("A", "B", 85, "C")
x, y, _, z = r
print(x)
print(y)
print(z)
