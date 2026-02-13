from flask import Flask, render_template, request

# Klasör isimlerini buradaki gibi tanımlarsan hata almazsın kanki
app = Flask(__name__, 
            template_folder='templates', 
            static_folder='static')

@app.route('/')
def login():
    # templates klasörünün içindeki login.html'i arar
    return render_template('login.html')

@app.route('/panel')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
