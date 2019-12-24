import os, shutil
from win10toast import ToastNotifier

path = "C:/Users/forte/Downloads/"
folderName = ["Text Files", "Zips", "Executables", "Pictures", "Documents", "Other"]
docExtensions = [".doc", ".docx", ".pptx", ".pdf", ".xlsx", ".vsdx"]
exeExtensions = [".exe", ".msi"]
picExtensions = [".png", ".jpg"]
txtExtensions = [".txt", ".json"]
zipExtensions = [".zip", ".rar", ".7z", ".gz"]
docPath = "Documents/"
exePath = "Executables/"
picPath = "Pictures/"
txtPath = "Text Files/"
zipPath = "Zips/"
otherPath = "Other/"
numFiles = 0
numFiles += len(folderName)
items = os.listdir(path)

def moveFile(file):
    for extension in docExtensions:
        if extension in file and not os.path.exists(path + docPath + file):
            shutil.move(path + file, path + docPath + file)
            return
    for extension in exeExtensions:
        if extension in file and not os.path.exists(path + exePath + file):
            shutil.move(path + file, path + exePath + file)
            return
    for extension in picExtensions:
        if extension in file and not os.path.exists(path + picPath + file):
            shutil.move(path + file, path + picPath + file)
            return
    for extension in txtExtensions:
        if extension in file and not os.path.exists(path + txtPath + file):
            shutil.move(path + file, path + txtPath + file)
            return
    for extension in zipExtensions:
        if extension in file and not os.path.exists(path + zipPath + file):
            shutil.move(path + file, path + zipPath + file)
            return
    # If none of above, move to Other folder
    if not os.path.exists(path + otherPath + file):
        shutil.move(path + file, path + otherPath + file)
        return

    #TODO: Don't count duplicate files
    #numFiles -= 1

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
toaster.show_toast("Daily Automation", "Organized " + str(numFiles - len(folderName)) + " files in Downloads.", threaded=True, icon_path=None, duration=6)
