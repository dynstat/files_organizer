import os
# import shutil
import filehandler_funcs as func
import time


func.app_setup_path = "C:/Users/vivek/Desktop/soft"
func.text_path = "C:/Users/vivek/Desktop/text"
func.audio_path = "C:/Users/vivek/Desktop/audio"


print("Have you set the paths of each destination folder ? (y/n)")
if input() != 'y' and 'Y':
    print("Please set the paths first, Exiting.....!!! ")
    time.sleep(1)
    exit()


while True:
    cwd = os.getcwd()   # to get the current working directory
    # returns a list of all the folders and files name
    # print(cwd)  # C:\Users\vivek\Downloads\def_fldr\prjfilehlr
    BASE_FOLDER = os.path.dirname(cwd)
    list_of_files = os.listdir(BASE_FOLDER)

    for item in list_of_files:
        # abs_item_path = f"{cwd}/{item}"

        ext = func.extenChecker(item)
        i# print("item = ", item)  #name of file or folder
        # print(f"ext = {ext}")   #its extension or folder
        try:
            func.filecopy(ext, item, BASE_FOLDER)
        except Exception as e:
        print("Oops!", e.__class__, "occurred")
    
    time.sleep(2)
    # movedToPath = func.filemover(ext)
    # print(f"file is successfuly moved to {movedToPath}")


# shutil.copy(src=BASE_FOLDER+r"\\"+item, dst=func.mp3_path)
# shutil.copy(src=BASE_FOLDER+r"\\"+list_of_files[1], dst=func.mp3_path)
