import socket
from Crypto.Cipher import AES

def decrypt_data(nonce, ciphertext, tag, key):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag)

def start_server(host='0.0.0.0', port=5001):
    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    print("[*] Sunucu başlatıldı. Bekleniyor...")

    conn, addr = s.accept()
    print(f"[+] Bağlantı kuruldu: {addr}")

    nonce = conn.recv(16)
    tag = conn.recv(16)
    ciphertext = conn.recv(4096)

    with open("key.bin", "rb") as f:
        key = f.read()

    data = decrypt_data(nonce, ciphertext, tag, key)
    with open("received_file.txt", "wb") as f:
        f.write(data)
    print("[+] Dosya başarıyla alındı ve kaydedildi.")

    conn.close()

start_server()
