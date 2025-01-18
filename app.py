from flask import Flask, render_template
import os
from skincare_routes import Skincare_Routes
from maquiagem_routes import Maquiagem_Routes
from produtos_routes import Produtos_Routes

skincareproducts = Skincare_Routes
maquiagemproducts = Maquiagem_Routes
products = Produtos_Routes

template_dir = os.path.abspath("templates")
app = Flask(__name__, template_folder=template_dir)

@app.route("/")
def index():
    skincare = skincareproducts.obter_produtos_skincare() 
    maquiagem = maquiagemproducts.obter_produtos_maquiagem()
    novidades = products.obter_produtos()
    return render_template("index.html", skincare=skincare, maquiagem=maquiagem, novidades=novidades)

@app.route("/skincare")
def skincare():
    return render_template("skincare.html")

@app.route("/maquiagem")
def maquiagem():
    return render_template("maquiagem.html")

# Executando o servidor
if __name__ == "__main__":
    app.run(debug=True)
