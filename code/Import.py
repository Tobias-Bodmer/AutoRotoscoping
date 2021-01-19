# import masks
from python_get_resolve import GetResolve
from tkinter import filedialog
import tkinter as tk
import time

resolve = GetResolve()
pm = resolve.GetProjectManager()
proj = pm.GetCurrentProject()
ms = resolve.GetMediaStorage()
mp = proj.GetMediaPool()
tl = proj.GetCurrentTimeline()

root = tk.Tk()
root.withdraw()

def myimport(timelinename, window):

    directoryName = filedialog.askopenfilename(parent=root, initialdir="/", title = window)

    newtl = mp.CreateEmptyTimeline(timelinename)

    mp.AppendToTimeline(ms.AddItemsToMediaPool(directoryName))

def myimport_matte():
    resolve.OpenPage("edit")
    directoryName = filedialog.askopenfilename(parent=root, initialdir="/", title = 'Please select matte.')

    tl = proj.GetCurrentTimeline()

    tlItem = tl.GetCurrentVideoItem()
    print(tlItem)
    mpItem = tlItem.GetMediaPoolItem()
   
    ms.AddClipMattesToMediaPool(mpItem, directoryName)
    resolve.OpenPage("color")

def myexport(format, codec):

    proj.DeleteAllRenderJobs()

    directoryName = filedialog.askdirectory(parent=root, initialdir="/", title = 'Please select a directory for exporting.')   

    proj.SetRenderSettings({"TargetDir": directoryName})

    proj.SetCurrentRenderFormatAndCodec(format, codec)
    proj.AddRenderJob()
    proj.StartRendering()

    flag = proj.IsRenderingInProgress()

    while flag:
        flag = proj.IsRenderingInProgress()
        pass

#load tifs
myimport("PreparingProject", "Please select the first matte tiff.")
#export mov
myexport("mp4", "H264")

pm.CreateProject("RotoscopeProject")
proj = pm.GetCurrentProject()
mp = proj.GetMediaPool()

#load video for rotoscope
myimport("Final-Rotoscope", "Please select the video you want to matte.")

#load matte from mp4
myimport_matte()

