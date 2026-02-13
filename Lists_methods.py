# -------------------
# -- Lists_methods --
# -------------------

# append()
myFriends = ["John", "Doe", "Michael"]
myOldFriends = ["John", "Doe", "Michael"]
myFriends.append("Ali")
myFriends.append(100)
myFriends.append(100.5)
myFriends.append(myOldFriends)

print(myFriends)
print(myFriends[2])
print(myFriends[6])
print(myFriends[5])
print(myFriends[6][2])

# extend()
a = [1, 2, 3, 4, 5, 6]
b = ["a", "b", "c", "d", "e", "f"]
c = ["one", "two", "three", "four", "five"]
a.extend(b)
a.extend(c)
print(a)

# remove
x = ["one", "two", "three", "four", "five"]
x.remove("one")
print(x)

# sort
y = [1, 5, 6, 8, 3, 2, 1, 1, 4, -5, -0.6, 45]
y.sort()
print(y)
y.sort(reverse=True)
print(y)
# reverse()
z = [10, 15, 12, 45, 4, 5, 8, 6, 5, 5, 5, "ahmad"]
z.reverse()
print(z)
