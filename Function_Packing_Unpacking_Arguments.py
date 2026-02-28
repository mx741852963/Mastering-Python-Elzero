# ------------------------------------------------
# -- Function Packing Unpacking Arguments *Args --
# ------------------------------------------------
# print(1, 2, 3, 4)
# myList = [1, 2, 3, 4]
# print(myList)
# print(*myList)
# def say_hello(*peoples):  # n1 n2 n3 ......
#     for person in peoples:
#         print(f"hello {person}")
#
#
# say_hello("John", "Smith", "Smith", "Smith", "Smith", "Smith")
def show_details(name, *skills):
    for skill in skills:
        print(f"Hello {name} your Skills is {skill} ")


show_details("Ahmad", "Css", "Python")
