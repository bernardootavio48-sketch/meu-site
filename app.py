from flask import Flask, render_template, session, redirect, url_for, request
import os

app = Flask(__name__)
# Chave de segurança para o carrinho
app.secret_key = 'tavinn-ti-chave-secreta-segura'

# --- 1. MÁQUINAS GAMER ---
gamers = [
    {
        "id": "g1",
        "nome": "PC Gamer Elite Aquário",
        "img": "pc-gamer-elite.png",
        "badge": "Lançamento",
        "badge_class": "bg-success",
        "specs": [
            {"icon": "fas fa-cpu", "item": "Intel Core i7-3770"},
            {"icon": "fas fa-microchip", "item": "RX 580 8GB"},
            {"icon": "fas fa-memory", "item": "16GB RAM Dual Channel"},
            {"icon": "fas fa-fan", "item": "Gabinete Aquário + 5 Fans RGB"}
        ],
        "desc_longa": "Domine seus jogos favoritos com o PC Gamer Elite. Equipado com processador i7 e placa de vídeo dedicada, ele oferece desempenho fluido em Full HD. O gabinete aquário garante um visual incrível para o seu setup.",
        "preco": "R$ 2.800,00",
        "preco_num": 2800.00,
        "msg_zap": "Tenho interesse no PC Gamer Elite i7 com RX580"
    }
]

# --- 2. COMPUTADORES DE MESA (OFFICE) ---
office = [
    {
        "id": "o1",
        "nome": "Desktop Pro-Work",
        "img": "pc-office.png",
        "badge": "Promoção",
        "badge_class": "bg-warning text-dark",
        "specs": [
            {"icon": "fas fa-cpu", "item": "Intel Core i5"},
            {"icon": "fas fa-hdd", "item": "SSD 240GB (Ultra Rápido)"},
            {"icon": "fab fa-windows", "item": "Windows 11 Pro Instalado"}
        ],
        "desc_longa": "Ideal para escritórios e home office. A velocidade do SSD combinada com o processador i5 garante que você não perca tempo abrindo programas.",
        "preco": "R$ 850,00",
        "preco_num": 850.00,
        "msg_zap": "Tenho interesse no Desktop Pro-Work de R$ 850"
    }
]

# --- 3. MONITORES ---
monitores = [
    {
        "id": "m1",
        "nome": "Monitor Mymax 19\" LED",
        "img": "monitor-mymax.png",
        "desc": "Conexão HDMI, 1440x900px, 3.6ms. Ideal para vídeos e tarefas ágeis.",
        "preco": "R$ 310,00",
        "preco_num": 310.00,
        "msg_zap": "Quero o Monitor Mymax 19 polegadas"
    },
    {
        "id": "m2",
        "nome": "Monitor Brazil PC 17.1\" HD",
        "img": "monitor-brazil.png",
        "desc": "Resolução HD, Conexão VGA. Acompanha cabos. Widescreen.",
        "preco": "R$ 270,00",
        "preco_num": 270.00,
        "msg_zap": "Quero o Monitor Brazil PC 17.1"
    },
    {
        "id": "m3",
        "nome": "Monitor Tronos 15.4\" LED",
        "img": "monitor-tronos.png",
        "desc": "Compacto e eficiente. Resolução 1280x800. Cabo incluso.",
        "preco": "R$ 260,00",
        "preco_num": 260.00,
        "msg_zap": "Quero o Monitor Tronos 15.4"
    }
]

# --- 4. PERIFÉRICOS E KITS ---
perifericos = [
    {
        "id": "p1",
        "nome": "Combo Lehmox LEY-2274",
        "img": "kit-lehmox.png",
        "desc": "Teclado 98% Semi-Mecânico + Mouse Colmeia HoneyComb. RGB Personalizável.",
        "preco": "R$ 170,00",
        "preco_num": 170.00,
        "promo": "Leve com PC por R$ 150",
        "msg_zap": "Interesse no Combo Lehmox"
    },
    {
        "id": "p2",
        "nome": "Kit Gamer Evolut White",
        "img": "kit-evolut.png",
        "desc": "Edição Branca. Teclado, Mouse, Headset e Mousepad. Setup completo!",
        "preco": "R$ 190,00",
        "preco_num": 190.00,
        "promo": "Leve com PC por R$ 170",
        "msg_zap": "Interesse no Kit Evolut White"
    },
    {
        "id": "p3",
        "nome": "Kit Gamer Alligator (Zoe)",
        "img": "kit-alligator.png",
        "desc": "Teclado Semi-Mecânico + Mouse 3200 DPI + Mousepad. Custo benefício.",
        "preco": "R$ 98,00",
        "preco_num": 98.00,
        "promo": "Preço Promocional",
        "msg_zap": "Interesse no Kit Alligator"
    },
    {
        "id": "p4",
        "nome": "Combo Gamer Thype RGB",
        "img": "kit-thype.png",
        "desc": "Mouse Ergonômico + Teclado Rainbow. Plug & Play.",
        "preco": "R$ 80,00",
        "preco_num": 80.00,
        "promo": "Leve com PC por R$ 65",
        "msg_zap": "Interesse no Combo Thype"
    }
]

