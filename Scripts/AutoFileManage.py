import tkinter as tk
import SortDownloads
import os, json
from tkinter import ttk

AUTO_CLOSE_TIME = 10000 #ms
NORMAL_FONT = ("Helvetica", 12)
LARGE_FONT = ("Helvetica", 14)

# Create folder in users app data to store config file
appdataPath = os.getenv('APPDATA')
if not os.path.exists(appdataPath + "\\Automated-File-Manager"):
    os.makedirs(appdataPath + "\\Automated-File-Manager")
appdataPath += "\\Automated-File-Manager\\"

# Default config JSON
configData = {
    "isFirstRun": True,
    "runOnStart": False,
    "autoClose": False,
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

class ConfigureTool(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Automated File Manager")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, ConfigPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column = 0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        lblStatus = tk.Label(self, text ="Welcome. \n Click Config to adjust options \n Click Run to sort Downloads", font=LARGE_FONT)
        lblStatus.pack(pady=10, expand=True)
        lblInfo = tk.Label(self, text ="", font=NORMAL_FONT)
        lblInfo.pack(expand=True)

        runOnStart = tk.BooleanVar()
        runOnStart.set(config["runOnStart"])
        chkStart = ttk.Checkbutton(self, text="Run on start", variable=runOnStart, command=lambda: OnRunOnStartClick(runOnStart.get()))
        chkStart.pack(side="top", expand=True, anchor="s")

        autoClose = tk.BooleanVar()
        autoClose.set(config["autoClose"])
        chkClose = ttk.Checkbutton(self, text="Auto close after run", variable=autoClose, command=lambda: OnCloseClick(autoClose.get()))
        chkClose.pack(side="top", anchor="s")

        btnOpen = ttk.Button(self, text="Open Config", command=lambda: controller.show_frame(ConfigPage))
        btnOpen.pack(side="left", anchor="sw", expand=True, fill="x")
        btnRun = ttk.Button(self, text="Run", command=lambda: OnRun(lblStatus))
        btnRun.pack(side="left", anchor="s", expand=True, fill="x")
        btnClose = ttk.Button(self, text="Exit", command=lambda: controller.destroy())
        btnClose.pack(side="left", anchor="se", expand=True, fill="x")

        # Check if Run on Start enabled
        if(config["runOnStart"] == True):
            OnRun(lblStatus)
        
        if(config["autoClose"] == True):
            UpdateLabel(lblInfo, f"Program will auto close in {AUTO_CLOSE_TIME / 1000} seconds.")
        
class ConfigPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text ="Config Page", font=LARGE_FONT)
        label.pack(pady=10)

        btnSave = ttk.Button(self, text="Save")
        btnSave.pack(side="left", anchor="sw", expand=True, fill="x")
        btnBack = ttk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        btnBack.pack(side="left", anchor="se", expand=True, fill="x")

def UpdateLabel(label, lblTxt):
    label.configure(text=lblTxt)

def OnRunOnStartClick(value):
    config["runOnStart"] = value
    UpdateConfig()

def OnCloseClick(value):
    config["autoClose"] = value
    UpdateConfig()

def OnRun(label):
    status = SortDownloads.run()
    label.configure(text=status)

def UpdateConfig():
    with open(appdataPath + "config.json", "w") as outfile:
        json.dump(config, outfile, indent=4)


app = ConfigureTool()

# Check if autoclose is enabled. If it is: close after AUTO_CLOSE_TIME ms
if(config["autoClose"] == True):
    app.after(AUTO_CLOSE_TIME, lambda: app.destroy())

app.geometry("400x200")
app.mainloop()
