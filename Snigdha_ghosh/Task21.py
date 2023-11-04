import numpy as np

a = np.array([[10, 25], [35, 45]])

a_inverse = np.linalg.inv(a)

print("original Matrix:")
print(a)
print("\n inverse Matrix:")
print(a_inverse)
