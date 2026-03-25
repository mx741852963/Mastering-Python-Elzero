# ---------------------
# -- Set Methods --
# ---------------------

# issuperset()

a = {1, 2, 3, 4, 5, 6, 7, 8}
b = {1, 2, 3, 4, 5, 6, 7}
c = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(a.issuperset(b))
print(a.issuperset(c))
print("=" * 40)

# issubset()
d = {1, 2, 3, 4, 5, 6, 7, 8}
e = {1, 2, 3, 4, 5, 6, 7}
f = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(d.issubset(e))
print(d.issubset(f))

print("=" * 40)
# isdisjoint()
g = {1, 2, 3, 4, 5, 6, 7, 8}
h = {1, 2, 3, 4, 5, 6, 7}
i = {10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}
print(g.isdisjoint(h))
print(g.isdisjoint(i))
print("=" * 40)
