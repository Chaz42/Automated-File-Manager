import os, shutil
from win10toast import ToastNotifier

path = "C:/Users/forte/Downloads/"
folderName = ["Text Files", "Zips", "Executables", "Pictures", "Documents" , "Other"]
docPath = "Documents/"
exePath = "Executables/"
picPath = "Pictures/"
txtPath = "Text Files/"
zipPath = "Zips/"
otherPath = "Other/"
numFiles = 0
items = os.listdir(path)

# Creates new folder if it doesn't already exist in path
for folder in folderName:
    if not os.path.exists(path + folder):
        os.makedirs(path + folder)

# Check each file type and move accordingly
for files in items:
    numFiles += 1
    # Documents
    if ".doc" in files and not os.path.exists(path + docPath + files):
       shutil.move(path + files, path + docPath + files)
    if ".docx" in files and not os.path.exists(path + docPath + files):
       shutil.move(path + files, path + docPath + files)
    if ".pptx" in files and not os.path.exists(path + docPath + files):
       shutil.move(path + files, path + docPath + files)
    if ".pdf" in files and not os.path.exists(path + docPath + files):
       shutil.move(path + files, path + docPath + files)
    if ".xlsx" in files and not os.path.exists(path + docPath + files):
       shutil.move(path + files, path + docPath + files)
    if ".vsdx" in files and not os.path.exists(path + docPath + files):
       shutil.move(path + files, path + docPath + files)
    # Executables
    if ".exe" in files and not os.path.exists(path + exePath + files):
       shutil.move(path + files, path + exePath + files)
    if ".msi" in files and not os.path.exists(path + exePath + files):
       shutil.move(path + files, path + exePath + files)
    # Pictures
    if ".png" in files and not os.path.exists(path + picPath + files):
       shutil.move(path + files, path + picPath + files)
    if ".jpg" in files and not os.path.exists(path + picPath + files):
       shutil.move(path + files, path + picPath + files)
    # Text Files
    if ".txt" in files and not os.path.exists(path + txtPath + files):
       shutil.move(path + files, path + txtPath + files)
    if ".json" in files and not os.path.exists(path + txtPath + files):
       shutil.move(path + files, path + txtPath + files)
    # Zip Files
    if ".zip" in files and not os.path.exists(path + zipPath + files):
       shutil.move(path + files, path + zipPath + files)
    if ".rar" in files and not os.path.exists(path + zipPath + files):
       shutil.move(path + files, path + zipPath + files)
    if ".7z" in files and not os.path.exists(path + zipPath + files):
       shutil.move(path + files, path + zipPath + files)
    if ".gz" in files and not os.path.exists(path + zipPath + files):
       shutil.move(path + files, path + zipPath + files)
    # All Other Files
    if ".m" in files and not os.path.exists(path + otherPath + files):
        shutil.move(path + files, path + otherPath + files)
    if ".py" in files and not os.path.exists(path + otherPath + files):
        shutil.move(path + files, path + otherPath + files)
    if ".cs" in files and not os.path.exists(path + otherPath + files):
        shutil.move(path + files, path + otherPath + files)
    if ".jar" in files and not os.path.exists(path + otherPath + files):
        shutil.move(path + files, path + otherPath + files)
    if ".unitypackage" in files and not os.path.exists(path + otherPath + files):
        shutil.move(path + files, path + otherPath + files)
    if ".aspx" in files and not os.path.exists(path + otherPath + files):
        shutil.move(path + files, path + otherPath + files)

toaster = ToastNotifier()
toaster.show_toast("Daily Automation", "Organized " + str(numFiles - len(folderName)) + " files in Downloads.", threaded=True, icon_path=None, duration=6)