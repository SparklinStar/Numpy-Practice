import numpy as np
singular_matrix = np.array([[111, 222], [1, 1]])
pseudo_inverse = np.linalg.pinv(singular_matrix)
print("Singular Matrix:")
print(singular_matrix)
print("Pseudo-Inverse:")
print(pseudo_inverse)
#end of task72
