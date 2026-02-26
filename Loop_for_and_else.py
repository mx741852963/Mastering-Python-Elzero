# -----------------
# -- Loop => For --
# -----------------
# for item in iterable_object
#   Do Something With Item
# -----------------
# item is a variable you create and call whenever you want
# item refer to the current position  and will run and visit all items to the end
# iterable_object => sequence [ list,tuples,set,dict,string of characters,etc.....]
# -----------------

myNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in myNumber:
    # print(number * 17)
    if number % 2 == 0:  # Even
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
else:
    print("The Loop is Finished")

myName = input("Enter your name: ")
for letter in myName:
    print(letter.upper())
