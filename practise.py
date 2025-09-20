import numpy as np

arr = np.array([1, 2, 3])

# Add scalar to array
print(arr + 10)   

# Add two arrays with different shapes
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix + arr)