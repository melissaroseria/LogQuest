from flask import Flask, render_template, request, redirect, url_for, jsonify
import asyncio
import requests
import os

app = Flask(__name__, template_folder='dasboard', static_folder='css')

# 📦 Proxy Mühimmatı Çekme
def get_proxies_from_file():
    try:
        with open('proxy/get.txt', 'r') as f:
            urls = f.read().splitlines()
        all_proxies = []
        for url in urls:
            r = requests.get(url, timeout=5)
            if r.status_code == 200:
                all_proxies.extend(r.text.splitlines())
        return all_proxies[:250]
    except:
        return ["1.1.1.1:80"]

@app.route('/')
def login():
    return render_template('login.html') # Login sayfası

@app.route('/panel')
def dashboard():
    proxies = get_proxies_from_file()
    return render_template('index.html', proxies=proxies)

@app.route('/fire', methods=['POST'])
def start_fire():
    target = request.json.get('target')
    # Arka planda sinsi vuruş motorunu tetikle
    return jsonify({"status": "sis_modu_aktif", "message": f"{target} darlanıyor!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
