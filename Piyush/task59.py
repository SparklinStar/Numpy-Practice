import numpy as np
a = np.array([1, 2, 3, 4, 5])
b = np.array([2, 3, 4, 4, 5])
c = np.corrcoef(a, b)[0, 1]
print("Pearson's correlation coefficient:", c)
#end of task59
