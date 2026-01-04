from flask import Flask, render_template
import os

app = Flask(__name__)

# --- 1. MÁQUINAS GAMER ---
gamers = [
    {
        "nome": "PC Gamer Elite Aquário",
        "img": "pc-gamer-elite.png",  # Nome do arquivo na pasta static/img
        "badge": "Lançamento",
        "badge_class": "bg-success",
        "specs": [
            {"icon": "fas fa-cpu", "item": "Intel Core i7-3770"},
            {"icon": "fas fa-microchip", "item": "RX 580 8GB"},
            {"icon": "fas fa-memory", "item": "16GB RAM Dual Channel"},
            {"icon": "fas fa-fan", "item": "Gabinete Aquário + 5 Fans RGB"}
        ],
        "preco": "R$ 2.800,00", # Ajuste o preço se necessário
        "msg_zap": "Tenho interesse no PC Gamer Elite i7 com RX580"
    }
]

# --- 2. COMPUTADORES DE MESA (OFFICE) ---
office = [
    {
        "nome": "Desktop Pro-Work",
        "img": "pc-office.png",
        "badge": "Promoção",
        "badge_class": "bg-warning text-dark",
        "specs": [
            {"icon": "fas fa-cpu", "item": "Intel Core i5"},
            {"icon": "fas fa-hdd", "item": "SSD 240GB (Ultra Rápido)"},
            {"icon": "fab fa-windows", "item": "Windows 11 Pro Instalado"}
        ],
        "preco": "R$ 850,00",
        "msg_zap": "Tenho interesse no Desktop Pro-Work de R$ 850"
    }
]

# --- 3. MONITORES ---
monitores = [
    {
        "nome": "Monitor Mymax 19\" LED",
        "img": "monitor-mymax.png",
        "desc": "Conexão HDMI, 1440x900px, 3.6ms. Ideal para vídeos e tarefas ágeis.",
        "preco": "R$ 310,00",
        "msg_zap": "Quero o Monitor Mymax 19 polegadas"
    },
    {
        "nome": "Monitor Brazil PC 17.1\" HD",
        "img": "monitor-brazil.jpg",
        "desc": "Resolução HD, Conexão VGA. Acompanha cabos. Widescreen.",
        "preco": "R$ 270,00",
        "msg_zap": "Quero o Monitor Brazil PC 17.1"
    },
    {
        "nome": "Monitor Tronos 15.4\" LED",
        "img": "monitor-tronos.png",
        "desc": "Compacto e eficiente. Resolução 1280x800. Cabo incluso.",
        "preco": "R$ 260,00",
        "msg_zap": "Quero o Monitor Tronos 15.4"
    }
]

# --- 4. PERIFÉRICOS E KITS ---
perifericos = [
    {
        "nome": "Combo Lehmox LEY-2274",
        "img": "kit-lehmox.png",
        "desc": "Teclado 98% Semi-Mecânico + Mouse Colmeia HoneyComb. RGB Personalizável.",
        "preco": "R$ 170,00",
        "promo": "Leve com PC por R$ 150",
        "msg_zap": "Interesse no Combo Lehmox"
    },
    {
        "nome": "Kit Gamer Evolut White",
        "img": "kit-evolut.png",
        "desc": "Edição Branca. Teclado, Mouse, Headset e Mousepad. Setup completo!",
        "preco": "R$ 190,00",
        "promo": "Leve com PC por R$ 170",
        "msg_zap": "Interesse no Kit Evolut White"
    },
    {
        "nome": "Kit Gamer Alligator (Zoe)",
        "img": "kit-alligator.png",
        "desc": "Teclado Semi-Mecânico + Mouse 3200 DPI + Mousepad. Custo benefício.",
        "preco": "R$ 98,00",
        "promo": "Preço Promocional",
        "msg_zap": "Interesse no Kit Alligator"
    },
    {
        "nome": "Combo Gamer Thype RGB",
        "img": "kit-thype.png",
        "desc": "Mouse Ergonômico + Teclado Rainbow. Plug & Play.",
        "preco": "R$ 80,00",
        "promo": "Leve com PC por R$ 65",
        "msg_zap": "Interesse no Combo Thype"
    }
]

# --- 5. SEGURANÇA ---
seguranca = [
    {
        "nome": "Câmera Lente Dupla Icsee",
        "img": "camera-dupla.png",
        "desc": "Sem pontos cegos. Visão noturna, sensor de movimento e controle pelo App.",
        "preco": "R$ 180,00",
        "promo": "Leve outra peça e pague R$ 150",
        "msg_zap": "Interesse na Câmera Lente Dupla"
    },
    {
        "nome": "Câmera Wi-Fi PTZ 1080p",
        "img": "camera-ptz.png",
        "desc": "Rotação 355°, Resistente à água (IP66), Visão noturna 25m.",
        "preco": "R$ 280,00",
        "promo": "Leve outra peça e pague R$ 250",
        "msg_zap": "Interesse na Câmera PTZ"
    }
]

# --- ROTAS ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vendas')
def vendas():
    # Enviamos TODAS as listas para o HTML
    return render_template('vendas.html', 
                         gamers=gamers, 
                         office=office, 
                         monitores=monitores, 
                         perifericos=perifericos,
                         seguranca=seguranca)

@app.route('/assistencia')
def assistencia():
    return render_template('assistencia.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)