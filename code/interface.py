import tkinter as tk
from tkinter import messagebox as mb

def call():
    result = mb.askquestion('Maskenabfrage', 'Existieren bereits Maskierte tiffs?')
    if result == 'yes' :
        import Import
    else :
        import Export 
        import Import

call()