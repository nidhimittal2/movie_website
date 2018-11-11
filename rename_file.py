import os
def rename_file():
    #get file name for a folder
    file_list = os.listdir(r"/home/nidhi/Desktop/prank")
    #get current working directory
    saved_path = os.getcwd()
    os.chdir(r"/home/nidhi/Desktop/prank")
    #for each file rename file_list
    for file_name in file_list:
        print("Old name- "+file_name)
        print("New name- "+file_name.translate(None,"0123456789"))
        os.rename(file_name,file_name.translate(None,"0123456789"))

        os.chdir(saved_path)

rename_file()
