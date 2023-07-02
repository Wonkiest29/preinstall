import tkinter as tk
from src.scenes.windows_scene import WindowsSetup

class ZeroScene:
    def __init__(self, window, scene_frame):
        self.window = window
        self.scene_frame = scene_frame
        self.start_button = None
        self.button_frame = None

    def show(self):
        # Create a label at the top
        title_label = tk.Label(self.scene_frame, text="Java Installation Assistant", font=("Arial", 16))
        title_label.pack(pady=20)

        # Create a frame to hold the button and text
        self.button_frame = tk.Frame(self.scene_frame)
        self.button_frame.pack()

        # Create the start button
        self.start_button = tk.Button(self.button_frame, text="Start", command=self.start)
        self.start_button.pack(pady=10)

        # Create the text label
        text_label = tk.Label(self.button_frame, text="Click the 'Start' button to begin the installation process.")
        text_label.pack(pady=10)

        self.window.geometry("300x250")

    def start(self):
        # Destroy the button frame along with its widgets
        self.button_frame.destroy()
        # Disable the button while processing
        self.window.update()  # Update the window to reflect the button text change
        windows_scene = WindowsSetup(self.window, self.show)  # Pass self.show as the start_callback
        windows_scene.show()