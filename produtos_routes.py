from conection import conectar_db, define_rota
from flask import flash, Blueprint, request, redirect, session, render_template, url_for
from login_required import login_required
import json
from users_routes import Users_Routes

usersRoutes = Users_Routes()

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
    
    def save_first_data_cart(self, id_produto, qtd_produto, valor_total_produto, email):
        db = conectar_db()
        cursor = db.cursor()

        idUser = usersRoutes.getIdUserByEmail(email)

        if idUser is None:
            print("Erro: Usuário não encontrado.")
            return False

        query = """
            INSERT INTO vendas (id_produto, id_usuario, qtd_produto, dt_registro, valor_total_produto, temporario)
            VALUES (%s, %s, %s, NOW(), %s, 1)
        """

        try:
            cursor.execute(query, (id_produto, idUser, qtd_produto, valor_total_produto))
            db.commit()

            # Obtendo o ID gerado pela última inserção
            id_gerado = cursor.lastrowid
            return id_gerado  # Retorna o ID gerado
        except Exception as e:
            db.rollback()
            print(f"Erro ao salvar no banco: {e}")
            return False
        finally:
            cursor.close()
            db.close()
    
    def save_shipping_data(self, cep, rua, bairro, cidade, estado, numero, complemento, forma_envio, valor_total_compra, valor_frete, id_tabela):
        db = conectar_db()
        cursor = db.cursor()
        query = """
            UPDATE vendas 
            SET cep = %s, rua = %s, bairro = %s, cidade = %s, estado = %s, numero = %s, complemento = %s, forma_envio = %s, 
                valor_total_compra = %s, valor_frete = %s, dt_registro = NOW()
            WHERE id = %s
        """
        try:
            for id in id_tabela:
                cursor.execute(query, (cep, rua, bairro, cidade, estado, numero, complemento, forma_envio, valor_total_compra, valor_frete, id))
            
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            print(f"Erro ao salvar no banco: {e}")
            return False
        finally:
            cursor.close()
            db.close()

    def get_products_for_payments(self, id_tabela):
        db = conectar_db()
        cursor = db.cursor()

        query = """
            SELECT p.nome, p.tipo_produto, v.qtd_produto, v.forma_envio, v.cep, v.rua, v.bairro, v.cidade, v.estado, v.numero, v.complemento, v.valor_total_produto, v.valor_frete, v.valor_total_compra
            FROM vendas v
            JOIN produtos p ON v.id_produto = p.id
            WHERE v.id = %s
        """

        produtos_decodificados = []

        for id in id_tabela:
            cursor.execute(query, (id,))
            produtos = cursor.fetchall()

            for produto in produtos:
                nome_produto = produto[0].decode('utf-8') 
                tipo_produto = produto[1]
                qtd_produto = produto[2]
                forma_envio = produto[3]
                cep = produto[4]
                rua = produto[5]
                bairro = produto[6]
                cidade = produto[7]
                estado = produto[8]
                numero = produto[9]
                complemento = produto[10]
                valor_total_produto = produto[11]
                valor_frete = produto[12]
                valor_total_compra = produto[13]

                produto_decodificado = {
                    'nome_produto': nome_produto,
                    'tipo_produto': tipo_produto,
                    'qtd_produto': qtd_produto,
                    'forma_envio': forma_envio,
                    'cep': cep,
                    'rua': rua,
                    'bairro': bairro,
                    'cidade': cidade,
                    'estado': estado,
                    'numero': numero,
                    'complemento': complemento,
                    'valor_total_produto': valor_total_produto,
                    'valor_frete': valor_frete,
                    'valor_total_compra': valor_total_compra
                }
                produtos_decodificados.append(produto_decodificado)

        cursor.close()
        db.close()

        return produtos_decodificados

    def set_payment_cart(self, id_tabela, forma_pgmt):
        db = conectar_db()
        cursor = db.cursor()
        query = """
            UPDATE vendas
            SET forma_pagamento = %s, temporario = 0, dt_registro = NOW()
            WHERE id = %s
        """
        try:
            for id in id_tabela:
                cursor.execute(query, (forma_pgmt, id))
            
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            print(f"Erro ao salvar no banco: {e}")
            return False
        finally:
            cursor.close()
            db.close()


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

