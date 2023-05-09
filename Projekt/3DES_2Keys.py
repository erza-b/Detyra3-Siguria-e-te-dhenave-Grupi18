import tkinter as tk
from tkinter import filedialog
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import binascii

def generate_random_key(size):
    return get_random_bytes(size)

def bytes_to_hex_string(data):
    return binascii.hexlify(data).decode()

def hex_string_to_bytes(hex_string):
    return binascii.unhexlify(hex_string)


def encrypt_decrypt_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            key1 = generate_random_key(8)
            key2 = generate_random_key(8)
            iv = get_random_bytes(8)

            with open(file_path, "rb") as file:
                data = file.read()


