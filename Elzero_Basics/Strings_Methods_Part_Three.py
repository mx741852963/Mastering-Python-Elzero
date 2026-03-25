# ---------------------------
# -- Strings Methods --
# ---------------------------
# index(SubString,Start,End)
a = "I love python and java"
print(a.index("p"))  # 7
print(a.index("p", 0, 10))  # 7
# print(a.index("p", 0, 5)) Error
# find(SubString,Start,End)
print(a.find("p"))  # 7
print(a.find("p", 0, 10))  # 7
print(a.find("p", 0, 5))  # -1
# rjust(Width,Fill Char) ljust(Width,Fill Char)
b = "ahmad"
print(b.rjust(10))
print(b.rjust(10, "#"))
print(b.ljust(10))
print(b.ljust(10, "#"))
# Splitlines()

e = """First line
Second line
Third line"""
print(e.splitlines())
f = """First line\nSecond line\nThird line"""
print(f.splitlines())
# expandtabs
g = "Hello\tWorld\tI\tLove\tPython"
print(g.expandtabs())
print(g.expandtabs(2))

one = "I Love Python And 3G"
two = "I love python and 3G"
print(one.istitle())
print(two.istitle())
three = " "
print(three.isspace())
four = ""
print(four.isspace())
five = "i love python "
six = "I love python"
print(five.islower())
print(six.islower())
seven = "ahmad_aljmal"
eight = "ahmadaljmal100"
nine = "ahmad--aljmal100"
print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())
x = "AaaaaBbbbbbbb"
print(x.isalpha())
z = "AaaaaBbbbbbbb123"
print(z.isalpha())
y = "AaaaaBbbbbbbb"
print(y.isalnum())
w = "AaaaaBbbbbbbb123"
print(w.isalnum())