@produtos.route('/continue-purchase', methods=['POST'])
@login_required
def continue_purchase():
    produtos = []
    email = session.get('user_email')
    ids_gerados = []
    
    for key in request.form:
        if key.startswith("id_produto_"):
            produto_id = request.form[key]
            quantidade = request.form.get(f"quantidade_{produto_id}")
            valor_total = request.form.get(f"valor_total_{produto_id}")
            
            produtos.append({
                "id_produto": produto_id,
                "quantidade": quantidade,
                "valor_total": valor_total
            })

    produtoRoute = Produtos_Routes()
    
    for produto in produtos:
        resultado = produtoRoute.save_first_data_cart(produto['id_produto'], produto['quantidade'], produto['valor_total'], email)
        
        if not resultado:
            flash("Houve um problema ao salvar os dados, tente novamente!", "danger")
            return redirect(define_rota('/cart'))
        
        ids_gerados.append(resultado)

    return render_template("shipping-method.html", ids_gerados=ids_gerados)

@produtos.route('/shipping-method', methods=['POST'])
@login_required
def shipping_method(): 
    id_tabela = request.form.getlist('id_tabela[]')
    cep = request.form.get('cep')
    rua = request.form.get('rua')
    bairro = request.form.get('bairro')
    cidade = request.form.get('cidade')
    estado = request.form.get('estado')
    numero = request.form.get('numero')
    complemento = request.form.get('complemento')
    forma_envio = request.form.get('forma_envio')
    valor_total_compra = request.form.get('final_total') 
    valor_frete = request.form.get('shipping_value')

    if float(forma_envio) > 0:
        forma_envio = "Envio"
    else:
        forma_envio = "Retirada"

    produtoRoute = Produtos_Routes()
    try:
        resultado = produtoRoute.save_shipping_data(cep, rua, bairro, cidade, estado, numero, complemento, forma_envio, valor_total_compra, valor_frete, id_tabela)
        
        if resultado:
            session['id_tabela'] = id_tabela
            return redirect(define_rota('/payments')) 
        else:
            flash("Houve um erro ao processar sua solicitação, tente novamente!", "danger")
            return redirect(define_rota('/')) 

    except Exception as e:
        flash(f"Erro: {str(e)}", "danger")
        return redirect(define_rota('/'))
    
@produtos.route('/payments')
@login_required
def payments_forms():
    id_tabela = session.get('id_tabela')
    
    if not id_tabela:
        flash("Erro: Nenhum ID de tabela encontrado na sessão.", "danger")
        return redirect(define_rota('/'))
    
    produtoRoute = Produtos_Routes()

    try:
        produtos = produtoRoute.get_products_for_payments(id_tabela)
        
        if produtos:
            return render_template('payments.html', produtos=produtos)
        else:
            flash("Nenhum produto encontrado para o pagamento.", "danger")
            return redirect(define_rota('/'))

    except Exception as e:
        flash(f"Erro ao carregar os produtos: {str(e)}", "danger")
        return redirect(define_rota('/'))

@produtos.route('/submit_payment', methods=['POST'])
@login_required
def submit_payment():
    id_tabela = session.get('id_tabela')

    if not id_tabela:
        flash("Erro: Nenhum ID de tabela encontrado na sessão.", "danger")
        return redirect(define_rota('/'))
    
    forma_pgmt = request.form.get('forma-pagamento')

    produtoRoute = Produtos_Routes()

    try:
        pagamento_concluído = produtoRoute.set_payment_cart(id_tabela, forma_pgmt)
        
        if pagamento_concluído:
            flash("Compra Finalizada com Sucesso!", "success")
            session['id_tabela'] = None
            return redirect(define_rota('/'))
        else:
            flash("Erro ao finalizar compra!", "danger")
            return redirect(define_rota('/'))

    except Exception as e:
        flash(f"Erro ao carregar os produtos: {str(e)}", "danger")
        return redirect(define_rota('/'))