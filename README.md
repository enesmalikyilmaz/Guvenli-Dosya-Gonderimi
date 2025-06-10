# 🔐 Güvenli Dosya Gönderimi

Bu proje, Bilgisayar Mühendisliği 3. sınıf **Bilgisayar Ağları** dersi kapsamında geliştirilmiş bir güvenli dosya aktarım sistemidir. Sistem, kullanıcı dostu bir arayüz üzerinden AES şifreleme ile veri aktarımı sağlar. Ayrıca IP seviyesinde düşük seviyeli kontrol, ağ performans testi ve trafik analizi özelliklerini de içerir.

## 📌 Proje Özeti

| Bileşen                 | Açıklama |
|-------------------------|----------|
| 🔒 AES Şifreleme        | Dosyalar EAX modunda şifrelenir (nonce + tag ile bütünlük sağlanır). |
| 📡 TCP Aktarımı         | Veriler güvenli ve sıralı şekilde sunucuya gönderilir. |
| 📶 Scapy Paket Üretimi  | Özel IP başlığına sahip paketler (TTL, DF, SYN) oluşturulur. |
| 🔬 Wireshark Analizi    | Şifrelenmiş veri paketlerinin içerikleri okunamaz. |
| 📈 iPerf3 Testi         | Bant genişliği ve aktarım hızı ölçülür. |
| 🖥️ GUI Arayüz           | tkinter ile kullanıcı dostu arayüz sağlanır. |

## 📁 Proje Yapısı
secure-file-transfer/
├── client.py
├── server.py
├── secure_file_transfer_gui.py
├── send_custom_packet.py
├── key.bin
├── testfile.txt
└── README.md


## ⚙️ Gereksinimler

- Python 3.7+
- Wireshark
- iPerf3
- Python kütüphaneleri:

```bash
pip install pycryptodome scapy
```

▶️ Kullanım
🔑 1. AES Anahtar Dosyası Oluştur
```bash
from Crypto.Random import get_random_bytes
with open("key.bin", "wb") as f:
    f.write(get_random_bytes(16))
```
🖥️ 2. Sunucuyu Başlat
```bash
python server.py
```
📤 3. GUI ile Dosya Gönder
```bash
python secure_file_transfer_gui.py
```

IP: 127.0.0.1

Port: 5001

Dosya ve anahtar dosyası seçildikten sonra Gönder tuşuna basılır.

🧠 Öğrenilenler
TCP üzerinden dosya gönderimi

AES ile veri şifreleme ve bütünlük doğrulama

IP header manipülasyonu (Scapy)

Wireshark ile trafik analiz becerisi

iPerf3 ile performans testi

tkinter ile grafiksel kullanıcı arayüzü geliştirme

📄 Rapor Özeti
Giriş
Bu proje, veri aktarımı sırasında şifreleme ve paket analizinin önemini göstermek amacıyla oluşturulmuştur. Geliştirilen sistem; AES şifreleme, TCP aktarımı, GUI, IP paketi işleme ve trafik analizi gibi modüllerden oluşur.

Teknik Özellikler
AES EAX modunda güvenli şifreleme

socket kütüphanesiyle TCP bağlantısı

IP paketlerinde manuel TTL ve bayrak kontrolü

iPerf3 ile performans ölçümü

Wireshark ile ağ trafiği gözlemi

Sınırlılıklar ve Geliştirme Alanları
Uygulama katmanında parçalama/birleştirme yapılmamıştır.

GUI yalnızca istemci tarafında uygulanmıştır.

UDP desteği ve gelişmiş loglama eklenebilir.

🧾 Lisans
Bu proje akademik amaçla geliştirilmiştir ve açık kaynaklıdır.

👨‍💻 Geliştirici
Enes Malik Yılmaz
Bilgisayar Mühendisliği 3. Sınıf
2025 Bahar Dönemi – Bilgisayar Ağları Dersi
