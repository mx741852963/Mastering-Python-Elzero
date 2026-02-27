# -----------------------------------
# -- Function Parameters Arguments --
# -----------------------------------
# a, b, c = "Ahmad", "Ali", "karem"


# print(f"Hello {a}")
# print(f"Hello {b}")
# print(f"Hello {c}")


# def                       => Function keyword [Define]
# say_hello()               => Function Name
# name                      => Parameters
# print(f"Hello {name}")    => Task
# say_hello("Ahmad")        => Ahmad is the argument

# def say_hello(name):
#     print(f"Hello {name}")
#
#
# say_hello(a)
# say_hello(b)
# say_hello(c)

def addition(n1, n2):
    if type(n1) != int or type(n2) != int:
        print("Please enter a number")
    else:
        print(n1 + n2)


addition(100, "dfg")


def full_name(first, middle, last):
    print(f"hello {first.capitalize()} {middle.upper():.1s} {last.capitalize()}")


full_name("ahmad", "ahmad", "ali")
