# -------------------------------------------------------------------------
# -- NumPy Data Types (dtypes) - Engineering Reference --
# -------------------------------------------------------------------------
# 1. Numeric Types (Memory & Precision Control):
# 'b' : Signed Byte. 1 byte (-128 to 127).
# 'B' : Unsigned Byte. 1 byte (0 to 255). Optimal for image processing (RGB).
# 'i' : Signed Integer (e.g., int32, int64). Standard numeric data.
# 'u' : Unsigned Integer. Removes sign bit to double the positive maximum limit (e.g., IDs).
# 'f' : Floating-point (e.g., float32, float64). Crucial for ML model weights.
# 'c' : Complex-floating point. Used in Digital Signal Processing (DSP) & physics.
#
# 2. Logical & Time Types:
# '?' : Boolean (True/False). 1 byte. Heavily used in array masking and filtering.
# 'M' : Datetime. Stores dates/times as a contiguous block for Time-Series analysis.
# 'm' : Timedelta. Stores time differences or durations.
#
# 3. Text & Raw Data (Use with Caution in ML):
# 'U' : Unicode string. Supports all languages but consumes more memory.
# 'S' / 'a' : Byte string (ASCII only). Faster than Unicode but limited character set.
# 'O' : Python Object. **WARNING**: Destroys NumPy's speed. Forces the array to store
#       pointers like a standard Python list instead of contiguous raw data.
# 'V' : Void (Raw data). Used for interacting with C structs or low-level memory blocks.
# -------------------------------------------------------------------------
# -------------------------------------------
# -- Numpy => Data Types And Control Array --
# -------------------------------------------
# https://numpy.org/devdocs/user/basics.types.html
# https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html#specifying-and-constructing-data-types
# -------------------------------------------
# '?' boolean
# 'b' (signed) byte
# 'B' unsigned byte
# 'i' (signed) integer
# 'u' unsigned integer
# 'f' floating-point
# 'c' complex-floating point
# 'm' timedelta
# 'M' datetime
# 'O' (Python) objects
# 'S', 'a' zero-terminated bytes (not recommended)
# 'U' Unicode string
# 'V' raw data (void)
# ------------------------------------------------
import numpy as np

# Show Array Data Type
array1 = np.array(["A", "B", "C", "D", "E", "F"])
array2 = np.array([1, 2, 3, 4, 5, 6, 7])
array3 = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0])
print(array1.dtype)
print(array2.dtype)
print(array3.dtype)
print("-" * 50)
# Create Array With Specific Data Type
array4 = np.array(["A", "B", "C", "D", "E", "F"], dtype=object)
print(array4.dtype)
array5 = np.array([1, 2, 3], dtype=float)  # "float" or "f" or float
array6 = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], dtype=int)
print(array5.dtype)
print(array6.dtype)
print(array6)
print(array4.dtype)
print(array4)
print("-" * 50)
# Change Data Type Of Existing Array
my_array7 = np.array([0, 1, 2, 3, 0, 4])
print(my_array7.dtype)
print(my_array7)
print("-" * 50)
print(my_array7.astype(int))
print(my_array7.astype(float))
print(my_array7.astype(complex))
print(my_array7.astype(bool))
print(my_array7.astype(str))
print(my_array7.astype(object))
print("-" * 50)
# Test Capacity

my_array8 = np.array([100, 200, 300, 400], dtype='f')
print(my_array8.dtype)
print(my_array8[0].itemsize)  # 4 Bytes

my_array8 = my_array8.astype('float')  # Change To Float64
print(my_array8.dtype)
print(my_array8[0].itemsize)  # 8 Bytes
