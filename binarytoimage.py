###################################################PROG 3#############################################
### convert binary number into image

from PIL import Image
import numpy as np

# Read binary data from file
with open('Binary_text.txt', 'rb') as f:
    binary_data = f.read()

# Convert binary data to numpy array
binary_array = np.frombuffer(binary_data, dtype=np.uint8)

# Calculate dimensions of image
width = 100  # Choose a desired width
height = int(np.ceil(len(binary_array) / width))

# Pad binary array with zeros to fit into image dimensions
padding = width * height - len(binary_array)
binary_array = np.pad(binary_array, (0, padding), 'constant')

# Reshape binary array into 2D array
image_array = np.reshape(binary_array, (height, width))

# Convert 2D array to PIL Image
image = Image.fromarray(image_array, mode='1')

# Save image to file
image.save('binary_image1.png')