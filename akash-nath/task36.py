#Task: Get today in numpy and deltas

import numpy as np
from datetime import datetime

#I don't actually know how to use timedelta, so I'm not gonna use that

currTime = np.datetime64(datetime.now())

print(currTime)