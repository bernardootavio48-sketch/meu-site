from flask import Flask, render_template
 import os # Importe o módulo os
app = Flask(__name__)

# Rota principal (Página Inicial)
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # O Render usa a variável de ambiente 'PORT'
    port = int(os.environ.get("PORT", 5000))
    # '0.0.0.0' permite que o site seja acessado externamente
    app.run(host='0.0.0.0', port=port)