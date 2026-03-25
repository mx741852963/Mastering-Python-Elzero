# NumPy – Array Slicing
import numpy as np

# slicing => [strat:end:steps] not including end
a = np.array(["A", "B", "C", "D", "E", "F"])
print(a.ndim)
print(a[1])
print(a[1:4])
print(a[:4])
print(a[4:])
print("=" * 50)
b = np.array([["A", "B", "X"], ["C", "D", "Y"], ["E", "F", "Z"], ["M", "N", "O"]])
print(b.ndim)
print(b[:3])
print("=" * 50)
print(b[:3, :2])
print("=" * 50)
print(b[2:, 0])
print(b[2:, -1])
