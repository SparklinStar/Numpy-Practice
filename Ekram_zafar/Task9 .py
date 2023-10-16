#Task: Create array of strings
import numpy as np

words = ["Apple", "bat", "cat", "dog", "eiffle tower", "friends", "goose", "hands", "ink", "jackle", "kangaroo", "lemon", "man", "nine eleven", "optimus prime", "pinterest", "quarks", "rest", "strings", "time", "ultra", "violet", "world trade center", "xender", "yes", "zibra"] #Random strings according to alphabets

arr = np.random.choice(words, np.random.randint(1, 10))

print(arr)
