import tkinter as tk
from tkinter import filedialog, messagebox
import socket
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
def encrypt_file(file_path, key):
    with open(file_path, "rb") as f:
        data = f.read()
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return cipher.nonce, ciphertext, tag


def send_encrypted_file(file_path, server_ip, server_port, key_path):
    try:
        with open(key_path, "rb") as f:
            key = f.read()

        nonce, ciphertext, tag = encrypt_file(file_path, key)

        s = socket.socket()
        s.connect((server_ip, int(server_port)))
        s.sendall(nonce)
        s.sendall(tag)
        s.sendall(ciphertext)
        s.close()

        messagebox.showinfo("Başarılı", "Dosya şifrelenip gönderildi.")
    except Exception as e:
        messagebox.showerror("Hata", str(e))


def create_gui():
    root = tk.Tk()
    root.title("Güvenli Dosya Gönderimi (AES + TCP)")
    root.geometry("400x300")

    tk.Label(root, text="Sunucu IP:").pack()
    ip_entry = tk.Entry(root)
    ip_entry.insert(0, "127.0.0.1")
    ip_entry.pack()

    tk.Label(root, text="Sunucu Port:").pack()
    port_entry = tk.Entry(root)
    port_entry.insert(0, "5001")
    port_entry.pack()

    file_label = tk.Label(root, text="Seçili Dosya: Henüz seçilmedi")
    file_label.pack()

    def choose_file():
        file_path = filedialog.askopenfilename()
        if file_path:
            file_label.config(text=f"Seçili Dosya: {os.path.basename(file_path)}")
            file_label.file_path = file_path

    tk.Button(root, text="Dosya Seç", command=choose_file).pack()

    key_label = tk.Label(root, text="AES Anahtar Dosyası: Henüz seçilmedi")
    key_label.pack()

    def choose_key():
        key_path = filedialog.askopenfilename()
        if key_path:
            key_label.config(text=f"Anahtar: {os.path.basename(key_path)}")
            key_label.key_path = key_path

    tk.Button(root, text="Anahtar Seç", command=choose_key).pack()

    def send_file():
        file_path = getattr(file_label, 'file_path', None)
        key_path = getattr(key_label, 'key_path', None)
        if not file_path or not key_path:
            messagebox.showerror("Hata", "Lütfen dosya ve anahtar seçin.")
            return
        send_encrypted_file(file_path, ip_entry.get(), port_entry.get(), key_path)

    tk.Button(root, text="Gönder", command=send_file, bg="green", fg="white").pack(pady=10)

    root.mainloop()


if __name__ == '__main__':
    create_gui()
