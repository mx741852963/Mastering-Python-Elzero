# -------------------------------------------------
# -- Object Oriented Programming => Polymorphism --
# -------------------------------------------------
# n1 = 10
# n2 = 20
# print(n1 + n2)
# s1 = "ahmad"
# s2 = "ali"
# print(s1 + s2)
# print(len([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(len("Ahmad ALi"))
# print(len({"key_one": 1, "key_two": 2, "key_three": 3}))


class A:
    def do_something(self):
        print("From Class A")

        raise NotImplementedError("Derived Class Must Implement This Method ")


class B(A):
    pass


class C(A):
    def do_something(self):
        print("From Class C")


my_instance = C()
my_instance.do_something()
