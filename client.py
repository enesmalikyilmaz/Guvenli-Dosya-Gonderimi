import socket
from Crypto.Cipher import AES

def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return cipher.nonce, ciphertext, tag

def send_file(filename, server_ip, server_port=5001):
    with open(filename, "rb") as f:
        data = f.read()

    with open("key.bin", "rb") as f:
        key = f.read()

    nonce, ciphertext, tag = encrypt_data(data, key)

    s = socket.socket()
    s.connect((server_ip, server_port))
    s.sendall(nonce)
    s.sendall(tag)
    s.sendall(ciphertext)
    print("[+] Dosya şifrelenip gönderildi.")
    s.close()

send_file("testfile.txt", "127.0.0.1")  # Yerel IP adresi
