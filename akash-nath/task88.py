#Task: Delete specific indices

import numpy as np

#Deleting specific indices can be done in two methods

#Method - 1
arr = np.array([1,2,3,4,5,6,7,8,9])
arr = np.delete(arr,[0,1,2]) #Delete the indices 0,1,2

print(arr)

#Method - 2
arr = np.array([1,2,3,4,5,6,7,8,9]) #Reinitializing the array
arr = np.delete(arr,np.s_[0:3]) #Delete the indices 0,1,2

print(arr)