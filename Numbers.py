# ------------------
# --Numbers--
# ------------------
# Integer
print(type(1))
print(type(10))
print(type(100))
print(type(-1))
print(type(-10))
# Float
print(type(0.1))
print(type(0.100))
print(type(-0.100))
print(type(-1000.100))
# Complex
myComplexNumber = 5 + 6j
print(type(myComplexNumber))
print(type(myComplexNumber.real))
print("Real Part Is : {}".format(myComplexNumber.real))
print("Imaginary Part Is : {}".format(myComplexNumber.imag))

# [1] you can convert from int to float or complex
# [2] you can convert from float to int or complex
# [3] you cannot convert complex to any type
print(100)
print(float(100))
print(complex(100))
print(10.20)
print(int(10.20))
print(complex(10.20))
print(10 + 9j)
# print(int(10 + 9j))
