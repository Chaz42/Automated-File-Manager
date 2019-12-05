import os, shutil
from win10toast import ToastNotifier

videosFolder = "C:/Users/forte/Videos/"
destination = "F:/Videos/"
numEmptyFolders = 0
numFilesMoved = 0

for folders in os.listdir(videosFolder):
    folderPath = os.path.join(videosFolder, folders)
    if os.path.isdir(folderPath):
        if not os.listdir(folderPath):
            os.removedirs(folderPath)
            numEmptyFolders += 1
        else:
            for videos in os.listdir(folderPath):
                newDest = destination + folders
                if not os.path.isdir(newDest):
                    os.mkdir(newDest)
                    shutil.move(folderPath + "/" + videos, newDest)
                    numFilesMoved += 1
                else:
                    shutil.move(folderPath + "/" + videos, newDest)
                    numFilesMoved += 1

# Clean up remaining empty folders
for folders in os.listdir(videosFolder):
    folderPath = os.path.join(videosFolder, folders)
    if os.path.isdir(folderPath):
        if not os.listdir(folderPath):
            os.removedirs(folderPath)

toaster = ToastNotifier()
toaster.show_toast("Daily Automation", "Deleted " + str(numEmptyFolders) + " empty folders. Moved " + str(numFilesMoved) + " files to external drive.", threaded=True, icon_path=None, duration=6)