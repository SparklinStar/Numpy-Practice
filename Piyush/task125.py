import numpy as np

# Create a sample 2D array
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# Specify the column indices you want to print
column_indices = [0, 2]  # Selecting columns 0 and 2

# Use array slicing to print the specified columns
selected_columns = data[:, column_indices]

print("Original 2D array:")
print(data)

print("Selected columns:")
print(selected_columns)
#end of task125
