import numpy as np

# Create a sample NumPy array
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# Define a custom function to apply to each element
def custom_function(x):
    if x > 4:
        return x * 2
    else:
        return x
vectorized_function = np.vectorize(custom_function)
result = vectorized_function(data)

print("Original array:")
print(data)
print("\nResult after applying the custom function:")
print(result)
#task104end
