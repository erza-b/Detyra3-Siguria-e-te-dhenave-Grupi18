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
                # Encrypt the data
            encrypt_cipher = DES3.new(key1 + key2, DES3.MODE_CBC, iv)
            encrypted_data = encrypt_cipher.encrypt(pad(data, DES3.block_size))

            # Convert encrypted data to hexadecimal string
            encrypted_hex = bytes_to_hex_string(encrypted_data)

            # Decrypt the data
            decrypt_cipher = DES3.new(key1 + key2, DES3.MODE_CBC, iv)
            decrypted_data = unpad(decrypt_cipher.decrypt(hex_string_to_bytes(encrypted_hex)), DES3.block_size)

            # Save the encrypted and decrypted data to the same file
            output_file_path = filedialog.asksaveasfilename(defaultextension=".enc")
            if output_file_path:
                with open(output_file_path, "w") as output_file:
                    output_file.write("Encrypted Data:\n")
                    output_file.write(encrypted_hex)
                    output_file.write("\n\nDecrypted Data:\n")
                    output_file.write(decrypted_data.decode())

                print("Encryption and decryption completed successfully!")
                print("Output file saved at:", output_file_path)

        except Exception as e:
            print("An error occurred during encryption and decryption:", str(e))



