from PIL import Image
import os
import sys


def logo():
    if sys.platform.startswith('linux'):
        image_path = os.path.join("src", "images", "linux.png")
        return "Linux", image_path
    elif sys.platform.startswith('darwin'):
        image_path = os.path.join("src", "images", "macos.png")
        return "macOS", image_path
    elif sys.platform.startswith('win'):
        image_path = os.path.join("src", "images", "win10.png")
        return "Windows", image_path
    else:
        image_path = os.path.join("src", "images", "default.png")
        return "Unknown operating system", image_path

