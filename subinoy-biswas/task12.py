import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)
meowarr = np.random.randint(100,24000,size=20000)
meowformatarr=meowarr.reshape(200,100)
print(meowformatarr)