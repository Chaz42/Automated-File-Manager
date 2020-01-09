import os, shutil, json
from win10toast import ToastNotifier

def run():
    # Create folder in users app data to store config file
    appdataPath = os.getenv('APPDATA')
    if not os.path.exists(appdataPath + "\\Automated-File-Manager"):
        os.makedirs(appdataPath + "\\Automated-File-Manager")
    appdataPath += "\\Automated-File-Manager\\"

    # Default config JSON
    configData = {
        "folderName": ["Text Files", "Zips", "Executables", "Pictures", "Documents", "Other"],
        "docExtensions": [".doc", ".docx", ".pptx", ".pdf", ".xlsx", ".vsdx"],
        "exeExtensions": [".exe", ".msi"],
        "picExtensions": [".png", ".jpg"],
        "txtExtensions": [".txt", ".json"],
        "zipExtensions": [".zip", ".rar", ".7z", ".gz"],
        "folderPaths": {
            "docPath": "Documents/",
            "exePath": "Executables/",
            "picPath": "Pictures/",
            "txtPath": "Text Files/",
            "zipPath": "Zips/",
            "otherPath": "Other/"
        }
    }

    # Check if config exists. If it doesn't, write configData to new file
    if not os.path.exists(appdataPath + "config.json"):
        with open(appdataPath + "config.json", "w") as outfile:
            json.dump(configData, outfile, indent=4)

    # Loads the config file
    with open(appdataPath + "config.json") as jsonFile:
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
        # Avoid category folders & desktop ini file
        if file in folderName or file == "desktop.ini":
            continue
        # Move the file
        numFiles += 1
        moveFile(file)

    #TODO: Move this to GUI, remove notifs
    #toaster = ToastNotifier()
    #toaster.show_toast("Daily Automation", f"Organized {numFiles} files in Downloads.", threaded=True, icon_path=None, duration=6)

if __name__ == "__main__":
    run()