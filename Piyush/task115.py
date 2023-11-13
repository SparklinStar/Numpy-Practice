import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = arr1 + arr2
# Result: array([5, 7, 9])
result2 = arr1 - arr2
# Result: array([-3, -3, -3])
result3 = arr1 * arr2
# Result: array([4, 10, 18])
result4 = arr1 / arr2
# Result: array([0.25, 0.4, 0.5])
print(result)
print(result2)
print(result3)
print(result4)
