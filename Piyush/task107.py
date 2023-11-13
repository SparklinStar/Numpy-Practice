import numpy as np

# Create a sample NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Perform a circular shift of 2 positions to the left
shifted_array = np.roll(arr, shift=-2)

print("Original array:")
print(arr)
print("\nShifted array:")
print(shifted_array)
#end of task107
