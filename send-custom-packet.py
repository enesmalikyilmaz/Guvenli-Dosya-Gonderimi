from scapy.all import IP, TCP, send

def send_custom_packet(target_ip, target_port):
    ip_layer = IP(dst=target_ip, ttl=42, flags="DF")  # TTL: 42 olarak ayarlanmıştır
    tcp_layer = TCP(dport=target_port, flags="S")     # SYN bayrağı
    packet = ip_layer / tcp_layer

    send(packet)
    print(f"[+] Paket gönderildi: {target_ip}:{target_port}")

# Test
send_custom_packet("8.8.8.8", 80)