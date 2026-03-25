# ---------------------
# -- Set Methods --
# ---------------------


# difference()

a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
b = {1, 2, 3, "ahmad"}
print(a)
print(a.difference(b))  # a-b
print(a)
print(a - b)

print("=" * 40)  # separator

# difference_update()

c = {1, 2, 3, 4, 5, 6, 7, 8, 9}
d = {1, 2, 3, "ahmad"}
print(c)
c.difference_update(d)  # a-b
print(c)
print(c - d)

print("=" * 40)  # separator
# intersection()
e = {1, 2, 3, 4, "x"}
f = {"ahmad", "x", 2}
print(e)
print(e.intersection(f))  # e & f
print(e)

print("=" * 40)  # separator
# intersection_update()
g = {1, 2, 3, 4, "x"}
h = {"ahmad", "x", 2}
print(g)
print(g.intersection_update(h))  # e & f
print(g)

print("=" * 40)  # separator
# symmetric_difference()
i = {1, 2, 3, 4, "x"}
j = {2, 3, 4, 5, 6, "z"}
print(i)
print(i.symmetric_difference(j))  # i^j
print(i)

print("=" * 40)  # separator
# symmetric_difference_update()
k = {1, 2, 3, 4, "x"}
l = {2, 3, 4, 5, 6, "z"}
print(k)
print(k.symmetric_difference_update(l))
print(k)
