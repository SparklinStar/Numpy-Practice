#Task: Pearson product-moment correlation

import numpy as np

data1 = np.array([1, 2, 3, 4, 5])
data2 = np.array([2, 3, 4, 5, 6])

correlation_matrix = np.corrcoef(data1, data2)

# The correlation coefficient is the value at position (0, 1) or (1, 0) in the matrix
pearson_coefficient = correlation_matrix[0, 1]

print("Pearson's correlation coefficient:", pearson_coefficient)
