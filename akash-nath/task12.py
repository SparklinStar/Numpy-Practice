#Task: Save Numpy to CSV
import numpy as np

data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

file_path = 'nineEleven.csv' #the csv file to save the data

data.tofile(file_path, sep=',', format='%10.5f')