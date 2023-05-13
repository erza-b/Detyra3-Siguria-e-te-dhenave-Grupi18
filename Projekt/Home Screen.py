import tkinter as tk
from tkinter import messagebox
import os
import sys

import response as response


def redirect_txt():
    # Krijimi i path-it te file-it te njejt duke perdorur os.path.join()
    file_path = os.path.join("Projekt", "txtfiles.py")
    os.system(file_path)
    sys.exit()

def redirect_other():
    # Krijimi i path-it te file-it tjeter duke perdorur os.path.join()
    file_path = os.path.join("Projekt", "otherfiles.py")
    os.system(file_path)
    sys.exit()

def file_selection():
    #Mesazhi i messagebox-it qe pyet perdoruesin nese deshiron te enkriptojke dhe dekriptoje nje file .txt/.md ose  je file tjeter
    response=messagebox.askquestion("Enkriptimi dhe Dekriptimi","Deshironi te enkriptoni nje file '.txt/.md' ose nje file tjeter?\n('yes' per .txt/md,'no' per file tjeter)",icon='question')
if response=='po':
    redirect_txt()
else:
    redirect_other()
    root=tk.Tk()
    root.title("Enkriptimi dhe dekriptimi")

