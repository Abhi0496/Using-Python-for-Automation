#scandir() helps to check what we have in current directory
#scandir will grab every object in our folder and further our goal of grabbing each file extension

import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

def pickDirectory(value):
    for category,suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category

    return 'MISC'
#print(pickDirectory(".pdf"))

def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue

        filePath = Path(item) 
        #print(type(filePath)) #Path(item) returns <class 'pathlib.PosixPath'> and not string

        #filetype = filePath.split(".")[-1] since its not returning string we cannot really do split to find out extension
        filetype = filePath.suffix.lower() #to get extension
        directory = pickDirectory(filetype)
        directoryPath = Path(directory)

        if directoryPath.is_dir() == False:
            directoryPath.mkdir()
        
        filePath.rename(directoryPath.joinpath(filePath)) #since we are moving the file we have to rename the path
        

organizeDirectory()
