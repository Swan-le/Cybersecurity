import shutil
import os
from datetime import datetime
import zipfile

# script configuration
source_dir = "/Users/noahschaik/Desktop" # Location/folder that we are backing up
backup_base_dir = "/Users/noahschaik/Downloads" # Location where backup will live.

# Creates timestamp config: YYYYMMDD_HHMMSS
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Creates the timestamped backup folder
backup_dir = os.path.join(backup_base_dir, f"backup_{timestamp}")

# Create the timestamped backup folder
os.makedirs(backup_dir, exist_ok=True)

# Copy the entire source directory
shutil.copytree(source_dir, os.path.join(backup_dir, os.path.basename(source_dir)))

#Create a compressed Zip archive
zip_filename = os.path.join(backup_base_dir, f"backup_{timestamp}.zip")
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            full_path = os.path.join(root, file)
            arcname = os.path.relpath(full_path, source_dir)
            zipf.write(full_path, arcname)

print(f"Backup completed: {zip_filename or backup_dir}")
