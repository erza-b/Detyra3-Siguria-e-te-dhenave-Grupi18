import tkinter as tk
from tkinter import messagebox
import os
import sys

def redirect_txt():
    # Krijimi i path-it te file-it te njejt duke perdorur os.path.join()
    file_path = os.path.join("Projekt", "txtfiles.py")
    os.system(file_path)
    sys.exit()