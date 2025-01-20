from flask import Flask, render_template, request, redirect, url_for
import os
from skincare_routes import Skincare_Routes
from maquiagem_routes import Maquiagem_Routes
from produtos_routes import Produtos_Routes
from users_routes import Users_Routes
import logging

# logging.basicConfig(filename='/home/u228502032/domains/testeecommerce.shop/public_html/app.log', level=logging.INFO)
# logging.info('Iniciando o app.py...')


skincareproducts = Skincare_Routes
maquiagemproducts = Maquiagem_Routes
products = Produtos_Routes

template_dir = os.path.abspath("templates")
app = Flask(__name__, template_folder=template_dir)
app.secret_key = os.urandom(24)

@app.route("/")
def index():
    skincare = skincareproducts.obter_produtos_skincare() 
    maquiagem = maquiagemproducts.obter_produtos_maquiagem()
    novidades = products.obter_produtos()
    return render_template("index.html", skincare=skincare, maquiagem=maquiagem, novidades=novidades)

@app.route("/skincare")
def skincare():
    tipos_produtos = skincareproducts.obter_tipos_skincare()
    skincare = skincareproducts.obter_produtos_skincare()
    return render_template("skincare.html", tipos_produtos=tipos_produtos, skincare=skincare)

@app.route("/maquiagem")
def maquiagem():
    tipos_produtos = maquiagemproducts.obter_tipos_maquiagem()
    maquiagem = maquiagemproducts.obter_produtos_maquiagem()
    return render_template("maquiagem.html", tipos_produtos=tipos_produtos, maquiagem=maquiagem)

@app.route("/produtos/<int:id>")
def produtos(id):
    produtos = products.mostrar_detalhes_produtos(id)
    return render_template("produtos.html", produtos=produtos)

@app.route("/create_user")
def create_user():
    return render_template("create_user.html")

@app.route("/submit_create_user", methods=["POST"])
def insert_user():
    CPF = request.form['CPF']
    nome = request.form['nome']
    telefone = request.form['telefone']
    email = request.form['email']
    nascimento = request.form['nascimento']
    rua = request.form['rua']
    numero = request.form['numero']
    complemento = request.form['complemento']
    cep = request.form['cep']
    cidade = request.form['cidade']
    estado = request.form['estado']
    senha = request.form['confirme-senha']
    print(senha)

    users_routes = Users_Routes()

    users_routes.insert_user()

    return redirect(url_for('index'))


def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, headers)
    return [b"Meu app Python funcionando com WSGI!"]

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
