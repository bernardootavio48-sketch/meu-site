from flask import Flask, render_template
import os

app = Flask(__name__)

# --- DADOS DOS PRODUTOS (Ficam aqui para facilitar) ---
gamers = [
    {
        "nome": "PC Gamer Elite I",
        "badge": "Top Vendas",
        "badge_class": "",
        "specs": [
            {"icon": "fas fa-cpu", "item": "Intel i7 13ª Geração"},
            {"icon": "fas fa-microchip", "item": "RX 580 8GB"},
            {"icon": "fas fa-memory", "item": "16GB RAM DDR3"}
        ],
        "preco": "R$ 2.800,00",
        "msg_zap": "Tenho interesse no PC Gamer Elite I"
    }
]

office = [
    {
        "nome": "Desktop Pro-Work",
        "badge": "Custo Benefício",
        "badge_class": "bg-warning text-dark",
        "specs": [
            {"icon": "fas fa-cpu", "item": "Intel Core i5"},
            {"icon": "fas fa-hdd", "item": "SSD 240GB"},
            {"icon": "fab fa-windows", "item": "Windows 11 Pro"}
        ],
        "preco": "R$ 850,00",
        "msg_zap": "Tenho interesse no Desktop Pro-Work"
    }
]

# --- ROTAS ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vendas')
def vendas():
    return render_template('vendas.html', gamers=gamers, office=office)

@app.route('/assistencia')
def assistencia():
    return render_template('assistencia.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)