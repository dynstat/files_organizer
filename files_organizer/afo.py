import hashlib
import os
import shutil
from pathlib import Path
import logging
from time import sleep

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def file_hash(filepath):
    """Compute the SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def get_unique_filename(target_path, source_path):
    """Generates a unique filename to avoid overwriting existing files with different content."""
    if os.path.exists(target_path) and file_hash(target_path) != file_hash(source_path):
        base_name, ext = os.path.splitext(target_path)
        counter = 1
        while os.path.exists(target_path) and file_hash(target_path) != file_hash(
            source_path
        ):
            target_path = f"{base_name}_{counter}{ext}"
            counter += 1
    return target_path


def organize_files_by_extension(source_folder, destination_folder, folder_extensions):
    """Organizes files from the source folder into subfolders in the destination folder based on file extensions."""
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)
        if os.path.isfile(source_path):
            extension = os.path.splitext(filename)[1][1:].lower()
            target_folder = next(
                (
                    folder
                    for folder, extensions in folder_extensions.items()
                    if extension in extensions
                ),
                None,
            )
            if not target_folder:
                continue
            target_folder_path = Path(destination_folder, target_folder)
            target_folder_path.mkdir(parents=True, exist_ok=True)

            target_path = target_folder_path.joinpath(filename)
            # Adjusted to pass the source_path for compatibility with the updated get_unique_filename
            unique_target_path = get_unique_filename(target_path, source_path)
            shutil.copy(source_path, unique_target_path)


def move_files_back_to_source(organized_folder, source_folder):
    """Moves files from their organized subfolders back to the source folder."""
    for folder_name in os.listdir(organized_folder):
        folder_path = Path(organized_folder, folder_name)
        if folder_path.is_dir():
            for filename in folder_path.iterdir():
                target_path = Path(source_folder).joinpath(filename.name)
                unique_target_path = get_unique_filename(target_path, filename)
                shutil.move(str(filename), unique_target_path)
            # Remove the folder if it's empty
            if not any(folder_path.iterdir()):
                folder_path.rmdir()


def organize_folder(source_folder, new_dest_folder_path=None):
    """Main function to organize files in a folder."""
    try:
        destination_folder = new_dest_folder_path or source_folder
        Path(destination_folder).mkdir(parents=True, exist_ok=True)

        folder_extensions = {
            "docs": ["pdf", "txt", "doc", "docx"],
            "audio": ["mp3", "aac"],
            "imgs": ["jpg", "jpeg", "png"],
            "video": ["mp4", "avi"],
            "soft": ["exe", "msi"],
            "compressed": ["zip", "rar", "7zip"],
        }

        organize_files_by_extension(
            source_folder, destination_folder, folder_extensions
        )
    except Exception as e:
        logging.error(f"An error occurred while organizing files: {e}")


def move_back_to_source(organized_folder, to_folder=None):
    """Moves files back to the source folder from their organized subfolders."""
    try:
        source_folder = to_folder or organized_folder
        Path(source_folder).mkdir(parents=True, exist_ok=True)

        move_files_back_to_source(organized_folder, source_folder)
    except Exception as e:
        logging.error(f"An error occurred while moving files back: {e}")


if __name__ == "__main__":
    try:
        source_folder = "testingfolder"
        organized_folder = Path(source_folder).resolve()
        logging.info(f"Organized folder: {organized_folder}")

        # Uncomment the next line to organize files
        organize_folder(source_folder)

        # sleep(20)
        # Move files back to the source folder
        move_back_to_source(str(organized_folder))
        logging.info("Files moved back to source folder.")
    except Exception as e:
        logging.error(f"An error occurred in the main block: {e}")
