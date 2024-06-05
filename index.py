from scapy.all import sniff, send, IP, UDP, TCP, DNS, DNSQR, DNSRR
from collections import defaultdict
import threading

dns_records = defaultdict(set)
port_scan_attempts = defaultdict(int)

def packet_callback(packet):
    # Анализируем DNS пакеты
    if packet.haslayer(DNS) and packet[DNS].qr == 1:  # Проверяем, является ли это ответом DNS
        dns_query = packet[DNS].qd.qname.decode('utf-8') if packet[DNS].qd else None
        dns_answer = packet[DNS].an.rdata if packet[DNS].an else None
        if dns_query and dns_answer:
            if dns_answer in dns_records[dns_query]:
                print(f"[ALERT] DNS Spoofing detected: {dns_query} -> {dns_answer}")
            dns_records[dns_query].add(dns_answer)
    
    # Анализируем попытки сканирования портов
    if packet.haslayer(TCP) and packet[TCP].flags == "S":  # Проверяем SYN пакеты
        src_ip = packet[IP].src
        port_scan_attempts[src_ip] += 1
        if port_scan_attempts[src_ip] > 10:  # Пороговое значение для определения сканирования
            print(f"[ALERT] Port scanning detected from IP: {src_ip}")

def capture_packets():
    sniff(prn=packet_callback, store=False)

def emulate_dns_spoofing(target_ip, spoofed_ip, domain):
    spoofed_packet = IP(dst=target_ip) / UDP(dport=53) / DNS(
        id=1, qr=1, aa=1, qd=DNSQR(qname=domain), an=DNSRR(rrname=domain, rdata=spoofed_ip)
    )
    send(spoofed_packet)
    print(f"Sent spoofed DNS response for {domain} to {target_ip} with IP {spoofed_ip}")

def emulate_port_scanning(target_ip, ports):
    for port in ports:
        syn_packet = IP(dst=target_ip) / TCP(dport=port, flags="S")
        send(syn_packet)
        print(f"Sent SYN packet to {target_ip}:{port}")

def start_packet_capture():
    capture_thread = threading.Thread(target=capture_packets)
    capture_thread.start()

# Запуск захвата пакетов
start_packet_capture()

# Пример использования функций эмуляции
emulate_dns_spoofing("192.168.1.10", "1.2.3.4", "ya.ru")
emulate_port_scanning("192.168.1.10", [22, 80, 443, 8080])
