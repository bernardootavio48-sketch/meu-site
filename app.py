from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    # --- LISTA DE PCS GAMER ---
    gamers = [
        {
            "nome": "PC Gamer Elite I",
            "badge": "Top Vendas",
            "badge_class": "", # Usa a cor padrão do CSS
            "specs": [
                {"icon": "fas fa-cpu", "item": "Intel i7 13ª Geração"},
                {"icon": "fas fa-microchip", "item": "RX 580 8GB"},
                {"icon": "fas fa-memory", "item": "16GB RAM DDR3"}
            ],
            "preco": "R$ 2.800,00",
            "msg_zap": "Olá! Tenho interesse no PC Gamer Elite I"
        },
        # Para adicionar outro PC, é só copiar o bloco acima, colar aqui e mudar os dados!
    ]

    # --- LISTA DE ESCRITÓRIO ---
    office = [
        {
            "nome": "Desktop Pro-Work",
            "badge": "Melhor Custo Benefício",
            "badge_class": "bg-warning text-dark", # Amarelo do Bootstrap
            "specs": [
                {"icon": "fas fa-cpu", "item": "Intel Core i5"},
                {"icon": "fas fa-hdd", "item": "SSD 240GB"},
                {"icon": "fab fa-windows", "item": "Windows 11 Pro"}
            ],
            "preco": "R$ 850,00",
            "msg_zap": "Olá! Tenho interesse no Desktop Pro-Work"
        }
    ]

    # Enviamos as listas para o HTML
    return render_template('index.html', gamers=gamers, office=office)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)