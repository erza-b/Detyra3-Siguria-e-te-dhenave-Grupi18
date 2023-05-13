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


def load_text_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("Markdown Files", "*.md")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                content = file.read()
                text_content.delete(1.0, tk.END)
                text_content.insert(tk.END, content)

        except Exception as e:
            print("An error occurred while loading the file:", str(e))



def encrypt_decrypt_content():
    content = text_content.get(1.0, tk.END).strip()
    if content:
        try:
            key1 = generate_random_key(8)
            key2 = generate_random_key(8)
            iv = get_random_bytes(8)

            # Encrypt the content
            encrypt_cipher = DES3.new(key1 + key2, DES3.MODE_CBC, iv)
            encrypted_data = encrypt_cipher.encrypt(pad(content.encode(), DES3.block_size))

            # Convert encrypted data to hexadecimal string
            encrypted_hex = bytes_to_hex_string(encrypted_data)

            # Decrypt the content
            decrypt_cipher = DES3.new(key1 + key2, DES3.MODE_CBC, iv)
            decrypted_data = unpad(decrypt_cipher.decrypt(hex_string_to_bytes(encrypted_hex)), DES3.block_size)

            # Update the encrypted and decrypted content labels
            encrypted_content.config(state=tk.NORMAL)
            encrypted_content.delete(1.0, tk.END)
            encrypted_content.insert(tk.END, encrypted_hex)
            encrypted_content.config(state=tk.DISABLED)

            decrypted_content.config(state=tk.NORMAL)
            decrypted_content.delete(1.0, tk.END)
            decrypted_content.insert(tk.END, decrypted_data.decode())
            decrypted_content.config(state=tk.DISABLED)

        except Exception as e:
            print("An error occurred during encryption and decryption:", str(e))


root = tk.Tk()
root.title("Text File Encryption and Decryption")

# Main Frame
main_frame = tk.Frame(root)
main_frame.pack(padx=120, pady=70)

# Load File Button
button_frame = tk.Frame(main_frame)
button_frame.pack(pady=10)

load_file_button = tk.Button(button_frame, text="Load File", command=load_text_file)
load_file_button.pack(side=tk.LEFT)

# Text Content
text_content = tk.Text(main_frame, height=10, width=40)
text_content.pack(pady=10)

# Encrypt/Decrypt Button
encrypt_decrypt_button = tk.Button(main_frame, text="Encrypt and Decrypt", command=encrypt_decrypt_content)
encrypt_decrypt_button.pack()

# Encrypted Content Label
encrypted_label = tk.Label(main_frame, text="Encrypted Content:")
encrypted_label.pack()

encrypted_content = tk.Text(main_frame, height=10, width=100, wrap=tk.WORD, state=tk.DISABLED)
encrypted_content.pack(pady=5)

# Decrypted Content Label
decrypted_label = tk.Label(main_frame, text="Decrypted Content:")
decrypted_label.pack()

scrollbar = tk.Scrollbar(main_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

decrypted_content = tk.Text(main_frame, height=10, width=100, wrap=tk.WORD, state=tk.DISABLED)
decrypted_content.pack(pady=5)
decrypted_content.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=decrypted_content.yview)

root.mainloop()
