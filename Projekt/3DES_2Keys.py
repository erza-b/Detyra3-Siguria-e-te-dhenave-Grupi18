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





