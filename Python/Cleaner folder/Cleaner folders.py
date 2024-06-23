import os
import shutil

def delete_files(folder, exclude_files=None):
    files = os.listdir(folder)

    for file in files:
        file_path = os.path.join(folder, file)
        try:
            if exclude_files and file in exclude_files:
                print(f"Skipped: {file}")
                # This file is in the exclude list, so it will not be deleted
            elif file.endswith(('.rblx', '.obj', '.blend', '.mp3', '.mp4', '.zip')):
                print(f"Skipped: {file} (ends with .rblx, .obj, .blend, .mp3, .mp4, or .zip)")
                # This file has a protected extension, so it will not be deleted
            elif os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted: {file}")
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                print(f"Deleted directory: {file}")
        except PermissionError:
            print(f"Permission denied: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

if __name__ == "__main__":
    # Specify the path to the Downloads folder
    downloads_folder = os.path.expanduser('~/Downloads')

    # List of files to exclude from deletion
    exclude_files = ["AutoClicker-3.0.exe"]

    delete_files(downloads_folder, exclude_files)
