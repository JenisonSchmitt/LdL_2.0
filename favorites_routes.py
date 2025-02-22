from conection import conectar_db, define_rota
from flask import flash, Blueprint, request, redirect, session, render_template, url_for, jsonify
from login_required import login_required
from decimal import Decimal
import json
from users_routes import Users_Routes

favorites = Blueprint('favorites_routes', __name__)

class Favorites_Routes:
    
    @staticmethod
    def get_usuario_from_db_favorites(email):
        db = conectar_db()
        cursor = db.cursor()
        try:
            query = '''
                SELECT * FROM usuarios WHERE email = %s
            '''
            parameters = (email,)
            cursor.execute(query, parameters)
            result = cursor.fetchone()
    
            if result:
                columns = [column[0] for column in cursor.description]  
                usuario = dict(zip(columns, result))
                return usuario
            else:
                return None
        except Exception as e:
            return None
        finally:
            db.close()
            
    @staticmethod
    def get_favoritos_from_db_remove_favorites(email):
        db = conectar_db()
        cursor = db.cursor()
        try:
            query = "SELECT produtos_favoritos FROM usuarios WHERE email = %s"
            cursor.execute(query, (email,))
            row = cursor.fetchone()
            return row[0] if row else None 
        except Exception as e:
            return None
        finally:
            db.close()
            
    @staticmethod
    def atualizar_favoritos_remove(email, favoritos):
        db = conectar_db()
        cursor = db.cursor()
        try:
            query = "UPDATE usuarios SET produtos_favoritos = %s WHERE email = %s"
            cursor.execute(query, (favoritos, email))
            db.commit()
        except Exception as e:
            db.rollback()
        finally:
            db.close()

    @staticmethod
    def atualizar_favoritos(email, favoritos):
        db = conectar_db()
        cursor = db.cursor()
        try:
            query = '''
                UPDATE usuarios
                SET produtos_favoritos = %s
                WHERE email = %s
            '''
            parameters = (favoritos, email)
            cursor.execute(query, parameters)
            db.commit()
        except Exception as e:
            db.rollback()
        finally:
            db.close()
    
    @staticmethod
    def get_favorites_products(email):
        db = conectar_db()
        cursor = db.cursor()
        try:
            query = "SELECT produtos_favoritos FROM usuarios WHERE email = %s"
            cursor.execute(query, (email,))
            result = cursor.fetchone()
    
            if not result or not result[0]:  
                return []
    
            favoritos_ids = json.loads(result[0])
    
            if not favoritos_ids:
                return []
    
            query = f"SELECT id, nome, descricao, valor, tipo_produto FROM produtos WHERE id IN ({','.join(['%s'] * len(favoritos_ids))})"
            cursor.execute(query, tuple(favoritos_ids))
            produtos = cursor.fetchall()
            
            produtos_decodificados = []
            for produto in produtos:
                id_produto = produto[0]
                nome_produto = produto[1].decode('utf-8') if isinstance(produto[1], bytearray) else produto[1]
                descricao_produto = produto[2].decode('utf-8') if isinstance(produto[2], bytearray) else produto[2]
                valor_produto = produto[3]
                tipo_produto = produto[4].decode('utf-8') if isinstance(produto[4], bytearray) else produto[4]
    
                produtos_decodificados.append((id_produto, nome_produto, descricao_produto, valor_produto, tipo_produto))
            
            return produtos_decodificados
    
        except Exception as e:
            return []
        finally:
            db.close()


@favorites.route('/adicionar_favorito', methods=['POST'])
def adicionar_favorito():

    user_email = session.get('user_email')
    if user_email is None or not user_email:
        return jsonify({'success': False, 'message': 'Usuário não Logado!'})

    data = request.get_json()
    product_id = data.get('product_id')

    usuario = Favorites_Routes.get_usuario_from_db_favorites(user_email)
    if not usuario:
        return jsonify({'success': False, 'message': 'Usuário não encontrado'})

    produtos_favoritos = json.loads(usuario['produtos_favoritos'] or '[]') 
    if product_id not in produtos_favoritos:
        produtos_favoritos.append(product_id)

    Favorites_Routes.atualizar_favoritos(user_email, json.dumps(produtos_favoritos))

    return jsonify({'success': True, 'message': 'Produto adicionado aos favoritos!'})
    
    
@favorites.route('/products-favorite', methods=['GET', 'POST'])
@login_required
def products_favorite():
    user_email = session.get('user_email')

    produtos_favoritos = Favorites_Routes.get_favorites_products(user_email)
    
    return render_template("products-favorites.html", produtos_favoritos=produtos_favoritos)

@favorites.route("/remove-favorites/<int:produto_id>", methods=['GET', 'POST'])
@login_required
def remove_favorite(produto_id):
    user_email = session.get('user_email')

    favoritos_str = Favorites_Routes.get_favoritos_from_db_remove_favorites(user_email) or "[]"

    try:
        favoritos = json.loads(favoritos_str)
    except json.JSONDecodeError:
        favoritos = []

    if str(produto_id) in favoritos:
        favoritos.remove(str(produto_id))

    nova_lista = json.dumps(favoritos)
    Favorites_Routes.atualizar_favoritos_remove(user_email, nova_lista)

    flash("Produto excluído dos favoritos!", "success")
    return redirect(define_rota('/products-favorite'))