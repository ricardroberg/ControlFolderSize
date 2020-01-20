from os import getenv, listdir
from os.path import join, isfile, getsize, getctime, abspath
from shutil import move

# Get environment variables
# Using for ONEDRIVE folder controll
folderPath = getenv('ONEDRIVE')

# Set file of folder to be controlled
controledFolder = join(folderPath, 'DB')

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
    slightly modified
    """
    # Create dictionary with absolute path and ctime
    return {join(controledFolder, filename): getctime(join(controledFolder, filename))
            for filename in listdir(p) if isfile(join(p, filename))}


#print(getctime(folderPath, 'ex13_aula25.mwb'))

foldersize = int(getFolderSize(controledFolder))/1048576  # folder size in MegaBytes
print(getFileList(controledFolder))

# Create and store file list and set the newest variable to store newest file
with open('folderdata.txt', 'w') as file:
    newest = 99999999999999999999999999999
    file.write(f'Folder size: {foldersize:.2f} MB\n')
    for k,v in getFileList(controledFolder).items():
        file.writelines(f'{k};{v}\n')
        if v < newest


# Remove older files if limit is reached
limit = 4500  # Free Onedrive accounts hold 5GB

# if foldersize >= limit:
#     lowestcreattime = 0
#     for

# print(getFolderSize(controledFolder))
# print(getFileList(controledFolder))