import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
outer_product = np.outer(arr1, arr2)
result = arr1 - outer_product  # Subtract from arr1
 result = arr2 - outer_product

print("Original arr1:")
print(arr1)

print("Outer product:")
print(outer_product)

print("Result:")
print(result)
