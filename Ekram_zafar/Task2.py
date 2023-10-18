# importing NumPy module with an alias name
import numpy as np

# creating a NumPy array
inputArray = np.array([])

# Checking whether the input array is empty or not using any() function

# Here it returns false if the array is empty else it returns true
temp_flag = np.any(inputArray)

# checking whether the temp_flag is false (Numpy array is empty)
if temp_flag == False:
   
   # printing empty array, if the condition is true
   print('Empty NumPy Input Array')
else:
   
   # else printing  NOT Empty
   print('Input NumPy Array is NOT Empty')
