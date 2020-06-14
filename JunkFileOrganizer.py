import os
import shutil
import sys
import os.path
import time
import json
from datetime import datetime

with open('file_types.json') as file:
    file_types = json.load(file)

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


# print()

if __name__ == '__main__':

    # Taking the input from Command line using Command line parsing.

    option = sys.argv[1]

if option == 'ext':
    byExtension()
elif option == 'date':
    bydate()
elif option == 'size':
    bysize()
