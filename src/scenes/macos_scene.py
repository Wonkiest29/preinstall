import tkinter as tk

class MacOSScene:
    def __init__(self, window):
        self.window = window
        self.step1_label = None
        self.step2_label = None
        self.step3_label = None

    def show(self):
        # Create labels for each step
        self.step1_label = tk.Label(self.window, text="Step 1: Remove old Java")
        self.step2_label = tk.Label(self.window, text="Step 2: Choose Java version")
        self.step3_label = tk.Label(self.window, text="Step 3: Install Java")

        # Grid layout to position the labels
        self.step1_label.grid(row=0, column=0, padx=10, pady=10)
        self.step2_label.grid(row=1, column=0, padx=10, pady=10)
        self.step3_label.grid(row=2, column=0, padx=10, pady=10)
