import kagglehub
import os
import shutil

# Download latest version
path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")

destination_path = './Data'

# Ensure the destination directory exists, or create it if it doesn't
if not os.path.exists(destination_path):
    os.makedirs(destination_path)

# Move the directory
try:
    shutil.move(path, destination_path)
    print(f"Successfully moved '{path}' to '{destination_path}'.")
except FileNotFoundError:
    print(f"Error: The source directory '{path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
