# ------------------------------------
# -- Decorator Practical Speed Test --
# ------------------------------------
from time import time


# def myDecorator(func):  # Decorators
#     def nestedFunc(*numbers):  # any name
#         for number in numbers:
#             if number < 0:
#                 print("Beware on of The numbers is less than  0")
#
#         func(*numbers)  # Execute Function
#
#     return nestedFunc  # Return All Data
#
#
# @myDecorator
# def calculate(n1, n2, n3, n4):
#     print(n1 + n2 + n3 + n4)
#
#
# calculate(1, 2, 3, 4)
# calculate(-1, 2, 3, 4)
def speed_test(func):
    def wrapper():
        start = time()
        func()
        end = time()
        print(f"Speed Test: {end - start} ")

    return wrapper


@speed_test
def big_loop():
    for i in range(1, 20000):
        print(i)


big_loop()
