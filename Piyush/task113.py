#Continguous Array
import numpy as np

# Create a non-contiguous NumPy array
arr_non_contig = np.array([[1, 2, 3], [4, 5, 6]])[:, ::2]

# Convert the non-contiguous array to a contiguous array
arr_contig = np.ascontiguousarray(arr_non_contig)

# Check if the arrays are contiguous
print("Is the non-contiguous array contiguous?", arr_non_contig.flags['C_CONTIGUOUS'])
print("Is the contiguous array contiguous?", arr_contig.flags['C_CONTIGUOUS'])
