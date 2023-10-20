import numpy as np
a = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

flipped_a = np.flip(a, axis=(0, 1))

print("original array:")
print(a)
print("\n horizontally and vertically flipped array:")
print(flipped_a)
#end of task28
