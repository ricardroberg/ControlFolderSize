# ControlFolderSize
V.1
Attempt to manage Cloud folder, DVR backups, etc. Locally. When the folder hit the limit size, the script will remove all files except the newer one.

## OBS:
Variables must be changed:  
folderPath = getenv('ENVIROMENT_VARIABLE_NAME')  
controledFolder = join(folderPath, 'FOLDER_NAME')  
limit = 4500  # SIZE EM MEGABYTES  

Next:
1 -   
Enter variable path and folder name, as well the size limit thought command line  
ex: python controlfolder.py TEMP 5000 (folder name supressed)  

2 -   
Implement watchdog to keep script alive instead using task manager to run it.  

3 -
Option to move files to another folder.
