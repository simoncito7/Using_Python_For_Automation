# importing os library
import os 
from pathlib import Path

# we define a dictionary named SUBDIRECTORIES that contains some extensions corresponding to each type of file
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

def pickDirectory(value):
    for category, suffixies in SUBDIRECTORIES.items():
        for suffix in suffixies:
            if suffix == value:
                return category
    return 'MISC'

print(pickDirectory('.pdf'))

def organizeDirectory():
    # os.scandir() returns an iterator of DirEntry (item) objects for given path
    for item in os.scandir():
        if item.is_dir():                       # 
            continue       
        filePath = Path(item)                   # Paths of item are stored in filePath
        fileType = filePath.suffix.lower()      # 
        directory = pickDirectory(fileType)     # here pickDirectory function is called to know what category filetype belongs to
        directoryPath = Path(directory)         # We store the directory path into directoryPath

        if directoryPath.is_dir() != True:              # if directoryPath doesn't exists, then we create one
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))


organizeDirectory()

