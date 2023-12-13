import os
import shutil

# Define the source and destination directories
downloads_dir = os.path.expanduser("~/Downloads")
photos_dir = os.path.join(downloads_dir, "fotos")

# Create the 'fotos' directory if it doesn't exist
os.makedirs(photos_dir, exist_ok=True)

# List all files in the Downloads directory
files = os.listdir(downloads_dir)

# Filter files based on extensions
image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Move image files to the 'fotos' directory
for image_file in image_files:
    source_path = os.path.join(downloads_dir, image_file)
    destination_path = os.path.join(photos_dir, image_file)
    shutil.move(source_path, destination_path)

print("Files have been organized. Check the 'fotos' folder in your Downloads directory.")
