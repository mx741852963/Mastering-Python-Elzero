# -----------------
# --Strings Formatting New Way__
# -----------------
name = "Ahmad"
age = 23
rank = 5
print("My Name is :{}".format(name))
print("My Name is :{}".format("Ahmad"))
print("My Age is :{}".format(age))
print("My name is: {} and my age is  :{}".format(name, age))
print("My name is: {:s} and my age is :{:d} and my rank is : {:f}".format(name, age, rank))
print("My name is: {:s} and my age is :{:d} and my rank is : {:.2f}".format(name, age, rank))
n = "ahmad"
l = "python"
y = 2
print("My name is {} Iam {} Developer With {} Years Exp".format(n, l, y))
myNumber = 10
print("My number is {:d}".format(myNumber))
print("My number is {:f}".format(myNumber))
print("My number is {:.3f}".format(myNumber))
myLongString = "Hello People of Elzero Web School I love You All"
print("Message is : {:s}".format(myLongString))
print("Message is : {:.5s}".format(myLongString))
print("Message is : {:.13s}".format(myLongString))
# Format Money
myMoney = 978532694518978
print(" My Money is {:d}".format(myMoney))
print("My Money is {:_d}".format(myMoney))
print("My Money is {:,d}".format(myMoney))
# print("My Money is {:&d}".format(myMoney))  Error
# ReArrange Items
a, b, c = "one", "two", "three"
print("Hello {} {} {}".format(a, b, c))  # Hello one two three
print("Hello {1} {2} {0}".format(a, b, c))  # Hello two three one
print("Hello {2} {1} {0}".format(a, b, c))  # Hello  three two one
x, y, z = 10, 20, 30
print("Hello {} {} {}".format(x, y, z))
print("Hello {2:d} {1:d} {0:d}".format(x, y, z))
print("Hello {2:.5f} {1:.4f} {0:.3f}".format(x, y, z))
# Format in Version 3.6+
myName = "Ahmad"
myAge = 23
print(f"My name is {myName} , my age is {myAge}")
