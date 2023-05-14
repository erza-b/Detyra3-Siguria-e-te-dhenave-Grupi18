import tkinter as tk
from tkinter import filedialog
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
import binascii

def generate_random_key(size):
    return get_random_bytes(size)

def bytes_to_hex_string(data):
    return binascii.hexlify(data).decode()

def hex_string_to_bytes(hex_string):
    return binascii.unhexlify(hex_string)

def show_success_message(message):
    success_label.config(text=message)

def encrypt_decrypt_file():
    if file_path:
        try:
            key1=generate_random_key(8)
            key2=generate_random_key(8)
            iv=get_random_bytes(8)

            with open(file_path,"rb") as file:
                data=file.read()
            encrypt_cipher=DES3.new(key1+key2,DES3.MODE_CBC,iv)
            encrypted_data=encrypt_cipher.encrypt(pad(data,DES3.block_size))
            encrypted_hex=bytes_to_hex_string(encrypted_data)
            encrypted_file_path=filedialog.asksaveasfilename(defaultextension=".enc")
                if encrypted_file_path:
                    with open(encrypted_file_path,"w")
            as encrypted_file:
        encrypted_file.write(encrypted_hex)
            show_success_message("Enkriptimi u krye me sukses!")
            print("File i enkriptuar u ruajt ne :",encrypted_file_path)

        