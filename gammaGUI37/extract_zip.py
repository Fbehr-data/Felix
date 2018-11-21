"""
Python 3.7.0 (default, Jun 28 2018, 08:04:48) [MSC v.1912 64 bit (AMD64)]
Python 3.7.0 (default, Jun 28 2018, 08:04:48) [MSC v.1912 64 bit (AMD64)] on win32

Tasks: List Zip Files and extract them into Same Folder (GammaGUI needs *.SAFE Structure)
"""

# Import Libs
import os, zipfile

def unzip_files ():
    """
    Extract all *.zip Files in current Working Directory
    """
    try:
        import os, zipfile
    except ImportError:
        # Try to install it automatically
        # https://stackoverflow.com/questions/46419607/how-to-automatically-install-required-packages-from-a-python-script-as-necessary
        print('Please install {os} and {zipfile} via pip install'.format(os = 'os', zipfile = 'zipfile')) #Keine Print Funktion in Python 3?! für format!?

    print('-- Start unzipping --')

    # Set wdir and extension
    wdir = os.getcwd() # String CWD
    extension = ".zip" # String Extension

    for i in os.listdir(wdir):  # loop through items in dir
        if i.endswith(extension):  # check for ".zip" extension
            file_name = os.path.abspath(i)  # get full path of files
            zip_ref = zipfile.ZipFile(file_name)  # create zipfile object
            zip_ref.extractall(wdir)  # extract file to dir
            zip_ref.close()  # close file
            print('File: {file} -- successfully extracted --'.format(file = i))

    print("-- Unzipping finished --")

unzip_files()
