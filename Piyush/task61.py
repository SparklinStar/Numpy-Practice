import numpy as np
a = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
unique_elements, counts = np.unique(a, return_counts=True)
for element, count in zip(unique_elements, counts):
    print(f"Element {element} occurs {count} times.")
#end of task61
