# Python-Project - JUNK FILES ORGANIZER

Python Project based on Junk File Organizer.

# NEED :

I made this Project to simplify my file Organization in a specific folder, it takes a lot of time to organize the different files in my system.

# Technology Stack Used
​
This project uses a number of open source tools, technologies and frameworks to work properly:
​

- [Visual Studio Code](https://code.visualstudio.com) - A code editor redefined and optimized for building and debugging modern web and cloud applications.

- [Flake8](https://pypi.org/project/flake8) - static analysis of source code checking for symantec discrepancies

# Built using:
1. [Python language](https://www.python.org/)
2. The code is built according to the standard pep8 rules and regulations.

# LIBRARIES USED :

import os - to get all the files from the directories,to create directories.  
import shutil - to move the files from one directory to another.  
import ntpath - to get the exact path of the file.  
import time - to get the time the files are deployed in that directory.  

# APPROACH USED :

1. For Extension based organization - For the Extension based organization we have created a file types and saved all the possible extensions I can think of to access the extensions and afterwords moving the files to their specified directories. Checking the extension of the file in the computer directory and then compairing it with the dictionary values of extensions if matched then creating the new directory and inside it moving the different files according to the specified new directories.

2. For date/Time based organization - Fetching the date/time for the files stored inside the directories. After finding out the days it is bin stored, the files are then moved to different directories according to the number of days by comparing it using the condition statements.

3. For SIZE based organization - I am checking the file size by using the if and elif conditions in the files directory into their specific folders as per the size of the files. The files which are in Bytes are inside a directory called BYTES and just like that all the different files in the subsequent folders(BYTES,KB,MB,GB)

# How To Run This Project File :

1.Store the junk file JunkFileOrganizer.py file in your system anywhere you want.

2.Go to terminal type python3 JunkFileOrganizer.py

3.Hit the Enter and run button

4.After doing anyone option from this it it asks user input

- 1 FOR TO ORGANIZE FILE BY EXTENSION.
- 2 FOR TO ORGANIZE BY DATE.
- 3 TO KNOW THE SIZE OF FILES IN YOUR DIRECTORY.
- Enter Path where you want to organize file.
