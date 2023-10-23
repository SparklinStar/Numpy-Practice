#Task: Shuffling by permutation

import numpy as np

#np.random.permutation() generates random permutations to shuffle an array

arr = np.array([1, 2, 3, 4, 5])
shuffled_array = np.random.permutation(arr)

print(arr)
print(shuffled_array)