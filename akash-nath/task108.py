#Task: Element-wise math

import numpy as np

# Create NumPy arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([5, 4, 3, 2, 1])

# Addition
result_add = arr1 + arr2  # Element-wise addition

# Subtraction
result_sub = arr1 - arr2  # Element-wise subtraction

# Multiplication
result_mul = arr1 * arr2  # Element-wise multiplication

# Division
result_div = arr1 / arr2  # Element-wise division

# Exponentiation
result_exp = np.exp(arr1)  # Element-wise exponentiation


print(result_add)
print(result_sub)
print(result_mul)
print(result_div)
print(result_exp)