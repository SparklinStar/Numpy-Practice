import numpy as np
from PIL import Image  

# Load an image using Pillow (PIL)
image = Image.open("example.png")

# Convert the image to a NumPy array
image_array = np.array(image)

# Print the shape and data type of the array
print("Shape:", image_array.shape)
print("Data Type:", image_array.dtype)
#end of task93
