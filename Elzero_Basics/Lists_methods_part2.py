# -------------------
# -- Lists_methods --
# -------------------
#  clear()
a = [1, 2, 3, 4]
a.clear()
print(a)

# copy()
b = [1, 2, 3, 4]
c = b.copy()
print(b)  # main list
print(c)  # copied list

b.append(5)

print(b)  # main list
print(c)  # copied list

# count
d = [1, 1, 1, 1, 2, 5, 4, 1, 5, 6, 8, 7, 5, 2, 1, 5, 8]
print(d.count(1))

# index()

e = ["ali", "ahmad", "sayed", "Ramy", "ahmad", "Ramy"]
print(e.index("Ramy"))

# insert()

f = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "B", "C", "D", "E", "F"]
f.insert(0, "Test")
f.insert(-1, "Test")
print(f)

# pop()

g = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(g.pop(0))
print(g.pop(-1))
print(g)
