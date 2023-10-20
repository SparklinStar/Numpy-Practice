import numpy as np

# Create a sample 2D NumPy array
a = np.array([[1, 2, 5],
                [4, 11, 20],
                [7, 85, 90]])

flipped_a = np.flipud(a.copy())
flipped_a[0, 0] = 99
print("Original array:")
print(a)
print("\nFlipped array:")
print(flipped_a)
#end of task26
