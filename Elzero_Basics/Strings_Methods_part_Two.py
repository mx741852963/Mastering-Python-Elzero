# ---------------------------
# -- Strings Methods --
# ---------------------------
# split() rsplit()
a = "I love python and java"
print(a.split())
b = "I-love-python-and-java"
print(b.split("-"))
c = "I-love-python-and-java"
print(c.split("-", 2))
print(c.rsplit("-", 2))
print(c.split("-", 3))
print(c.rsplit("-", 3))
# center
d = "ahmad"
print(d.center(9, "#"))
# count
f = "I love python and java because python is easy "
print(f.count("python"))
print(f.count("python", 0, 15))
# swapcase()
m = "I love python and java "
n = "I lOve pyThon aNd Java "
print(m.swapcase())
print(n.swapcase())
# startwith
i = "I love python and java because python is easy "
print(i.startswith("I"))
print(i.startswith("S"))
print(i.startswith("p", 7, 22))
# endwith
k = "I love python"
print(k.endswith("n"))
print(k.endswith("S"))
print(k.endswith("e", 2, 6))
