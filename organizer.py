# organizer.py

import os
import shutil
import sys
import time

# --- CONFIGURATION ---
# Check if a folder path was provided when running the script
if len(sys.argv) > 1:
    # The first argument after the script name is our target folder
    TARGET_FOLDER = sys.argv[1]
else:
    # If no folder is provided, print an error and exit
    print("Error: Please provide the folder path as a command-line argument.")
    sys.exit(1)

# This dictionary maps file extensions to the folder they should be moved to.
# You can easily add more file types and folders here!
FILE_TYPES = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".zip": "Archives",
    ".rar": "Archives",
    ".mp3": "Music",
    ".wav": "Music",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".js": "Scripts",
    ".py": "Scripts",
}

# --- SCRIPT LOGIC ---

print(f"Starting file organizer for folder: {TARGET_FOLDER}")
print("Press CTRL+C to stop the script.")

try:
    # This creates an infinite loop to continuously watch the folder
    while True:
        # Get a list of all items in the target folder
        with os.scandir(TARGET_FOLDER) as entries:
            for entry in entries:
                # Check if it is a file and not a directory
                if entry.is_file():
                    # Get the file extension in lowercase
                    file_ext = os.path.splitext(entry.name)[1].lower()

                    # Check if the file extension is in our FILE_TYPES mapping
                    if file_ext in FILE_TYPES:
                        # Get the destination folder name from the mapping
                        dest_folder_name = FILE_TYPES[file_ext]

                        # Construct the full path of the destination folder
                        dest_folder_path = os.path.join(TARGET_FOLDER, dest_folder_name)

                        # Create the destination folder if it doesn't already exist
                        os.makedirs(dest_folder_path, exist_ok=True)

                        # Construct the full path for the destination file
                        dest_path = os.path.join(dest_folder_path, entry.name)

                        # Move the file from the source to the destination
                        shutil.move(entry.path, dest_path)

                        print(f"Moved: {entry.name} -> {dest_folder_name}/")

        # Wait for 10 seconds before checking the folder again to save CPU
        time.sleep(10)

except KeyboardInterrupt:
    print("\nFile organizer stopped by user.")
except FileNotFoundError:
    print(f"Error: The folder '{TARGET_FOLDER}' does not exist. Please check the path.")
