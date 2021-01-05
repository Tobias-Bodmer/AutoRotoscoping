import FindMattes as fm
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog as sd
from os import listdir

# Render as tifs



# Create masks
root = tk.Tk()
root.withdraw()

directoryName = filedialog.askdirectory(parent=root, initialdir="/", title = 'Please select a directory')
matteHeight = sd.askinteger("Set the matte size", "Output matte vertical resolution (256 recommended for quick tests)?", parent=root,initialvalue=256)

listOfFiles = listdir(directoryName)

for currentFile in listOfFiles:
    sourceFile = directoryName + "/" + currentFile
    mainNameEnd = currentFile.find('.')
    nameForMatte = currentFile[:mainNameEnd] + "_matte" + currentFile[mainNameEnd:]
    fullPathMatteName = directoryName + "/" + nameForMatte
    fm.createMatte(sourceFile, fullPathMatteName, matteHeight)
    print("Just created: " + nameForMatte)


# import masks