# --- 5. SEGURANÇA ---
seguranca = [
    {
        "id": "s1",
        "nome": "Câmera Lente Dupla Icsee",
        "img": "camera-dupla.png",
        "desc": "Sem pontos cegos. Visão noturna, sensor de movimento e controle pelo App.",
        "preco": "R$ 180,00",
        "preco_num": 180.00,
        "promo": "Leve outra peça e pague R$ 150",
        "msg_zap": "Interesse na Câmera Lente Dupla"
    },
    {
        "id": "s2",
        "nome": "Câmera Wi-Fi PTZ 1080p",
        "img": "camera-ptz.png",
        "desc": "Rotação 355°, Resistente à água (IP66), Visão noturna 25m.",
        "preco": "R$ 280,00",
        "preco_num": 280.00,
        "promo": "Leve outra peça e pague R$ 250",
        "msg_zap": "Interesse na Câmera PTZ"
    }
]

# --- LISTA DO INSTAGRAM (Feed Manual) ---
posts_insta = [
    {"img": "pc-gamer-elite.png", "link": "https://instagram.com/tavinn_00", "desc": "Setup White Edition montado para cliente!"},
    {"img": "pc-gamer-elite.png", "link": "https://instagram.com/tavinn_00", "desc": "Detalhe da RX 580 no gabinete aquário."},
    {"img": "pc-office.png", "link": "https://instagram.com/tavinn_00", "desc": "Manutenção completa feita hoje."},
    {"img": "kit-evolut.png", "link": "https://instagram.com/tavinn_00", "desc": "Mais um PC Gamer Elite saindo!"}
]

# Função para encontrar produto pelo ID
def buscar_produto(id_produto):
    todas_listas = gamers + office + monitores + perifericos + seguranca
    for prod in todas_listas:
        if prod['id'] == id_produto:
            return prod
    return None

# --- ROTAS ---

@app.route('/')
def index():
    return render_template('index.html', posts=posts_insta)

@app.route('/vendas')
def vendas():
    return render_template('vendas.html', 
                         gamers=gamers, 
                         office=office, 
                         monitores=monitores, 
                         perifericos=perifericos,
                         seguranca=seguranca)

# ESTA ROTA FOI ADICIONADA/CORRIGIDA PARA EVITAR O ERRO 500
@app.route('/produto/<id_produto>')
def ver_produto(id_produto):
    prod = buscar_produto(id_produto)
    if not prod:
        return redirect(url_for('vendas'))
    return render_template('produto.html', produto=prod)

@app.route('/assistencia')
def assistencia():
    return render_template('assistencia.html')

# --- CARRINHO ---

@app.route('/adicionar/<id_produto>')
def adicionar_carrinho(id_produto):
    if 'carrinho' not in session:
        session['carrinho'] = []
    
    session['carrinho'].append(id_produto)
    session.modified = True
    return redirect(url_for('ver_carrinho'))

@app.route('/carrinho')
def ver_carrinho():
    itens = []
    total = 0
    if 'carrinho' in session:
        for id_prod in session['carrinho']:
            prod = buscar_produto(id_prod)
            if prod:
                itens.append(prod)
                total += prod['preco_num']
    
    return render_template('carrinho.html', itens=itens, total=total)

@app.route('/limpar')
def limpar_carrinho():
    session.pop('carrinho', None)
    return redirect(url_for('vendas'))

@app.route('/finalizar', methods=['POST'])
def finalizar_compra():
    nome = request.form.get('nome')
    session.pop('carrinho', None) # Limpa o carrinho
    return render_template('sucesso.html', nome=nome)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)