import requests
import os

# --- CONFIGURATION ---
REPO_OWNER = "victoriastreder"
REPO_NAME = "Coastal-Wetland-NGGI-Data-Public"
FOLDER_PATH = "2-NGGI Data Sets/Set-105"
# Updated path to save in data/raw
SAVE_FOLDER = os.path.join("data", "raw") 

def download_github_folder():
    # Create the directory structure data/raw
    if not os.path.exists(SAVE_FOLDER):
        print(f"Creating directory: {SAVE_FOLDER}")
        os.makedirs(SAVE_FOLDER, exist_ok=True)

    # API endpoint to get folder contents
    api_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{FOLDER_PATH}"

    try:
        print(f"Connecting to GitHub API for: {FOLDER_PATH}...")
        response = requests.get(api_url)
        response.raise_for_status()
        contents = response.json()
        
        # Iterate through the items in the folder
        for item in contents:
            if item['type'] == 'file':
                filename = item['name']
                download_url = item['download_url']

                print(f"Downloading {filename}...", end=" ")

                # Stream the download for efficiency
                with requests.get(download_url, stream=True) as r:
                    r.raise_for_status()
                    file_path = os.path.join(SAVE_FOLDER, filename)
                    with open(file_path, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            f.write(chunk)
                print("Done ✅")
            elif item['type'] == 'dir':
                print(f"Skipping sub-directory: {item['name']}")
        
        print(f"\nSuccess! All files from '{FOLDER_PATH}' have been saved to: {SAVE_FOLDER}")

    except requests.exceptions.RequestException as e:
        print(f"Error accessing GitHub: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Execute the downloader
download_github_folder()