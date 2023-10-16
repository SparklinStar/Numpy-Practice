#Task: Checking whether an array is empty or not
import numpy as np

arr = np.array([])
print(arr)

if arr.size == 0:
    print("The array is empty")
else:
    print("The array is not empty")