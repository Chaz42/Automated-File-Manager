import tkinter as tk
import SortDownloads
from tkinter import ttk

LARGE_FONT = ("Helvetica", 16)

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

        label1 = tk.Label(self, text ="Hello", font=LARGE_FONT)
        label1.pack(pady=10)

        btnOpen = ttk.Button(self, text="Open Config", command=lambda: controller.show_frame(ConfigPage))
        btnOpen.pack(side="left", anchor="sw", expand=True, fill="x")
        btnRun = ttk.Button(self, text="Run", command=lambda: SortDownloads.run())
        btnRun.pack(side="left", anchor="s", expand=True, fill="x")
        btnClose = ttk.Button(self, text="Exit", command=lambda: controller.destroy())
        btnClose.pack(side="left", anchor="se", expand=True, fill="x")
        update_label(label1)
        
class ConfigPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text ="Config Page", font=LARGE_FONT)
        label.pack(pady=10)

        btnSave = ttk.Button(self, text="Save")
        btnSave.pack(side="left", anchor="sw", expand=True, fill="x")
        btnBack = ttk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        btnBack.pack(side="left", anchor="se", expand=True, fill="x")

def update_label(label):
    label.configure(text="Updated Label")

app = ConfigureTool()
app.geometry("400x100")
app.mainloop()