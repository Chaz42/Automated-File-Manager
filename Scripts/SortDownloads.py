import os, shutil, json
from win10toast import ToastNotifier

#TODO: Check if first launch, if so: create default config file, place in Appdata
# if not, load file from appdata
with open("c:/Users/forte/Documents/github/Automated-File-Manager/Scripts/config.json") as jsonFile:
    config = json.load(jsonFile)

path = os.path.expanduser("~\Downloads\\")
folderName = config["folderName"]
docExtensions = config["docExtensions"]
exeExtensions = config["exeExtensions"]
picExtensions = config["picExtensions"]
txtExtensions = config["txtExtensions"]
zipExtensions = config["zipExtensions"]
folderPaths = config["folderPaths"]

numFiles = 0
numFiles += len(folderName)
items = os.listdir(path)


def moveFile(file):
    for extension in docExtensions:
        if extension in file and not os.path.exists(path + folderPaths["docPath"] + file):
            shutil.move(path + file, path + folderPaths["docPath"] + file)
            return
    for extension in exeExtensions:
        if extension in file and not os.path.exists(path + folderPaths["exePath"] + file):
            shutil.move(path + file, path + folderPaths["exePath"] + file)
            return
    for extension in picExtensions:
        if extension in file and not os.path.exists(path + folderPaths["picPath"] + file):
            shutil.move(path + file, path + folderPaths["picPath"] + file)
            return
    for extension in txtExtensions:
        if extension in file and not os.path.exists(path + folderPaths["txtPath"] + file):
            shutil.move(path + file, path + folderPaths["txtPath"] + file)
            return
    for extension in zipExtensions:
        if extension in file and not os.path.exists(path + folderPaths["zipPath"] + file):
            shutil.move(path + file, path + folderPaths["zipPath"] + file)
            return
    # If none of above, move to Other folder
    if not os.path.exists(path + folderPaths["otherPath"] + file):
        shutil.move(path + file, path + folderPaths["otherPath"] + file)
        return

    #TODO: Don't count duplicate files
    #numFiles -= 1
    #NOTE: If a file already exists, it gets put in Other.
    # What if that file also exists in other?

# Creates new folder if it doesn't already exist in path
for folder in folderName:
    if not os.path.exists(path + folder):
        os.makedirs(path + folder)

# Check each file type and move accordingly
for file in items:
    numFiles += 1
    # Avoid category folders & desktop ini file
    if file in folderName or file == "desktop.ini":
        numFiles -= 1
        continue
    # Move the file
    moveFile(file)

toaster = ToastNotifier()
toaster.show_toast("Daily Automation", f"Organized {numFiles - len(folderName)} files in Downloads.", threaded=True, icon_path=None, duration=6)
