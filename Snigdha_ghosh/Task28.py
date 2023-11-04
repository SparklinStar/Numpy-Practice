import numpy as np
a = np.array([[10, 15, 30], [40, 55, 60], [70, 85, 90]])

flipped_a = np.flip(a, axis=(0, 1))

print("original array:")
print(a)
print("\n horizontally and vertically flipped array:")
print(flipped_a)
