# ------------------------------------
# -- Numpy => Array Shape & ReShape --
# ------------------------------------
# Shape Returns A Tuple Contains The Number Of Elements in Each Dimension
# ----------------------------------------------

import numpy as np

my_array1 = np.array([1, 2, 3, 4])
print(my_array1.ndim)
print(my_array1.shape)
print("_" * 50)
my_array2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_array2.ndim)
print(my_array2.shape)
print("_" * 50)
my_array3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
                      [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]])
print(my_array3.ndim)
print(my_array3.shape)
print("_" * 50)
my_array4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(my_array4.ndim)
print(my_array4.shape)
# print(my_array4.repeat(4, axis=0))
print(my_array4.reshape(4, 3))
print(my_array4.reshape(3, 4))
print(my_array4.reshape(2, 2, 3))
print(my_array4.reshape(2, 3, 2))
print("_" * 50)
my_array5 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
print(my_array5.reshape(4, 5))
print(my_array5.reshape(5, 4))
print("_" * 50)
my_array5 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
print(my_array5.reshape(4, 4))
my_array6 = my_array5.reshape(2, 2, 2, 2)
print(my_array6)
print(my_array6.shape)
print(my_array6.ndim)
my_array7 = my_array6.reshape(-1)
print(my_array7)
print(my_array7.shape)
print(my_array7.ndim)
