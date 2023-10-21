import numpy as np

meowarr = np.random.randint(100,24000,size=20)
np.savetxt("output.csv",meowarr.reshape(2,10),delimiter=",")