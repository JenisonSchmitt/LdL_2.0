from flask import Flask, render_template, request, redirect, url_for, flash, session, Blueprint
import os
from skincare_routes import Skincare_Routes
from maquiagem_routes import Maquiagem_Routes
from produtos_routes import Produtos_Routes
from users_routes import users, Users_Routes
from login_required import login_required
import logging

logging.basicConfig(filename='/home/u228502032/domains/testeecommerce.shop/public_html/app.log', level=logging.INFO)
logging.info('Iniciando o app.py...')

skincareproducts = Skincare_Routes
maquiagemproducts = Maquiagem_Routes
products = Produtos_Routes

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=template_dir)
app.secret_key = os.urandom(24)
app.register_blueprint(users)

@app.route("/")
def index():
    skincare = skincareproducts.obter_produtos_skincare_mais_vendidos() 
    maquiagem = maquiagemproducts.obter_produtos_maquiagem_mais_vendidos()
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

@app.route("/create-user")
def create_user():
    return render_template("create-user.html")
    
@app.route("/account")
def account():
    if 'user_email' not in session:
        return render_template("account.html") 
    else:
        return redirect('https://testeecommerce.shop/acess-account')
        
@app.route("/esqueci-senha")
def rec_senha():
    return render_template("esqueci-senha.html")

@app.route("/acess-account")
@login_required
def acess_account():
    users_routes = Users_Routes()
    
    usuario = users_routes.get_usuario_from_db(session.get('user_email'))
    return render_template('acess-account.html', usuario=usuario)
        
@app.route("/logout")
def logout():
    session.pop('user_email', None)
    flash("Você foi desconectado com sucesso.", "success")
    return redirect('https://testeecommerce.shop')


def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, headers)
    return [b"Meu app Python funcionando com WSGI!"]

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
