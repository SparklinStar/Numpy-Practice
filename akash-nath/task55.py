#Task: Cross correlation
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([5, 4, 3, 2, 1])

# Compute the cross-correlation
cross_correlation = np.correlate(arr1, arr2, mode='full') #The mode='full' parameter indicates that we want to compute the cross-correlation over the full range of possible lags, which includes positive and negative lags.

print("Cross-correlation result:", cross_correlation)
