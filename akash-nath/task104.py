#Task: Serialize array with pickle

import numpy as np
import pickle

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(arr)

# Serialize array with pickle
with open('array.pkl', 'wb') as f:
    pickle.dump(arr, f)
    
with open('array.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
    