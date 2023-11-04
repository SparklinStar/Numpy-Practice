import numpy as np

# Create a sample 2D array
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

# Select specific columns (columns 0 and 2 in this example)
selected_columns = array_2d[:, [0, 2]]

print("Original 2D Array:")
print(array_2d)

print("Selected Columns:")
print(selected_columns)
#end of task100
