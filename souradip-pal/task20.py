import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mp_img
import requests
from io import BytesIO

# Specify the URL of the image you want to use
image_url = 'https://freepngimg.com/thumb/tree/1-tree-png-image-download-picture.png'  # Replace with the actual image URL

# Download the image from the URL
response = requests.get(image_url)

if response.status_code == 200:
    # Read the image from the response content
    image_data = mp_img.imread(BytesIO(response.content))

    # Flip the image vertically
    image_b = np.flipud(image_data)

    # Display the flipped image
    plt.imshow(image_b)
    plt.show()
else:
    print('Failed to download the image. Check the URL and try again.')
