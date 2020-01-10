import os, shutil, json

def run():

    # Create folder in users app data to store config file
    appdataPath = os.getenv('APPDATA')
    appdataPath += "\\Automated-File-Manager\\"

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

    return f"Organized {numFiles} files in Downloads"

    #TODO: Move this to GUI, remove notifs
    #toaster = ToastNotifier()
    #toaster.show_toast("Daily Automation", f"Organized {numFiles} files in Downloads.", threaded=True, icon_path=None, duration=6)

if __name__ == "__main__":
    run()
