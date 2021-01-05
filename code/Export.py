# render as tifs
import os
from tkinter import filedialog
import tkinter as tk
command = "cmd"

resolve = app.GetResolve()
pm = resolve.GetProjectManager()
proj = pm.GetCurrentProject() 

def myexport(format, codec):

    proj.DeleteAllRenderJobs()

    root = tk.Tk()
    root.withdraw()

    directoryName = filedialog.askdirectory(parent=root, initialdir="/", title = 'Please select a directory')

    proj.SetRenderSettings({"TargetDir": directoryName})

    proj.SetCurrentRenderFormatAndCodec(format, codec)
    proj.AddRenderJob()
    proj.StartRendering()

    flag = proj.IsRenderingInProgress()

    while flag:
        flag = proj.IsRenderingInProgress()
        pass

    os.system(command)

myexport("TIFF", "RGB8")