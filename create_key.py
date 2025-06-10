# create_key.py
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)  # 16 bytes = 128 bit
with open("key.bin", "wb") as f:
    f.write(key)
print("[+] Anahtar oluşturuldu.")
