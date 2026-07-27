import os
import shutil

# ===== CONFIGURATION =====

# Folder that will be organized
TARGET_DIR = "C:\\Users\\DELL\\OneDrive\\Desktop\\New folder"   # change this path if needed

# File type categories with their extensions
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"]
}

# ===== FILE ORGANIZER LOGIC =====

# Loop through all items in the target directory
for filename in os.listdir(TARGET_DIR):

    # Create full path of the item
    file_path = os.path.join(TARGET_DIR, filename)

    # Skip directories, only process files
    if not os.path.isfile(file_path):
        continue

    # Separate file name and extension
    _, ext = os.path.splitext(filename)
    ext = ext.lower()   # normalize extension for matching

    moved = False  # flag to track if file was categorized

    # Check each category and its extensions
    for folder, extensions in FILE_TYPES.items():
        if ext in extensions:

            # Create destination folder if it does not exist
            dest_folder = os.path.join(TARGET_DIR, folder)
            os.makedirs(dest_folder, exist_ok=True)

            # Move the file into the category folder
            shutil.move(file_path, dest_folder)

            moved = True
            break

    # If file type does not match any category
    if not moved:
        other_folder = os.path.join(TARGET_DIR, "Others")
        os.makedirs(other_folder, exist_ok=True)
        shutil.move(file_path, other_folder)

print("Files organized successfully.")
