# ------------------------------------
# Strings Indexing and Slicing
# 1 All Data In Python Is Object
# 2 Object Contain Elements
# 3 Every Element Has Its Own Index
# 4 Python use Zero Based Indexing
# 5 Use Square Brackets To Access Element
# 6 Enable Accessing Parts Of Strings,Tuples,Lists
# --------------------------------------


# Indexing (Access Single Item)
myString = "I love python"
print(myString[0])
print(myString[9])
print(myString[-2])
# Slicing (Access multiple Sequence Items)
# [Start:End] End not include
# [Start:End:Steps]
print(myString[8:11])  # yth
print(myString[3:5])  # ov
print(myString[:10])  # from zero (I love pyt)
print(myString[5:])  # to end (e python)
print(myString[:])  # full
print(myString[0::1])
print(myString[::1])
print(myString[::2])  # Ilv yhn
print(myString[::3])  # Io tn
