import tkinter as tk
from tkinter import messagebox
from src.modules.checkupdates import check_for_updates
from config import CURRENT_VERSION
from src.scenes.zero_scene import zero_scene
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
            repo_url = "https://api.github.com/repos/Wonkiest29/preinstaller/releases/latest"
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
        create_config_file(file_path)
        print(f"Config file created: {file_path}")
    
    window = tk.Tk()
    window.title("Java Installer")
    window.geometry("900x500")
    window.resizable(False, False)
    
    icon_path = os.path.join("src", "images", "icon.ico")
    if os.path.exists(icon_path):
        window.iconbitmap(icon_path)
    else:
        print(f"Icon file not found: {icon_path}")
    
    
    # Start the Tkinter event loop
    window.mainloop()

# Call the main function to start the application
if __name__ == "__main__":
    main()
