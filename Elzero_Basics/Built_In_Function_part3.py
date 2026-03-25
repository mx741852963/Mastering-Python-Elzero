# -----------------------------
# -- Built In Function part3 --
# -----------------------------
# abs()
# pow()
# min()
# max()
# slice()
# ------------------------------

# abs()
x = - 10.5
print(abs(x))
# pow(base,exp,mod)
y = 2
print(pow(y, 5))
print(pow(y, 5, 10))  # (2*2*2*2*2)%10
# min(item,item,item,or iterators)
print(min(10, 5, 6, 5, 4))
z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(z))
print(min("x", "y", "Ahmad"))
# max(item,item,item,or iterators)
print(max(10, 5, 45, 6, 5, 4))
k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max(k))
print(max("x", "y", "Ahmad"))
# slice()
a = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
print(a[:5])
print(a[slice(2, 6, 2)])
