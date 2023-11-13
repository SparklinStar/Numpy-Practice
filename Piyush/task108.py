import numpy as np

# Create a sample NumPy array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Perform a circular shift along both rows and columns
shifted_array = np.roll(arr, shift=(1, 1), axis=(0, 1))

print("Original array:")
print(arr)
print("\nShifted array:")
print(shifted_array)
