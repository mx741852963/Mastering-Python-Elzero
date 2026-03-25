# ----------------
# -- Generators --
# ----------------
# [1] Generators Is Function With "yield" Keyword Instead Of "return"
# [2] It Support Iteration And Return Generator Iterator By Calling "yield"
# [3] Generator Function Can Have One Of More "yield"
# [4] By Using next() It Resume From Where It Called "yield" Not from Beginning
# [5] When Called , Its Not Start Automatically , its Only Give You The Control
# -----------------------------------------------------------------------------
def myGenerator():
    yield 1
    yield 2
    yield 3
    yield 4


# print(myGenerator())
myGen = myGenerator()
# print(next(myGen))
# print("Hello World")
# print(next(myGen))
# print("Hello World")
# print(next(myGen))
# print("Hello World")
# print(next(myGen))
# print("Hello World")

for number in myGenerator():
    print(number)
