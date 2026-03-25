# -----------------
# --Type Conversion--
# -----------------

# str()
a = 10
print(type(a))
print(type(str(a)))
print("=" * 50)
# tuple()
c = "ahmad"  # String
d = [1, 2, 3, 4, 5]  # List
e = {"A", "B", "C", "D", "E"}  # Set
f = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}  # Dictionary
print(tuple(c))
print(tuple(d))
print(tuple(e))
print(tuple(f))
print("=" * 50)
# List()
c = "ahmad"  # String
d = (1, 2, 3, 4, 5)  # Tuple
e = {"A", "B", "C", "D", "E"}  # Set
f = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}  # Dictionary
print(list(c))
print(list(d))
print(list(e))
print(list(f))
print("=" * 50)
# Set()
c = "ahmad"  # String
d = (1, 2, 3, 4, 5)  # Tuple
e = ["A", "B", "C", "D", "E"]  # list
f = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}  # Dictionary
print(set(c))
print(set(d))
print(set(e))
print(set(f))
print("=" * 50)
# Dict()
# c = "ahmad"  # String
d = (("A", 1), ("B", 2), ("C", 3))  # Tuple
e = [["A", 1], ["B", 2], ["C", 3]]  # list
# f = {{"A", 1}, {"B", 2}}  # Set
# print(dict(c))
print(dict(d))
print(dict(e))
# print(dict(f))
