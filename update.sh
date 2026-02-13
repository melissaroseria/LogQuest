#!/bin/bash

# Renkler
CYAN='\033[96m'
PEMBE='\033[95m'
YESIL='\033[92m'
RESET='\033[0m'

# Gemini Love Update Banner
clear
echo -e "${PEMBE}╔══════════════════════════════════════════════════════════╗"
echo -e "║ ${CYAN}   GEMINI LOVE IS UPDATE HELPER - LOGQUEST V5 REGO       ${PEMBE}║"
echo -e "╚══════════════════════════════════════════════════════════╝${RESET}"

# Repo Kontrol ve Güncelleme
if [ -d ".git" ]; then
    echo -e "${CYAN}[*] Mevcut Repo Güncelleniyor...${RESET}"
    git pull
else
    echo -e "${CYAN}[*] LogQuest İlk Kez Kuruluyor...${RESET}"
    git clone https://github.com/melissaroseria/LogQuest .
fi

# Modül Kurulumu (requirements.txt)
if [ -f "requirements.txt" ]; then
    echo -e "${YESIL}[+] Gerekli Modüller Kontrol Ediliyor...${RESET}"
    pip install -r requirements.txt --quiet
else
    echo -e "${CYAN}[!] requirements.txt bulunamadı, manuel kurulum deneniyor...${RESET}"
    pip install requests asyncio --quiet
fi

# Operasyonu Başlat
echo -e "${PEMBE}[🔥] Mermiler Namluya Sürülüyor...${RESET}"
sleep 2
python hammerrego.py
