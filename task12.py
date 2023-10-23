import numpy as np

x = np.arange(10000)

print('Before setting print options : ')
print(x)

import sys

np.set_printoptions(threshold=sys.maxsize)

print('After setting print options : ')
print(x)
