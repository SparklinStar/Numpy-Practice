#Task: Print without truncation
import numpy as np

arr = np.arange(1000) #Truncation allows us to show very long arrays without any clutters

np.set_printoptions(threshold=np.inf)

print(arr)