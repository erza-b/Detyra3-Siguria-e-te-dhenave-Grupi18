import tkinter as tk
from tkinter import filedialog
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import binascii
import os


def generate_random_key(size):
    return get_random_bytes(size)


def bytes_to_hex_string(data):
    return binascii.hexlify(data).decode()


def hex_string_to_bytes(hex_string):
    return binascii.unhexlify(hex_string)


def show_success_message(message):
    current_message = success_label.cget("text")
    new_message = current_message + "\n" + message
    success_label.config(text=new_message)


def encrypt_decrypt_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            key1 = generate_random_key(8)
            key2 = generate_random_key(8)
            iv = get_random_bytes(8)

            with open(file_path, "rb") as file:
                data = file.read()

            encrypt_cipher = DES3.new(key1 + key2, DES3.MODE_CBC, iv)
            encrypted_data = encrypt_cipher.encrypt(pad(data, DES3.block_size))

            encrypted_hex = bytes_to_hex_string(encrypted_data)

            directory = os.path.dirname(file_path)
            file_name = os.path.basename(file_path)
            encrypted_file_path = os.path.join(directory, f"{os.path.splitext(file_name)[0]}_encrypted{os.path.splitext(file_name)[1]}")
            with open(encrypted_file_path, "w") as encrypted_file:
                encrypted_file.write(encrypted_hex)

            show_success_message("Enkriptimi u krye me sukses!")
            print("File-i i enkriptuar u ruajt në:", encrypted_file_path)

            decrypt_cipher = DES3.new(key1 + key2, DES3.MODE_CBC, iv)
            decrypted_data = unpad(decrypt_cipher.decrypt(hex_string_to_bytes(encrypted_hex)), DES3.block_size)

            decrypted_file_path = os.path.join(directory, f"{os.path.splitext(file_name)[0]}_decrypted{os.path.splitext(file_name)[1]}")
            with open(decrypted_file_path, "wb") as decrypted_file:
                decrypted_file.write(decrypted_data)

            show_success_message("Dekriptimi u krye me sukses!")
            print("File-i i dekriptuar u ruajt në:", decrypted_file_path)

        except Exception as e:
            print("An error occurred during encryption and decryption:", str(e))


root = tk.Tk()
root.title("Enkriptimi dhe Dekriptimi i File-ve")

main_frame = tk.Frame(root)
main_frame.pack(padx=120, pady=70)

button_frame = tk.Frame(main_frame, width=30, height=15)
button_frame.pack(pady=10, padx=10)

encrypt_decrypt_button = tk.Button(button_frame, text="Enkripto dhe Dekripto", command=encrypt_decrypt_file)
encrypt_decrypt_button.pack()

success_label = tk.Label(main_frame, text="", fg="green")
success_label.pack()

root.mainloop()
