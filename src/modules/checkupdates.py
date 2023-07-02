import requests
import json
from config import CURRENT_VERSION
def check_for_updates(repo_url):
    response = requests.get(repo_url)
    try:
        latest_release = response.json()
    except json.JSONDecodeError:
        print("Error: Failed to parse JSON response. Invalid data received.")
        return None
    return latest_release

def perform_update_check():
    repo_url = "https://api.github.com/repos/Wonkiest29/preinstaller/releases/latest"
    latest_version = check_for_updates(repo_url)
    return latest_version
