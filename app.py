from flask import Flask, render_template, session, redirect, url_for, request
import os

app = Flask(__name__)
# IMPORTANTE: Chave secreta para o carrinho funcionar (pode ser qualquer texto aleatório)
app.secret_key = 'tavinn-ti-segredo-chave-super-secreta'

# --- SEUS PRODUTOS (Mantenha suas listas aqui, vou resumir para o exemplo) ---
# DICA: Adicionei um 'id' único para cada produto para o carrinho saber qual é qual.
gamers = [
    {"id": "g1", "nome": "PC Gamer Elite Aquário", "img": "pc-gamer-elite.jpg", "preco_num": 2800.00, "preco": "R$ 2.800,00", "specs": [...]},
    # ... seus outros gamers
]
office = [
    {"id": "o1", "nome": "Desktop Pro-Work", "img": "pc-office.jpg", "preco_num": 850.00, "preco": "R$ 850,00", "specs": [...]}
]
# ... faça o mesmo para monitores, periféricos (adicione 'id' e 'preco_num')

# Função auxiliar para buscar produto pelo ID
def buscar_produto(id_produto):
    todas_listas = gamers + office # + monitores + perifericos (junte todas aqui)
    for prod in todas_listas:
        if prod['id'] == id_produto:
            return prod
    return None

# --- ROTAS ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vendas')
def vendas():
    return render_template('vendas.html', gamers=gamers, office=office) # Adicione as outras listas

# --- LÓGICA DO CARRINHO ---

@app.route('/adicionar/<id_produto>')
def adicionar_carrinho(id_produto):
    # Cria o carrinho se não existir
    if 'carrinho' not in session:
        session['carrinho'] = []
    
    # Adiciona o ID do produto na lista
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
    # Aqui você receberia os dados do formulário
    nome = request.form.get('nome')
    whatsapp = request.form.get('whatsapp')
    # Em um sistema real, aqui integraria com Mercado Pago ou salvaria no Banco de Dados
    
    # Por enquanto, vamos simular limpando o carrinho e agradecendo
    session.pop('carrinho', None)
    return render_template('sucesso.html', nome=nome)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)