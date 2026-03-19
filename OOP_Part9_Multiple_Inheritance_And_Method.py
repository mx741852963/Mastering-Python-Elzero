# -----------------------------------------------
# -- OOP Part9 Multiple Inheritance And Method --
# -----------------------------------------------
# class Food:  # Base Class
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         print(f"{self.name} Is Created From Base Class and Price is {self.price}")
#
#     def eat(self):
#         print("Eat Method Is From Base Class")
#
#
# class Apple(Food):  # Derived Class
#     def __init__(self, name, price, amount):
#         # Food.__init__(self, name) # Create Instance From Base Class
#         super().__init__(name, price)
#         # self.name = name
#         # self.price = price + 20
#         self.amount = amount
#         print(f"{self.name} Is Created From Derived Class and Price is {self.price} and Amount is {self.amount}")
#
#     def get_from_tree(self):
#         print("Get From Tree Method Is From Derived Class")
#
#     def eat(self):
#         print("Eat Method Is From Derived Class")
#
#
# # food_one = Food("Pizza")
# food_two = Apple("Pizza", 20, 5)
# food_two.eat()
# food_two.get_from_tree()
class BaseOne:
    def __init__(self):
        print("BaseOne")

    def func_one(self):
        print("One")


class BaseTwo:
    def __init__(self):
        print("BaseTwo")

    def func_two(self):
        print("Two")


class Derived(BaseOne, BaseTwo):
    pass


my_var = Derived()
# base_one = BaseOne()
# base_two = BaseTwo()
# derived_one = Derived()
# derived_two = Derived()
# print(Derived.mro())
print(my_var.func_one)
# print(my_var.func_two())


# my_var.func_one()
# my_var.func_two()
# class Base:
#     pass
#
#
# class DerivedOne(Base):
#     pass
#
#
# class DerivedTwo(DerivedOne):
#     pass
