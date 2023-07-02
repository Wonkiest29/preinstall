import tkinter as tk
from tkinter import messagebox
import subprocess
import json
import platform
import requests

class WindowsSetup:
    def __init__(self, parent, start_callback):
        self.parent = parent
        self.frame = tk.Frame(parent)
        self.step_label = None
        self.remove_java_var = None
        self.java_version_var = None
        self.install_button = None
        self.java_info = None  # Instance variable for storing Java installation information
        self.start_callback = start_callback

    def show(self):
        self.frame.pack()

        # Create step label
        self.step_label = tk.Label(self.frame)
        self.step_label.pack()

        # Create remove Java checkbox
        self.remove_java_var = tk.BooleanVar()
        remove_java_checkbox = tk.Checkbutton(self.frame, text="Remove old Java", variable=self.remove_java_var)
        remove_java_checkbox.pack()

        # Load the Java installation information from the remote JSON file
        try:
            url = "https://raw.githubusercontent.com/Wonkiest29/preinstaller/main/docx/java.json"
            response = requests.get(url)
            if response.status_code == 200:
                self.java_info = response.json()
            else:
                messagebox.showerror("JSON Error", "Failed to fetch the Java installation information from the JSON file.")
                return
        except requests.exceptions.RequestException:
            messagebox.showerror("Network Error", "Failed to fetch the Java installation information. Please check your internet connection.")
            return

        # Filter Java options based on the current operating system
        current_os = platform.system()
        filtered_java_info = {version: data for version, data in self.java_info.items() if data.get("os") == current_os}

        # Create Java version selection dynamically based on available versions
        self.java_version_var = tk.StringVar()
        default_version = None

        for version, data in filtered_java_info.items():
            java_name = data.get("name")
            tk.Radiobutton(self.frame, text=java_name, variable=self.java_version_var, value=version).pack()

            # Set the default selection based on the first version
            if default_version is None:
                default_version = version

        self.java_version_var.set(default_version)  # Set the default selection

        # Create Install button
        self.install_button = tk.Button(self.frame, text="Install", command=self.install_java)
        self.install_button.pack()

    def hide(self):
        self.frame.pack_forget()

    def install_java(self):
        remove_java = self.remove_java_var.get()
        java_version = self.java_version_var.get()

        # Fetch the URL based on the selected Java version
        try:
            url = self.java_info.get(java_version, {}).get("link")
            if not url:
                messagebox.showerror("URL Not Found", "Failed to find the URL for the selected Java version.")
                return
        except AttributeError:
            messagebox.showerror("Java Info Error", "Java installation information is missing.")
            return

        # Perform OS-dependent operations only for Windows
        if platform.system() == "Windows":
            # Perform Windows-specific installation

            # Download the Java installer file
            try:
                subprocess.run(["powershell", "-Command", f"(New-Object System.Net.WebClient).DownloadFile('{url}', 'java_installer.msi')"])
            except subprocess.CalledProcessError:
                messagebox.showerror("Download Error", "Failed to download the Java installer.")
                return

            # Silent installation command
            install_command = "msiexec /i java_installer.msi /qn"

            # Run the installation command silently
            try:
                subprocess.run(["powershell", "-Command", install_command], shell=True)
            except subprocess.CalledProcessError:
                messagebox.showerror("Installation Error", "Failed to install Java.")
                return

        # After the installation, execute the start callback function
        self.start_callback()
