#Task: Image as an array
import numpy as np
from PIL import Image

# Load a color image
color_image = Image.open("C:\\Users\\AKASH NATH\\Desktop\\vscode\\Numpy-Practice\\akash-nath\\ironman.webp")

# Convert the image to a NumPy array
color_array = np.array(color_image)
np.set_printoptions(threshold=np.inf)

print(color_array)
