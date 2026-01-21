# ---------------------------
# -- Strings Methods --
# ---------------------------
# replace(Old Value, New Value , count)
a = "Hello one two Three one one "
print(a.replace("one", "1"))
print(a.replace("one", "1", 1))
print(a.replace("one", "1", 2))
# join(Iterable)
myList = ["ahmad", "ahmad", "aljmal"]
print("_".join(myList))
print(" ".join(myList))
print("\n".join(myList))
print("\t".join(myList).expandtabs(5))
print(type(" ".join(myList)))
