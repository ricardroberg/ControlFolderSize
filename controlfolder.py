from os import getenv, listdir, remove
from os.path import *
from shutil import move

# get folder size and file list
def getFolderSize(p):
    """
    Script got from StackOverFlow
    url: https://stackoverflow.com/questions/1392413/calculating-a-directorys-size-using-python/
    from: user2772509
    """
    from functools import partial
    prepend = partial(join, p)
    return sum([(getsize(f) if isfile(f) else getFolderSize(f)) for f in map(prepend, listdir(p))])


def getFileList(p):
    """
    Script got from StackOverFlow
    url: https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
    from: pycruft
    slightly modified to create a dict with full file path and ctime, intead a list with only filename
    """
    # Create dictionary with absolute path and ctime
    return {join(controledFolder, filename): getctime(join(controledFolder, filename))
            for filename in listdir(p) if isfile(join(p, filename))}


# Get environment variables
# Using for ONEDRIVE folder controll
folderPath = getenv('ENVIROMENT_VARIABLE_NAME')
controledFolder = join(folderPath, 'FOLDER_NAME')  # Set file of folder to be controlled
foldersize = int(getFolderSize(controledFolder))/1048576  # folder size in MegaBytes
limit = 4500  # SIZE EM MEGABYTES
newest = 0

# Create and store file list and set the newest variable to store newest file
with open('folderdata.txt', 'w') as file:
    file.write(f'Folder size: {foldersize:.2f} MB;\n')
    for k,v in getFileList(controledFolder).items():
        file.writelines(f'{k};{v}\n')
        newest = v if v > newest else newest
    file.writelines(f'{newest};')


# Remove older files if limit is reached
if foldersize > limit:
    with open('folderdata.txt', 'r') as file:
        line = file.readlines()
        for l in range(1, len(line)-1):
            if line[l].split(';')[1] < line[len(line)-1].split(';')[0]:
                remove(line[l].split(';')[0])

# PUSHING THIS IF BLOCK INSIDE THE ABOVE 'WITH OPEN' WOULD REDUCE SOME LINES. BUT THE INTENTION, IN THE FUTURE,
# IS TO MAKE THE CODE MORE O.O. AND CREATE A CLASS AND SOME METHODS.
