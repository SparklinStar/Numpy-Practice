import numpy as np

# Create a sample NumPy array
array = np.array([1, 2, 3, 4, 5, 6])

# Apply a condition to filter elements greater than 3
condition = array > 3
filtered_array = array[condition]

print("Original Array:")
print(array)

print("Filtered Array (elements greater than 3):")
print(filtered_array)
#end of task102
