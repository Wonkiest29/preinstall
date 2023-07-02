import json
import platform

def get_java_info():
    # Load the JSON file
    try:
        with open('java_info.json') as file:
            data = json.load(file)
    except FileNotFoundError:
        return None
    
    # Get the current operating system
    current_os = platform.system().lower()
    
    # Check if the operating system is supported in the JSON data
    if current_os in data:
        return [data[key] for key in data if data[key]["os"].lower() == current_os]
    else:
        return None
