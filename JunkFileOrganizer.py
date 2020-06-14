import argparse
import os
import shutil
from datetime import datetime
import time
from stat import ST_SIZE


def main():
    parameter = argparse.ArgumentParser()

    # To get the path and options from the command line.

    parameter.add_argument('--path', default='.', help='path to organize')
    parameter.add_argument('-o', default='ext', help='Organize by',
                           choices=['ext', 'size', 'date', 'count'])

    args = parameter.parse_args()
    organize(args)

# recursively list out all the files.


file_Data = []


def get_Data(path):
    for file in os.scandir(path):
        if not file.is_dir():
            fileName = file.name
            filePath = file.path
            fileExtension = fileName.split('.')[-1]
            fileSize = os.stat(filePath)[ST_SIZE]
            file_Data.append([fileName, filePath, fileExtension, fileSize])
        else:
            file_Data + [data for data in (get_Data(file.path))]

    return file_Data

# This function arrange the files by their extension


def byExtension(path, Data, organizedPath):
    for data in Data:
        fileName = data[0]
        filePath = data[1]
        extension = data[2]

        if not os.path.exists(organizedPath + extension):
            os.makedirs(organizedPath + extension)

        shutil.move(filePath, organizedPath + extension + '/' + fileName)

# This function arrange the files by their size


def bySize(path, Data, organizedPath):
    for data in Data:
        fileName = data[0]
        filePath = data[1]
        size = data[3]

        if 0 <= size < 1000:  # bytes
            if not os.path.exists(organizedPath + 'BYTES'):
                os.makedirs(organizedPath + 'BYTES')

            shutil.move(filePath, organizedPath + 'BYTES/' + fileName)

        elif 1000 < size < 1000000:  # KiloBytes
            if not os.path.exists(organizedPath + 'KB'):
                os.makedirs(organizedPath + 'KB')

            shutil.move(filePath, organizedPath + 'KB/' + fileName)

        elif 1000000 < size < 100000000:  # MegaBytes
            if not os.path.exists(organizedPath + 'MB'):
                os.makedirs(organizedPath + 'MB')

            shutil.move(filePath, organizedPath + 'MB/' + fileName)

        # If any file more than 100 MB
        else:
            if not os.path.exists(organizedPath + 'more than MB'):
                os.makedirs(organizedPath + 'more than MB')

            shutil.move(filePath, organizedPath + 'more than MB/' +
                        fileName)

# This function arrange the files by their last used date


def bydate(path, Data, organizedPath):

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

        if(os.path.isdir(organizedPath + modified_date)):
            shutil.move(os.path.join(path, x), organizedPath + modified_date)

        else:

            os.makedirs(organizedPath + modified_date)
            shutil.move(os.path.join(path, x), organizedPath + modified_date)

# Path where we have to count files and directories


def countFiles(path, Data, organizedPath):
    # path = os.getcwd()
    n = 0
    for base, dirs, files in os.walk(path):
        print('Looking in : ', base)
        for Files in files:
            n += 1
    print('Number of files', n)
    print(Files, dirs)

# This function check the condition by which the files


def organize(args):
    path = args.path
    organizeBy = args.o

    # For exception handling during wrong path input
    try:
        Data = get_Data(path)
    except FileNotFoundError:
        print('Invalid path directory')
        return

    if not os.path.exists(path + '/organized'):
        os.makedirs(path + '/organized')
    organizedPath = path + '/organized/'

    if organizeBy == 'ext':
        byExtension(path, Data, organizedPath)
    elif organizeBy == 'size':
        bySize(path, Data, organizedPath)
    elif organizeBy == 'date':
        bydate(path, Data, organizedPath)
    elif organizeBy == 'count':
        countFiles(path, Data, organizedPath)


print('Done')

# Driver code


if __name__ == '__main__':
    main()
