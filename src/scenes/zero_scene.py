import tkinter as tk
from PIL import Image, ImageTk
import os

class ZeroScene:
    def __init__(self, window):
        self.window = window
        self.logo_image_path = os.path.join(os.path.dirname(__file__), "..", "images", "windows10.png")
        self.logo_image = None
        self.logo_label = None
        self.start_button = None

    def show(self):
        # Load the logo image using PIL
        self.logo_image = Image.open(self.logo_image_path)

        # Resize the logo image to a smaller size
        smaller_logo_image = self.logo_image.resize((200, 50))  # Adjust the size as needed

        # Create a Tkinter-compatible photo image from the smaller logo image
        logo_photo = ImageTk.PhotoImage(smaller_logo_image)

        # Create a label to display the logo image
        self.logo_label = tk.Label(self.window, image=logo_photo)
        self.logo_label.image = logo_photo  # Store a reference to prevent image from being garbage collected
        self.logo_label.grid(row=0, column=0, padx=10, pady=10, sticky="nw")  # Position at top-left corner

        # Create the "Start" button
        self.start_button = tk.Button(self.window, text="Start", command=self.start_setup)
        self.start_button.grid(row=1, column=0, padx=10, pady=10, sticky="n")  # Position below the logo

        # Center the button horizontally
        self.window.grid_columnconfigure(0, weight=1)

    def start_setup(self):
        # Your setup code here
        pass

# Create the main window
window = tk.Tk()
window.title("Java Installer")
window.geometry("900x500")
window.resizable(False, False)

# Create and show the ZeroScene
zero_scene = ZeroScene(window)
zero_scene.show()

# Start the Tkinter event loop
window.mainloop()
