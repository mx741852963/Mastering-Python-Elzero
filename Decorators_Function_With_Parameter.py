# ----------------------------------------
# -- Decorators Function With Parameter --
# -----------------------------------------
def myDecorator(func):  # Decorators
    def nestedFunc(num1, num2):  # any name

        if num1 < 0 or num2 < 0:
            print("Beware on of The numbers is less than  0")

        func(num1, num2)  # Execute Function

    return nestedFunc  # Return All Data


def myDecorator2(func):  # Decorators
    def nestedFunc(num1, num2):  # any name

        print("coming from decorator 2")

        func(num1, num2)  # Execute Function

    return nestedFunc  # Return All Data


@myDecorator
@myDecorator2
def calculate(n1, n2):
    print(n1 + n2)


# calculate(5, 5)
calculate(-5, 0)
