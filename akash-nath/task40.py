#Task: String to numpy array

import numpy as np

string_list = ["Apple", "bat", "cat", "dog", "eiffle tower", "friends", "goose", "hands", "ink", "jackle", "kangaroo", "lemon", "man", "nine eleven", "optimus prime", "pinterest", "quarks", "rest", "strings", "time", "ultra", "violet", "world trade center", "xender", "yes", "zibra"]

arr = np.array(string_list, dtype=np.str_)

print(arr)