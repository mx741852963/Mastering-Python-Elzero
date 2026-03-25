# ---------------------------
# -- Strings Methods --
# ---------------------------

a = "   I love python   "

b = "I         love       python"
print(len(a))
print(len(b))
# Strip() rstrip() lstrip()

print(a.strip())
print(a.rstrip())
print(a.lstrip())
c = "########### I love python #############"
print(c.strip("#"))
print(c.rstrip("#"))
print(c.lstrip("#"))
d = "@#@#@#@#I love python@#@#@#@#@#"
print(d.strip("@#"))
print(d.rstrip("@#"))
print(d.lstrip("@#"))
# Title()
e = "I love python and 5g technology and coding"
print(e.title())
# capitalize
f = "I love python and 5g technology and coding"
print(f.capitalize())
# zfill
g, h, k, l = "1", "11", "111", "1111"
print(g, h, k, l)
print(g.zfill(4), h.zfill(4), k.zfill(4), l.zfill(4))
# upper & lower
m = "AhmaD"
print(m.upper())
print(m.lower())
