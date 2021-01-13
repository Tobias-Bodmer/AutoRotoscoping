import Export
import Import
import tkinter as tk
from tkinter import messagebox as mb

def call():
    result = mb.askquestion('Maskenabfrage', 'Exestiert bereits eine Maske?')
    if result == 'yes' :
        Export
    else :
        Import

call()