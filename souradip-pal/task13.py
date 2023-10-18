# 13. Save Numpy to CSV

import numpy as np

a = np.asarray([[1, 2, 3], [4, 5, 6]])
print(a)

# Save the NumPy array to a CSV file named "abc.csv" with a comma as the delimiter
np.savetxt("abc.csv", a, delimiter=",")
