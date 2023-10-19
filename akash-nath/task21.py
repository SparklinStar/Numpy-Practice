#Task: Numpy compare
import numpy as np

#There are many ways to compare two arrays. Some of them are given below

#Method 1:
a1 = np.array([1, 2, 3])
a2 = np.array([1, 2, 3])

result1 = a1 == a2 #Directly compares 2 arrays using "==" operator

print(result1)

#Method 2:
b1 = np.array([1, 2, 3])
b2 = np.array([1, 2, 3])

resul2 = np.array_equal(b1, b2) #Compares 2 identical arrays using np.array_equal function

print(resul2)

#Method 3:
c1 = np.array([1, 2, 3])
c2 = np.array([1.0, 2.0, 3.0])

resul3 = np.array_equiv(c1, c2) #Compares 2 arrays and checks if they are equivalent. In this method, 2 elements can be different, (eg. for c1 all the elements are decimal values where as for c2 they are float values. But they are equivalent as float characters doesn't have anything after decimal point)

print(resul3)

#Method 4:
d1 = np.array([1.0, 2.0, 3.0])
d2 = np.array([1.01, 2.01, 3.01])

result4 = np.isclose(d1, d2, atol=0.01) #Checks if 2 arrays are equal or close enough, with tolerance of 0.01

print(result4)

#Method 5:
e1 = np.array([1.0, 2.0, 3.0])
e2 = np.array([1.01, 2.01, 3.01])

result5 = np.allclose(e1, e2, atol=0.01) #Checks if all elements of 2 arrays are close, with tolerance of 0.01

print(result5)