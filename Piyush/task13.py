import numpy as np


a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

file_name = "me"

# Save the NumPy array to a CSV file
np.savetxt(file_name, a, delimiter=',') 
#end of task13
