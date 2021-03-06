import os
import shutil

# cwd = os.getcwd()
# src_path = cwd
# Paths to be set manually
text_path = "C:/Users/vivek/Downloads/def_fldr/textwala"
video_path = "C:/Users/vivek/Downloads/def_fldr/videowala"
img_path = "C:/Users/vivek/Downloads/def_fldr/imgwala"
app_setup_path = "C:/Users/vivek/Downloads/def_fldr/softfileswala"
docs_path = "C:/Users/vivek/Downloads/def_fldr/docswala"
audio_path = "C:/Users/vivek/Downloads/def_fldr/audiowala"

docs_extensions = {'pdf', 'doc', 'docx', 'ppt', 'PDF', 'PPT'}
audio_extensions = {'mp3', 'aac', 'flac', 'wav'}
video_extensions = {'mp4', 'mkv', '3gp', 'gif'}
img_extensions = {'jpg', 'jpeg', 'png'}
app_setup_extensions = {'exe', 'zip', 'rar', 'apk', 'msi', '7z'}
text_extensions = {'txt'}


def filemover(ext, item, from_folder):

    if ext != "folder":
        if ext in audio_extensions:
            shutil.move(f'{from_folder}\\\\{item}', audio_path)
            # print(ext)
        elif ext in video_extensions:
            shutil.move(f'{from_folder}\\\\{item}', video_path)
            # print(ext)
        elif ext in docs_extensions:
            shutil.move(f'{from_folder}\\\\{item}', docs_path)

        elif ext in img_extensions:
            shutil.move(f'{from_folder}\\\\{item}', img_path)

        elif ext in app_setup_extensions:
            shutil.move(f'{from_folder}\\\\{item}', app_setup_path)

        elif ext in text_extensions:
            shutil.move(f'{from_folder}\\\\{item}', text_path)


def filecopy(ext, item, from_folder):

    if ext != "folder":
        if ext in audio_extensions:
            shutil.copy(f'{from_folder}\\\\{item}', audio_path)
            # print(f"ext = {ext} and path = {r}")
        elif ext in video_extensions:
            shutil.copy(f'{from_folder}\\\\{item}', video_path)
            # print(ext)
        elif ext in docs_extensions:
            shutil.copy(f'{from_folder}\\\\{item}', docs_path)
            # print("docs  = ", ext, '\n')
        elif ext in img_extensions:
            shutil.copy(f'{from_folder}\\\\{item}', img_path)

        elif ext in app_setup_extensions:
            shutil.copy(f'{from_folder}\\\\{item}', app_setup_path)

        elif ext in text_extensions:
            shutil.copy(f'{from_folder}\\\\{item}', text_path)


def extenChecker(abs_path):
    counter = 0
    rev_path = abs_path[::-1]
    for ch in rev_path:
        if ch != '.':
            counter += 1
        else:
            break
    if counter < 5:
        return rev_path[:counter:1][::-1]
    else:
        return "folder"
