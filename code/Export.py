# render as tifs
from python_get_resolve import GetResolve
import os
from tkinter import filedialog
import tkinter as tk
command = "cmd /k py C:/tmp/autoroto.py"

resolve = GetResolve()
pm = resolve.GetProjectManager()
proj = pm.GetCurrentProject() 

def myexport(format, codec):

    proj.DeleteAllRenderJobs()

    root = tk.Tk()
    root.withdraw()

    directoryName = filedialog.askdirectory(parent=root, initialdir="/", title = 'Please select a directory for exporting(use an empty folder).')

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