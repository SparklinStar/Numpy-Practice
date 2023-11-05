import numpy as np

matrix = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])


def custom_function(x):
    return np.sum(x)  # Sum the elements 

axis_to_apply = 0  # Apply along rows (axis 0)


result = np.apply_along_axis(custom_function, axis_to_apply, matrix)

print("Original matrix:")
print(matrix)
print("\nResult after applying the custom function along axis", axis_to_apply, ":")
print(result)
#end of 105
