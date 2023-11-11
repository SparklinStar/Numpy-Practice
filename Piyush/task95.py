import numpy as np

# Create a NumPy array
original_array = np.array([1, 2, 3, 4, 5])

# Specify the indices you want to delete
indices_to_delete = [1, 3]

# Delete the specified indices
new_array = np.delete(original_array, indices_to_delete)

print("Original Array:", original_array)
print("New Array after deleting specified indices:", new_array)
#end of task95
