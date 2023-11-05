import numpy as np

data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

condition = data[:, 1] > 4
column_to_sum = data[condition, 1]
result = np.sum(column_to_sum)

print("Sum of values in the second column where values are greater than 4:", result)
#end of task103
