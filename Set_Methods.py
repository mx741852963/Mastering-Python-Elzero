# ---------------------
# -- Set Methods --
# ---------------------

# clear()
a = {1, 2, 3, 4, 5, 6}
a.clear()
print(a)
# union()

b = {1, 2, 3, 4, 5, 6}
c = {"one", "two", "three", "four", "five", "six"}
d = {"1", "2", "3", "4", "5", "6"}
print(b | c)
print(b.union(c, d))

# add()
e = {1, 2, 3, 4, 5, 6}
e.add(7)
e.add(8)
e.add(0)
print(e)

# copy()
f = {1, 2, 3, 4, 5, 6}
g = f.copy()
print(f)
print(g)
f.add(7)
print(f)
print(g)

# remove()
h = {1, 2, 3, 4, 5, 6}
h.remove(1)
# h.remove(0)
print(h)

# discard()
m = {1, 2, 3, 4, 5, 6}
m.discard(1)
m.discard(0)
print(h)

# pop()
i = {2, 3, 4, 5, 6}
print(i.pop())

# update()
j = {1, 2, 3, 4, 5, 6}
k = {"a", "b", "c", 1, 1, 2, 34}
j.update(k)
j.update(["css", "html"])
print(j)
