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
    # Kerkohet nga perdoruesi per te zgjedhur nje file
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("Markdown Files", "*.md")])
    if file_path:
        try:
            # Hapet file-i dhe lexohet permbajtja
            with open(file_path, "r") as file:
                content = file.read()
                # Pastrohet permbajtja e dhenash ne dritaren tekstuale
                text_content.delete(1.0, tk.END)
                # Vendoset permbajtja e lexuar ne dritaren tekstuale
                text_content.insert(tk.END, content)

        except Exception as e:
            print("Ndodhi nje gabim gjate ngarkimit te file-it:", str(e))


def encrypt_decrypt_content():
    # Merr permbajtjen e dhenash nga dritarja tekstuale
    content = text_content.get(1.0, tk.END).strip()
    if content:
        try:
            # Gjenerohet celesi i rastesishem
            key1 = generate_random_key(8)
            key2 = generate_random_key(8)
            iv = get_random_bytes(8)

            # Kriptohet permbajtja
            encrypt_cipher = DES3.new(key1 + key2, DES3.MODE_CBC, iv)
            encrypted_data = encrypt_cipher.encrypt(pad(content.encode(), DES3.block_size))

            # Konvertohet permbajtja e kriptuar ne string heksadecimal
            encrypted_hex = bytes_to_hex_string(encrypted_data)

            # Dekriptohet permbajtja
            decrypt_cipher = DES3.new(key1 + key2, DES3.MODE_CBC, iv)
            decrypted_data = unpad(decrypt_cipher.decrypt(hex_string_to_bytes(encrypted_hex)), DES3.block_size)

            # Rifreskohen etiketat e permbajtjes se kriptuar dhe dekriptuar
            encrypted_content.config(state=tk.NORMAL)
            encrypted_content.delete(1.0, tk.END)
            encrypted_content.insert(tk.END, encrypted_hex)
            encrypted_content.config(state=tk.DISABLED)

            decrypted_content.config(state=tk.NORMAL)
            decrypted_content.delete(1.0, tk.END)
            decrypted_content.insert(tk.END, decrypted_data.decode())
            decrypted_content.config(state=tk.DISABLED)

        except Exception as e:
            print("Ndodhi nje gabim gjate kriptimit dhe dekriptimit:", str(e))


root = tk.Tk()
root.title("Enkriptimi dhe Dekriptimi i File-it Tekst")

# Frame kryesor
main_frame = tk.Frame(root)
main_frame.pack(padx=120, pady=70)

# Butoni per ngarkimin e file-it
button_frame = tk.Frame(main_frame)
button_frame.pack(pady=10)

load_file_button = tk.Button(button_frame, text="Ngarko File-in", command=load_text_file)
load_file_button.pack(side=tk.LEFT)

#Dritarja tekstuale e permbajtjes
text_content = tk.Text(main_frame, height=10, width=100)
text_content.pack(pady=10)

#Butoni per enkriptim dhe dekriptim
encrypt_decrypt_button = tk.Button(main_frame, text="Enkripto dhe Dekripto", command=encrypt_decrypt_content)
encrypt_decrypt_button.pack()

#Etiketa per permbajtjen e enkriptuar
encrypted_label = tk.Label(main_frame, text="Permbajtja e Enkriptuar:")
encrypted_label.pack()

#Dritarja tekstuale e permbajtjes se enkriptuar
encrypted_content = tk.Text(main_frame, height=10, width=100, wrap=tk.WORD, state=tk.DISABLED)
encrypted_content.pack(pady=5)

#Etiketa per permbajtjen e dekriptuar
decrypted_label = tk.Label(main_frame, text="Permbajtja e Dekriptuar:")
decrypted_label.pack()

#Shiriti i skroll-it per dritaren e permbajtjes se dekriptuar
scrollbar = tk.Scrollbar(main_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#Dritarja tekstuale e permbajtjes se dekriptuar
decrypted_content = tk.Text(main_frame, height=10, width=100, wrap=tk.WORD, state=tk.DISABLED)
decrypted_content.pack(pady=5)
decrypted_content.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=decrypted_content.yview)

root.mainloop()