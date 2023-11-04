import numpy as np  

a = np.random.randint(0, 10, (3, 3))
print('Before : ')
print(a)

print('\nAfter : ')
b = a[a[:, 2].argsort()]
print(b)
