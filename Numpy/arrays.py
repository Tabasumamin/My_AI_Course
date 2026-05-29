import numpy as np

# 1D array
arr1 = np.array([10, 20, 30, 40])
print(arr1)

# 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

# Indexing
print(arr1[0])
print(arr2[1][2])

# Slicing
print(arr1[1:3])
print(arr2[:, 1])

# Shape
print(arr2.shape)