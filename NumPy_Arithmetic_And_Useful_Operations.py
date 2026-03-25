# ---------------------------------------------
# -- Numpy => Arithmetic & Useful Operations --
# ---------------------------------------------
# - Addition
# - Subtraction
# - Multiplication
# - Divination
# ----------------
# - min
# - max
# - sum
# - ravel => Returns Flattened Array 1 Dimension With Same Type
# ----------------------------------------------
import numpy as np

# Arithmetic Operations
a1 = np.array([10, 20, 30])
a2 = np.array([5, 2, 4])
print(a1 + a2)  # Result => [15 22 34]
print(a1 - a2)  # Result => [ 5 18 26]
print(a2 - a1)  # Result => [ -5 -18 -26]
print(a1 * a2)  # Result => [ 50  40 120]
print(a1 / a2)  # Result => [ 2.  10.   7.5]
print(a1 // a2)  # Result => [ 2 10  7]
print(a1 % a2)  # Result => [0 0 2]
print(a1 ** a2)  # Result => [100000    400 810000]
print(a1 >= a2)  # Result => [ True  True False]
print("-" * 50)
b1 = np.array([[1, 2], [4, 5]])
b2 = np.array([[6, 7], [8, 9]])
print(b1 + b2)  # Result => [[ 7  9][12 14]]
print(b1 * b2)  # Result => [[ 6 14][32 45]]
print(b1 // b2)  # Result => [[0 0][0 0]]
print(b1 % b2)  # Result => [[1 2][4 5]]
print(b1 <= b2)  # Result => [[ True  True][ True  True]]
print("-" * 50)
# Min, Max, Sum
# STD (Standard Deviation) is not just a math term;
# mean Average
c1 = np.array([10, 20, 30, 40, 50, 60])
print(c1.min(), c1.max(), c1.mean(), c1.std(), c1.sum(), sep="\n")
print("-" * 50)
c2 = np.array([[10, 20], [30, 40], [50, 60]])
print(c2.min(), c2.max(), c2.sum(), c2.mean(), c2.std(), sep="\n")
# For both array c1 , c2 same result
# 10
# 60
# 210
# 35.0
# 17.07825127659933
print("-" * 50)
# Ravel
c2 = np.array([[10, 20], [30, 40], [50, 60]])
print(c2.ravel())
