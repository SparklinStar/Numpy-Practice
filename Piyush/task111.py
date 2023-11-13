import numpy as np
import pickle

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Serialize the array to a file
with open('serialized_array.pkl', 'wb') as file:
    pickle.dump(arr, file)

# Deserialize the array from the file
with open('serialized_array.pkl', 'rb') as file:
    deserialized_arr = pickle.load(file)

print("Original array:")
print(arr)
print("Deserialized array:")
print(deserialized_arr)
#end of task111
