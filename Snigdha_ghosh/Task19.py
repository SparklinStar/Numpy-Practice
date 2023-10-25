import numpy as np
a = np.array([1, 5, 3, 4, 9])

arr_view = arr.view()

arr_view[0] = 10
print("Original array:", arr)

print("View:", arr_view)
