from conection import conectar_db, define_rota
from flask import flash, Blueprint, request, redirect, session, render_template, url_for, jsonify
from login_required import login_required
from decimal import Decimal
import json
from users_routes import Users_Routes

search = Blueprint('search_route', __name__)


class Search_Routes:
    
    def buscar_produtos_search(self, nome_produto):
        db = conectar_db()
        cursor = db.cursor()
        
        query = """
        SELECT id, nome, valor, tipo_produto
        FROM produtos
        WHERE LOWER(nome) COLLATE utf8_general_ci LIKE LOWER(%s) 
        AND tipo_produto != "" AND tipo_produto is not null
        ORDER BY nome DESC;
        """

        cursor.execute(query, ('%' + nome_produto + '%',))  
        produtos = cursor.fetchall()
        cursor.close()
        db.close()

        produtos_decodificados = []
        for produto in produtos:
            id_produto = produto[0]
            nome_produto = produto[1].decode('utf-8') if isinstance(produto[1], bytearray) else produto[1]
            valor_produto = produto[2].decode('utf-8') if isinstance(produto[2], bytearray) else produto[2]
            tipo_produto = produto[3].decode('utf-8') if isinstance(produto[3], bytearray) else produto[3]

            produtos_decodificados.append({
                'id': id_produto,
                'nome': nome_produto,
                'valor': valor_produto,
                'tipo_produto': tipo_produto,
            })
            
        return produtos_decodificados
    
    def buscar_produtos_route_search(self):
        nome_produto = request.args.get('q', '').strip()  
        if nome_produto:
            produtos = self.buscar_produtos_search(nome_produto)
            return jsonify(produtos)
        return jsonify([])
        
@search.route('/search_products', methods=['GET'])
def search_products():
    return Search_Routes().buscar_produtos_route_search()
