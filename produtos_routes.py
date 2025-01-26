from conection import conectar_db, define_rota
from flask import flash, Blueprint, request, redirect, session, render_template, jsonify
from login_required import login_required
import json

produtos = Blueprint('produtos_routes', __name__)

class Produtos_Routes:
    
    # Função para buscar os produtos mais vendidos
    def obter_produtos():
        db = conectar_db()
        cursor = db.cursor()

        query = "SELECT id, nome, valor, tipo_produto, imagem FROM produtos WHERE dt_cadastro >= '2025-01-01 00:00:00' ORDER BY dt_cadastro DESC LIMIT 8"
        cursor.execute(query)
        
        produtos = cursor.fetchall()
        cursor.close()
        db.close()

        produtos_decodificados = []
        for produto in produtos:
            id_produto = produto[0]
            nome_produto = produto[1].decode('utf-8') if isinstance(produto[1], bytearray) else produto[1]
            valor_produto = produto[2].decode('utf-8') if isinstance(produto[2], bytearray) else produto[2]
            tipo_produto = produto[3].decode('utf-8') if isinstance(produto[3], bytearray) else produto[3]
            imagem_produto = produto[4].decode('utf-8') if isinstance(produto[4], bytearray) else produto[4]

            produtos_decodificados.append((id_produto, nome_produto, valor_produto, tipo_produto, imagem_produto))
        
        return produtos_decodificados
    
    def mostrar_detalhes_produtos(id):
        db = conectar_db()
        cursor = db.cursor()
        id = int(id)

        query = "SELECT p.id, p.nome, p.descricao, p.valor, p.tipo_produto, tp.nome, p.imagem FROM produtos p INNER JOIN tipo_produtos tp ON p.tipo = tp.id WHERE p.id = %s"
        cursor.execute(query, (id,))

        produtos = cursor.fetchall()
        cursor.close()
        db.close()

        produtos_decodificados = []
        for produto in produtos:
            id_produto = produto[0]
            nome_produto = produto[1].decode('utf-8') if isinstance(produto[1], bytearray) else produto[1]
            descricao_produto = produto[2].decode('utf-8')
            valor_produto = produto[3]
            tipo_produto = produto[4].decode('utf-8') if isinstance(produto[4], bytearray) else produto[4]
            tipo_produtos = produto[5].decode('utf-8') if isinstance(produto[5], bytearray) else produto[5]
            imagem_produto = produto[6].decode('utf-8') if isinstance(produto[6], bytearray) else produto[6]
            produtos_decodificados.append((id_produto, nome_produto, descricao_produto, valor_produto, tipo_produto, tipo_produtos, imagem_produto))

        return produtos_decodificados
    
    def get_products_cart(self, product_ids):
        db = conectar_db()
        cursor = db.cursor()

        # Gera placeholders para a quantidade de IDs fornecidos, ex: (%s, %s, %s)
        placeholders = ', '.join(['%s'] * len(product_ids))

        query = f"""
            SELECT p.id, p.nome, p.descricao, p.valor, p.tipo_produto, tp.nome, p.imagem 
            FROM produtos p 
            INNER JOIN tipo_produtos tp ON p.tipo = tp.id 
            WHERE p.id IN ({placeholders})
        """
        cursor.execute(query, product_ids)

        produtos = cursor.fetchall()
        cursor.close()
        db.close()

        produtos_decodificados = []
        for produto in produtos:
            id_produto = produto[0]
            nome_produto = produto[1].decode('utf-8') if isinstance(produto[1], bytearray) else produto[1]
            descricao_produto = produto[2].decode('utf-8') if isinstance(produto[2], bytearray) else produto[2]
            valor_produto = float(produto[3]) 
            tipo_produto = produto[4].decode('utf-8') if isinstance(produto[4], bytearray) else produto[4]
            tipo_produtos = produto[5].decode('utf-8') if isinstance(produto[5], bytearray) else produto[5]
            imagem_produto = produto[6].decode('utf-8') if isinstance(produto[6], bytearray) else produto[6]

            produtos_decodificados.append((
                id_produto, nome_produto, descricao_produto, valor_produto, 
                tipo_produto, tipo_produtos, imagem_produto
            ))

        return produtos_decodificados

@produtos.route("/cart", methods=['POST'])
@login_required
def cart():
    product_ids = json.loads(request.form['product_ids'])
    product_quantities = json.loads(request.form['product_quantities'])

    produtoRouter = Produtos_Routes()
    produtos_decodificados = produtoRouter.get_products_cart(product_ids)

    produtos_dict = {produto[0]: produto for produto in produtos_decodificados}

    produtos_ordenados = [produtos_dict[int(id)] for id in product_ids]

    produtos_com_quantidade = []
    for produto, quantidade in zip(produtos_ordenados, product_quantities):
        produtos_com_quantidade.append((*produto, quantidade))

    return render_template('cart.html', product_cart=produtos_com_quantidade)
