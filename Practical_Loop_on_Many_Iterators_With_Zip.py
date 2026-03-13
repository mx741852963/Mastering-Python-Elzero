# -------------------------------------------------
# -- Practical Loop on Many Iterators With Zip() --
# -------------------------------------------------
# zip() return a zip objects contains all objects
# zip() length is the length of lowest object
# --------------------------------------------------
list1 = [1, 2, 3, 4, 5]
list2 = ["A", "B", "C", "D"]
tuple1 = ("Man", "women", "boy", "girl")
dict1 = {"name": "ahmad", "age": 23, "country": "syria"}

for item1, item2, item3, item4 in zip(list1, list2, tuple1, dict1):
    print("List 1 item =>", item1, )
    print("List 2 item =>", item2)
    print("Tuple item =>", item3)
    print("dict item =>", item4, "Value=>", dict1[item4])

# ultimate = zip(list1, list2)
# print(ultimate)
# for item in ultimate:
#     print(item)
