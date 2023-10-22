import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

np.savetxt("myoutput.csv", a, delimiter=",")
