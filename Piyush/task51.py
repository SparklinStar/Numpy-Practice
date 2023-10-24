import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
min_values_column = np.min(matrix, axis=0)
print("Minimum values along columns:", min_values_column)
max_values_row = np.max(matrix, axis=1)
print("Maximum values along rows:", max_values_row)
matrix_sum = np.sum(matrix)
print("Sum of all elements in the matrix:", matrix_sum)
#end of task51
