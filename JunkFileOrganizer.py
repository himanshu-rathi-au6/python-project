import os
import shutil
import os.path
import time
from datetime import datetime

# this function is used to organize files by extension


def byExtension():

    path = input("Enter Your directory Path :- ")
    name = os.listdir(path)
    name.sort(key=lambda x: os.stat(os.path.join(path, x)).st_mtime)

    # List only the files in the folder

    [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    # change the current path

    os.chdir(path)
    dir = os.listdir()

    file_types = {
        "Images": [".png", ".jpeg", ".jpg", ".gif", ".bmp", "svg"],
        "Text": [".txt", ".wps", ".docx"],
        "Documents": [".doc", ".ppt", ".csv", ".pptx", ".xml"],
        "Audio": [".mp3", ".m4a"],
        "Video": [".mp4", ".avi",  ".wmv", ".m4v", ".mov", ".mpg", ".flv"],
        "Notes": [".pdf"],
        "Apps": [".apk", ".exe ", ".jar"],
        "Code": [".js", ".css", ".html", ".php", ".sass"],
        "Compressed": [".zip", ".rar"],
        "Program": [".c", ".cpp", ".ruby", ".rust", ".java"],
        "Python": [".py"],
        "Shell": [".sh"]
    }

    for x in dir:
        fileflag = 0
        if os.path.isfile(x):
            if("." in x):
                Ext_Name = x[x.index("."):]
                for file_type, extensions in file_types.items():
                    if Ext_Name in extensions:
                        fileflag = 1
                        folderName = file_type
                        dest_path = path + '/' + folderName
                        print(dest_path)

                        break

                if (fileflag == 0):
                    folder_name = "Extra"
                    dest_path = path + '/' + folder_name
                    print(dest_path)

            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            shutil.move(path + '/' + x, dest_path + '/' + x)

# this function is used to organize by date


def bydate():

    path = input("Enter Your directory Path :-")
    name = os.listdir(path)
    name.sort(key=lambda x: os.stat(os.path.join(path, x)).st_mtime)
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path,
             f))]

    os.chdir(path)

    for x in files:

        # Get the creation time

        create_time = time.ctime(os.path.getmtime(os.path.join(path, x)))
        create_dt = datetime.strptime(create_time, '%a %b %d %H:%M:%S %Y')
        modified_date = str(create_dt.day) + '-' + str(
                        create_dt.month) + '-' + str(create_dt.year)

        if(os.path.isdir(modified_date)):
            shutil.move(os.path.join(path, x), modified_date)

        else:

            os.makedirs(modified_date)
            shutil.move(os.path.join(path, x), modified_date)

# this function is used to know the size


def bysize():

    path = input("Enter your directory path:-")
    size = 0
    fileSize = {'Bytes': 1, 'Kilobytes': float(1)/1024,
                'Megabytes': float(1)/(1024*1024),
                'Gigabytes': float(1)/(1024*1024*1024)}

    for (path, dirs, files) in os.walk(path):

        for file in files:
            filename = os.path.join(path, file)
            size += os.path.getsize(filename)

    for key in fileSize:

        print("File Size: " + str(round(fileSize[key]*size, 2)) + " " + key)

# this function is used to count the files


print(""" 1 FOR TO ORGANIZE FILE BY EXTENSION

 2 FOR TO ORGANIZE BY DATE

 3 THE SIZE OF FILES IN YOUR DIRECTORY""")

option = int(input("SELECT YOUR OPTION :- "))

if option == 1:
    byExtension()
elif option == 2:
    bydate()
elif option == 3:
    bysize()
