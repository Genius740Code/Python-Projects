import os
import zipfile
import shutil

def extract_and_delete_zip_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".zip"):
                zip_file_path = os.path.join(root, file)
                extract_path = os.path.splitext(zip_file_path)[0]
                
                with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_path)
                
                print(f"Extracted: {zip_file_path} to {extract_path}")
                
                # Delete the zip file
                os.remove(zip_file_path)
                
                print(f"Deleted: {zip_file_path}")

if __name__ == "__main__":
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads") # Path to downloads
    extract_and_delete_zip_files(downloads_path)
