import numpy as np
a = np.array([1, 2, 3, 4, 5])
b = np.array([2, 3, 4, 4, 5])
cross_correlation = np.correlate(a, b, mode='full')
print("Cross-correlation result:")
print(cross_correlation)
#end of task60
