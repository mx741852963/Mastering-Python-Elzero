from operator import index

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 6, 4, 5, 23, 8, 45, 6, 5, 1, 2, 5, 6, 54, 6, 8, 45, 5]
myListTwo = []
myListThree = []
for a in myList:
    if a % 2 == 0:
        myListTwo.append(a)

myListTwo.sort()
print(myListTwo)
for b in myListTwo:
    if b not in myListThree:
        myListThree.append(b)

print(myListThree)
