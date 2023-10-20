import numpy as np

# Create a sample 2D NumPy array
a = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

# Flip the array horizontally using slicing
flipped_a = a[:, ::-1]

# Print the original and flipped arrays
print("Original array:")
print(a)
print("\n Horizontally Flipped array:")
print(flipped_a)
