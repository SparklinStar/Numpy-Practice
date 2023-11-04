import numpy as np

# Create a sample 2D array
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

# Reverse the rows
reversed_rows = array_2d[::-1, :]

# Reverse the columns
reversed_columns = array_2d[:, ::-1]

print("Original 2D Array:")
print(array_2d)

print("2D Array with Reversed Rows:")
print(reversed_rows)

print("2D Array with Reversed Columns:")
print(reversed_columns)
#end of task 92
