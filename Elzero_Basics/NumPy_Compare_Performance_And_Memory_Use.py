# NumPy – Compare Performance And Memory Use
# Performance
# Memory Use
import numpy as np
import time
import sys

# elements = 150000
# my_list1 = range(elements)
# my_list2 = range(elements)
# my_array1 = np.arange(elements)
# my_array2 = np.arange(elements)
# list_start = time.time()
# list_result = [(n1 + n1) for n1, n2 in zip(my_list1, my_list2)]
# # print(list_result)
# array_start = time.time()
# array_result = my_array1 + my_array2
# # print(array_result)
# List_Time = time.time() - list_start
# Array_Time = time.time() - array_start
# print(f" List Time {List_Time}")
# print(f" Array Time {Array_Time}")
# # for n1, n2 in zip(my_list1, my_list2):
#
# #     print(n1 + n2)
# print((Array_Time / List_Time) * 100)
my_array = np.arange(100)
print(my_array.itemsize)
print(my_array.size)
print(my_array.dtype)
print(my_array.ndim)
print(my_array.shape)
print(f"All Bytes Size = {my_array.size * my_array.itemsize} Bytes")
my_array = np.arange(100)
print(my_array.strides)
# The .strides property shows the number of bytes to step in each dimension.
# If it prints (8,), it means NumPy skips 8 bytes in memory to reach the next element.
# This confirms the use of int64 (8 bytes per element) on a 64-bit architecture.
my_list = range(100)
print(sys.getsizeof(my_list[0]))
print(sys.getsizeof(my_list[96]))
print(sys.getsizeof(my_list))
print(sys.getsizeof(my_array[0]))
print(sys.getsizeof(my_array[1]))
print(sys.getsizeof(my_array))
print(f"All Bytes Size = {(sys.getsizeof(my_list[0])) * len(my_list)} Bytes")
# -------------------------------------------------------------------------------------
# -- Memory Analysis: Python List vs. NumPy Array --
# -------------------------------------------------------------------------------------

# 1. Python List (Objects & Pointers):
# - sys.getsizeof(my_list[0]) -> 28 Bytes (Standard Python int object overhead).
# - A list stores "pointers" to objects scattered in memory, causing high overhead.

# 2. NumPy Array (Contiguous Memory):
# - sys.getsizeof(my_array[0]) -> 32 Bytes (NumPy scalar wrapper around raw data).
# - Although the wrapper is 32 bytes, the RAW data inside the array is only 8 bytes (int64).
# - sys.getsizeof(my_array) -> 912 Bytes (800 bytes for 100 elements + 112 bytes Metadata).
# - Metadata includes: .shape, .dtype, and .strides, which stay small regardless of array size.

# CONCLUSION: NumPy is efficient for "Big Data" because it stores raw values in a
# contiguous block, whereas Python lists store heavy objects and pointers.
# -------------------------------------------------------------------------------------
