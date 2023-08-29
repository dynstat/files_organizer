import os
import shutil
from pathlib import Path
from time import sleep


def organize_folder(source_folder, new_dest_folder_path=None):
    try:
        if not new_dest_folder_path:
            # using the same location as the destination folder, i.e. organize in place
            destination_folder = os.path.abspath(source_folder)
        else:
            # Create the destination folder in the same directory as the source folder, if asked
            destination_folder = os.path.join(os.path.abspath(new_dest_folder_path))
            Path(destination_folder).mkdir(parents=True, exist_ok=True)

        # Mapping of folder names to lists of extension names
        folder_extensions = {
            "docs": [
                "pdf",
                "txt",
                "doc",
                "docx",
            ],
            "audio": ["mp3", "aac"],
            "imgs": ["jpg", "jpeg", "png"],
            "video": ["mp4", "avi"],
            "soft": ["exe", "msi"],
            "compressed": ["zip", "rar", "7zip"]
            # Add more folder and extension combinations as needed
        }

        # Iterate through files in the source folder
        for filename in os.listdir(source_folder):
            source_path = os.path.join(source_folder, filename)
            if os.path.isfile(source_path):
                extension = filename.split(".")[-1].lower()

                # Find the target folder based on the extension
                target_folder = None
                for folder, extensions in folder_extensions.items():
                    if extension in extensions:
                        target_folder = folder
                        break
                if not target_folder:
                    continue  # if uncommented, and if the filetype used is not in the expected extension list, it will be ignored
                    target_folder = "other"

                target_folder_path = os.path.join(destination_folder, target_folder)

                # Create the target folder if it doesn't exist
                Path(target_folder_path).mkdir(parents=True, exist_ok=True)

                target_path = os.path.join(target_folder_path, filename)

                # Handle existing target files by appending a number
                base_name, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(target_path):
                    target_path = os.path.join(
                        target_folder_path, f"{base_name}_{counter}{ext}"
                    )
                    counter += 1

                # Move the file to the target folder
                shutil.move(source_path, target_path)
                # sleep(10)

    except Exception as e:
        print(f"An error occurred: {e}")


def move_back_to_source(organized_folder, to_folder=None):
    try:
        if not to_folder:
            source_folder = os.path.join(os.path.abspath(organized_folder))
        else:
            source_folder = os.path.join(os.path.abspath(organized_folder), to_folder)
        # Create the source folder if it doesn't exist
        Path(source_folder).mkdir(parents=True, exist_ok=True)

        # Iterate through organized folders
        for folder_name in os.listdir(organized_folder):
            folder_path = os.path.join(organized_folder, folder_name)
            if os.path.isdir(folder_path):
                for filename in os.listdir(folder_path):
                    source_path = os.path.join(folder_path, filename)
                    target_path = os.path.join(source_folder, filename)

                    # Handle existing target files by appending a number
                    base_name, ext = os.path.splitext(filename)
                    counter = 1
                    while os.path.exists(target_path):
                        target_path = os.path.join(
                            source_folder, f"{base_name}_{counter}{ext}"
                        )
                        counter += 1

                    # Move the file back to the source folder
                    shutil.move(source_path, target_path)

        # # Remove the organized_files directory
        # shutil.rmtree(organized_folder)

    except Exception as e:
        print(f"An error occurred: {e}")


# just for testing
if __name__ == "__main__":
    source_folder = "testingfolder"

    # Organize files to the destination folder
    # organize_folder(source_folder)
    # print("Files organized successfully.")

    organized_folder = os.path.join(os.path.abspath(source_folder))
    print(organized_folder)
    # Move files back to the source folder
    move_back_to_source(organized_folder)
    print("Files moved back to source folder.")
