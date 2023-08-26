import os
import shutil
from pathlib import Path


def organize_files(source_folder):
    try:
        # Create the destination folder in the same directory as the source folder
        destination_folder = os.path.join(
            os.path.dirname(source_folder), "organized_files"
        )
        Path(destination_folder).mkdir(parents=True, exist_ok=True)

        # Mapping of folder names to lists of extension names
        folder_extensions = {
            "docs": ["pdf", "txt"],
            "audio": ["mp3"],
            "imgs": ["jpg", "jpeg"],
            "video": ["mp4"],
            "soft": ["exe"],
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

    except Exception as e:
        print(f"An error occurred: {e}")


def move_back_to_source(destination_folder, to_folder):
    try:
        source_folder = os.path.join(os.path.dirname(destination_folder), to_folder)

        # Create the source folder if it doesn't exist
        Path(source_folder).mkdir(parents=True, exist_ok=True)

        # Iterate through organized folders
        for folder_name in os.listdir(destination_folder):
            folder_path = os.path.join(destination_folder, folder_name)
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

        # Remove the organized_files directory
        shutil.rmtree(destination_folder)

    except Exception as e:
        print(f"An error occurred: {e}")


# just for testing
if __name__ == "__main__":
    source_folder = "testfolder"

    # Organize files to the destination folder
    organize_files(source_folder)
    print("Files organized successfully.")

    # destination_folder = os.path.join(os.path.dirname(source_folder), "organized_files")
    # print(destination_folder)
    # # Move files back to the source folder
    # move_back_to_source(destination_folder, to_folder=source_folder)
    # print("Files moved back to source folder.")
