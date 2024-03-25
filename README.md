# Files Organizer
![image](https://github.com/dynstat/files_organizer/assets/38962239/2846d128-e3a6-4fd1-8a37-bc95aa15e643)

**WARNING !!!** 
Do not test it on your important folders and files, it is just a simple FUN project for making desktop GUI apps in python and it is still in the development phase.

Files Organizer is a small, cross-platform GUI application developed in Python. It's designed to help you manage cluttered folders by automatically organizing files into categorized subfolders based on their file types. This tool is especially useful for tidying up commonly cluttered spaces like your downloads folder.

## Features

- **Automatic Organization**: Sorts files into subfolders based on file extensions.
- **Custom Destination Folder**: Optionally specify a different destination folder for the organized files.
- **De-Organization**: Revert the organization process, moving files back to their original location.
- **Simple Interface**: Simple and intuitive graphical user interface for ease of use.
- **Support for Various File Types**: Works with documents, audio files, images, videos, software installers, and compressed files. Adding Custom file types, feature will be added soon.

## How to Use

1. **Launch the Application**: Open the Files Organizer application.
2. **Select the Source Folder**: Use the "Browse" button next to the "Folder to organize" field to choose the folder you want to organize.
3. **(Optional) Select Destination Folder**: Use the "Browse" button next to the "Destination folder" field to choose a different destination folder. If left unchanged, the source folder will be used.
4. **Organize**: Click the "ORGANIZE" button to start organizing your files into subfolders.
5. **De-Organize (Optional)**: To revert the organization, click the "DE-ORGANIZE" button. This will move the files back to the source folder.

## Installation from binaries
 - **Windows**: [Download PyFileOrganizer.exe](https://github.com/dynstat/files_organizer/releases/download/Beta/PyFileOrganizer.exe)

## Installation from source code

Ensure you have Python 3.6 or higher installed on your system. Follow these steps to set up Files Organizer:

1. Clone the repository or download the source code.
2. Install the required Python libraries by running `pip install flet` in your terminal.
3. Navigate to the application directory and run `python start_app.py` to launch the application.

## System Requirements for building from source

- Operating System: Windows, macOS, or Linux
- Python 3.6 or higher
- Required Python libraries: `flet`

## Caution

This application is currently in development. Please avoid using it on important folders and files to prevent unintended file movements. Back up your data before using the application.

