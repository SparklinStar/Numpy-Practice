#Task: Float anomalies in Numpy Arange

import numpy as np

range_with_anomalies = np.arange(0.1, 1.0, 0.1)
print(range_with_anomalies)

#The result might not include the endpoint 1.0 due to rounding errors.