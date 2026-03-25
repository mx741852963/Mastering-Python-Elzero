# -----------------
# --Strings Formatting Old Way__
# -----------------
name = "Ahmad"
age = 23
rank = 5
print("My name is " + name)
# print("My age is " + age) type error
print("My name is %s" % "Ahmad")
print("My name is %s" % name)
print("My name is: %s and my age is %d :" % (name, age))
print("My name is: %s and my age is :%d and my rank is : %f" % (name, age, rank))
# %s Strings
# %d Number
# %f Float
n = "ahmad"
l = "python"
y = 2
print("My name is %s Iam %s Developer With %d Years Exp" % (n, l, y))
# control floating point number
myNumber = 10
print("My number is %d" % myNumber)
print("My number is %f" % myNumber)
print("My number is %.2f" % myNumber)
# Truncate Strings
myLongString = "Hello People of Elzero Web School I love You All"
print("Message is : %s" % myLongString)
print("Message is : %.5s" % myLongString)
print("Message is : %.13s" % myLongString)
