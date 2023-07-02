import os
from PIL import Image

# Get the path of the current module
module_path = os.path.abspath(__file__)

# Get the directory containing the current module
module_dir = os.path.dirname(module_path)

# Construct the file path relative to the module directory
image_path = os.path.join(module_dir, "../images/windows10.png")

# Use the image_path variable in your code
# For example, to open the image using PIL
image = Image.open(image_path)
