import numpy as np

# Create an example array
original_array = np.array([10, 20, 30, 40, 50])

# Define a permutation (an array of indices)
permutation = np.array([3, 1, 4, 0, 2])

# Use np.take() to rearrange the array based on the permutation
rearranged_array = np.take(original_array, permutation)

print("Original array:")
print(original_array)

print("Permutation:")
print(permutation)

print("Rearranged array:")
print(rearranged_array)
#end of last task
#got to know about lot of numpy libraries
#END 
#COMPLETED THE NUMPY PRACTICE
