#Task: Generate random array with random size
import numpy as np

size = np.random.randint(5, 10) #Generating the size first

arr = np.random.randint(1, 20, size=size) #Generating the array after generating array

print(arr)