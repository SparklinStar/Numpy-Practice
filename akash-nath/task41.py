#Task: Find the nearest element in the array
import numpy as np

#We have to specify a certain value to which nearest value will be determined

arr = np.arange(1, 25, 3)

target_value = 17

index = np.abs(arr - target_value).argmin() #This finds the index of the nearest values of 17 in the array

nearest_element = arr[index]

print(nearest_element)