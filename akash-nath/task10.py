#Task: Numpy array with strings and explit dtypes
import numpy as np

arr = np.array(["I", "am", "Ironman"], dtype='U10') #This allows only those unicode strings who are less than 10 in length

print(arr)