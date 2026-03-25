# ----------------------
# -- Decorators Intro --
# ----------------------
# [1] Sometime called meta_programing
# [2] everything in python is object even function
# [3] Decorators take a function and some functionality and return it
# [4] Decorators Wrap other function and enhance their behavior
# [5] Decorators is higher order function (function accept function as parameter )
# -----------------------------------------------------------------------------------
def myDecorator(func):  # Decorators
    def nestedFunc():  # any name

        print("Before")  # Message From Decorator

        func()  # Execute Function

        print("After")  # Message From Decorator

    return nestedFunc  # Return All Data


@myDecorator  # Syntactic Sugar
def say_hello():
    print("Hello From Say Hello Function")


@myDecorator
def say_hello2():
    print("Hello From Say Hello Function 2 ")


# say_hello()
# afterDecoration = myDecorator(say_hello)
say_hello()
say_hello2()
