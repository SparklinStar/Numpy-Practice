import numpy as np

# Create two arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Calculate the outer product of arr1 and arr2
outer_product = np.outer(arr1, arr2)

# Multiply the outer product by another array or a scalar
# Here, we'll multiply it by a scalar for demonstration
scalar_multiplier = 2
result = outer_product * scalar_multiplier

print("Original arr1:")
print(arr1)

print("Outer product:")
print(outer_product)

print("Result after multiplying by a scalar:")
print(result)
