# ------------------------------------------------------
# -- Regular Expressions => Group Trainings And Flags --
# ------------------------------------------------------


import re

my_web = "https://www.elzero.org:8080/category.php?article=105?name=how-to-do"

search = re.search(r"(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)", my_web)

# # print(dir(search))
# print(search.groups())
# for item in search.groups():
#     print(item)
print(f"Protocol : {search.group(1)}")
print(f"sub Domain : {search.group(2)}")
print(f"sub Domain name : {search.group(3)}")
print(f"Top level Domain : {search.group(4)}")
print(f"Port : {search.group(5)}")
print(f"Query String: {search.group(6)}")
