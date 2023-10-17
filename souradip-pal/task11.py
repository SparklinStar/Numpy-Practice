import numpy as np
# 11. Numpy array with strings and explicit dtype
def create_string_array():
    """
    Creates a numpy array with a single string element and explicit dtype.
    Returns a new numpy array with each character of the string as a separate element.
    """
    x = np.array(['To'], dtype=object)
    y = x[0]
    print(y)
    return np.array(list(y))

print(create_string_array())
