import numpy as np

# Create a NumPy array
original_array = np.array([1, 2, 3, 4, 5])

# Specify the elements you want to delete
elements_to_delete = [2, 4]

# Create a mask to identify the elements to delete
mask = np.isin(original_array, elements_to_delete)

# Use the mask to create a new array without the specified elements
new_array = original_array[~mask]

print("Original Array:", original_array)
print("New Array after deleting specified elements:", new_array)
#end of task96
