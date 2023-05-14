import tkinter as tk
from tkinter import messagebox
import os
import sys

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
    # Mesazhi i messagebox-it qe pyet perdoruesin nese deshiron te enkriptoje dhe dekriptoje nje file .txt/.md ose nje file tjeter
    response = messagebox.askquestion("Enkriptimi dhe Dekriptimi", "Deshironi te enkriptoni dhe dekriptoni nje file '.txt/.md' ose nje file tjeter? \n ('yes' per .txt/.md, 'no' per file tjeter)", icon='question')
    if response == 'yes':
        redirect_txt()
    else:
        redirect_other()

root = tk.Tk()
root.title("Enkriptimi dhe Dekriptimi")

main_frame = tk.Frame(root)
main_frame.pack(padx=50, pady=30)

btn_frame = tk.Frame(main_frame)
btn_frame.pack(pady=10)

encrypt_decrypt_btn = tk.Button(btn_frame, text="Enkripto/Dekripto", width=15, command=file_selection)
encrypt_decrypt_btn.pack(side=tk.LEFT, padx=10)

cancel_btn = tk.Button(btn_frame, text="Anullo", width=15, command=root.destroy)
cancel_btn.pack(side=tk.LEFT, padx=10)

root.mainloop()