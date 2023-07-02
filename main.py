import tkinter as tk
from tkinter import messagebox
from src.scenes.zero_scene import ZeroScene
from src.modules.checkupdates import check_for_updates
from config import CURRENT_VERSION
import os
import json

def show_update_message(latest_version):
    messagebox.showinfo("Update Available", f"A new version ({latest_version}) is available. Click OK to download it.")

def create_config_file(file_path):
    # Define the data to be written to the JSON file
    config_data = {
        "check_updates": True
    }

    try:
        # Open the file in write mode
        with open(file_path, "w") as file:
            # Write the JSON data to the file
            json.dump(config_data, file, indent=4)

        print(f"Config file created successfully: {file_path}")
    except IOError:
        print(f"Failed to create config file: {file_path}")

def main():
    # Check if the config file exists
    file_path = "config.json"
    if os.path.exists(file_path):
        # The config file exists, read the configuration
        with open(file_path, "r") as file:
            config_data = json.load(file)

        # Check if update checks are enabled
        check_updates = config_data.get("check_updates", False)
        if check_updates:
            # Perform the update check
            repo_url = "https://api.github.com/Wonkiest29/preinstaller/releases/latest"
            latest_version = check_for_updates(repo_url)

            if latest_version:
                latest_version_number = latest_version.get("tag_name", "")
                if latest_version_number > CURRENT_VERSION:
                    show_update_message(latest_version_number)
                else:
                    print("No updates available.")
            else:
                print("Failed to check for updates.")
        else:
            print("Update checks are disabled.")
    else:
        # The config file does not exist, create it
        create_config_file(file_path)
        print(f"Config file created: {file_path}")

    # Create the main window
    window = tk.Tk()
    window.title("Java Installer")
    window.geometry("300x250")
    window.resizable(False, False)

    # Create a frame to hold the scenes
    scene_frame = tk.Frame(window)
    scene_frame.pack()

    # Create and show the initial scene (ZeroScene)
    zero_scene_instance = ZeroScene(window, scene_frame)
    zero_scene_instance.show()

    # Start the main event loop
    window.mainloop()

# Call the main function to start the application
if __name__ == "__main__":
    main()
