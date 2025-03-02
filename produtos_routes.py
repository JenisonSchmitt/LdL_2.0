from conection import conectar_db, define_rota
from flask import flash, Blueprint, request, redirect, session, render_template, url_for
from login_required import login_required
from decimal import Decimal
import json
from users_routes import Users_Routes
from emails_routes import Email_Routes

usersRoutes = Users_Routes()

produtos = Blueprint('produtos_routes', __name__)

class Produtos_Routes:
    
    # Função para buscar os produtos mais novos
    def obter_produtos():
        db = conectar_db()
        cursor = db.cursor()
        
        query = """SELECT p.id, p.nome, p.valor, p.tipo_produto, p.imagem, p.qtd_comprada, COALESCE(SUM(v.qtd_produto), 0) AS qtd_vendida, p.variacao
            FROM produtos p 
            LEFT JOIN vendas v ON p.id = v.id_produto AND v.obs IS NOT NULL AND v.id_pagamento IS NOT NULL AND v.forma_pagamento IS NOT NULL
            WHERE p.dt_cadastro >= '2025-01-01 00:00:00'
            GROUP BY p.id
            ORDER BY p.dt_cadastro DESC
            LIMIT 8;
        """
        
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
            qtd_comprada = produto[5]
            qtd_vendida = produto[6]
            variacao = produto[7].decode('utf-8') if isinstance(produto[7], bytearray) else produto[7]

            produtos_decodificados.append((id_produto, nome_produto, valor_produto, tipo_produto, imagem_produto, qtd_comprada, qtd_vendida, variacao))
        
        return produtos_decodificados
    
    def mostrar_detalhes_produtos(id):
        db = conectar_db()
        cursor = db.cursor()
        id = int(id)
        
        query = """SELECT p.id, p.nome, p.descricao, p.valor, p.tipo_produto, tp.nome, p.imagem, p.qtd_comprada, COALESCE(SUM(v.qtd_produto), 0) AS qtd_vendida, p.variacao
        FROM produtos p
        LEFT JOIN vendas v ON p.id = v.id_produto AND v.obs IS NOT NULL AND v.id_pagamento IS NOT NULL AND v.forma_pagamento IS NOT NULL
        INNER JOIN tipo_produtos tp ON p.tipo = tp.id
        WHERE p.id = %s
        GROUP BY p.id, tp.nome"""
        
        cursor.execute(query, (id,))
        produtos = cursor.fetchall()
        
        cursor.close()
        
        produtos_decodificados = []
        
        for produto in produtos:
            id_produto = produto[0]
            nome_produto = produto[1].decode('utf-8') if isinstance(produto[1], bytearray) else produto[1]
            descricao_produto = produto[2].decode('utf-8')
            valor_produto = produto[3]
            tipo_produto = produto[4].decode('utf-8') if isinstance(produto[4], bytearray) else produto[4]
            tipo_produtos = produto[5].decode('utf-8') if isinstance(produto[5], bytearray) else produto[5]
            imagem_produto = produto[6].decode('utf-8') if isinstance(produto[6], bytearray) else produto[6]
            qtd_comprada = produto[7]
            qtd_vendida = produto[8]
            variacao_produto = produto[9].decode('utf-8') if isinstance(produto[9], bytearray) else produto[9]  # Coluna que contém os IDs das variações
            
        variacoes = []
        if variacao_produto:
            ids_variacoes = variacao_produto.split(', ') if variacao_produto else []
            
            for id_variacao in ids_variacoes:
                query_variacao = """SELECT p.id, p.nome, p.qtd_comprada
                            FROM produtos p
                            LEFT JOIN vendas v ON p.id = v.id_produto
                            WHERE p.id = %s AND v.temporario = 0 AND v.obs = 'OK'
                            GROUP BY p.id, p.nome, p.qtd_comprada
                            HAVING p.qtd_comprada > COALESCE(SUM(v.qtd_produto), 0)"""
                cursor = db.cursor() 
                cursor.execute(query_variacao, (id_variacao,))
                variacao_resultado = cursor.fetchone()
                
                if variacao_resultado:
                    nome_variacao_completo = variacao_resultado[1].decode('utf-8') if isinstance(variacao_resultado[1], bytearray) else variacao_resultado[1]
                    id_variacao = variacao_resultado[0]
                    
                    if nome_produto in nome_variacao_completo:
                        nome_variacao = nome_variacao_completo.replace(nome_produto, "").strip(" -")
                    else:
                        nome_variacao = nome_variacao_completo
                    
                    variacoes.append((nome_variacao, id_variacao)) 
        
            cursor.close()
        
        produtos_decodificados.append((id_produto, nome_produto, descricao_produto, valor_produto, tipo_produto, tipo_produtos, imagem_produto, qtd_comprada, qtd_vendida, variacoes))
                
        db.close()
        
        return produtos_decodificados
    
    def get_products_cart(self, product_ids):
        db = conectar_db()
        cursor = db.cursor()

        placeholders = ', '.join(['%s'] * len(product_ids))

        query = f"""
            SELECT p.id, p.nome, p.descricao, p.valor, p.tipo_produto, tp.nome, p.imagem, p.qtd_comprada, COALESCE(SUM(v.qtd_produto), 0) AS qtd_vendida, p.peso, p.altura, p.largura, p.comprimento
            FROM produtos p 
            LEFT JOIN vendas v ON p.id = v.id_produto AND v.obs IS NOT NULL AND v.id_pagamento IS NOT NULL AND v.forma_pagamento IS NOT NULL
            INNER JOIN tipo_produtos tp ON p.tipo = tp.id 
            WHERE p.id IN ({placeholders})
            GROUP BY p.id;
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
            qtd_disponivel = Decimal(produto[7]) - Decimal(produto[8])
            peso = produto[9]
            altura = produto[10]
            largura = produto[11]
            comprimento = produto[12]

            produtos_decodificados.append((
                id_produto, nome_produto, descricao_produto, valor_produto, 
                tipo_produto, tipo_produtos, imagem_produto, qtd_disponivel,
                peso, altura, largura, comprimento
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
            VALUES (%s, %s, %s, CONVERT_TZ(NOW(), '+00:00', '-03:00'), %s, 1)
        """

        try:
            cursor.execute(query, (id_produto, idUser, qtd_produto, valor_total_produto))
            db.commit()

            id_gerado = cursor.lastrowid
            return id_gerado  
        except Exception as e:
            db.rollback()
            print(f"Erro ao salvar no banco: {e}")
            return False
        finally:
            cursor.close()
            db.close()
    
    def save_shipping_data(self, cep, rua, bairro, cidade, estado, numero, complemento, forma_envio, transportadora, valor_total_compra, valor_frete, id_tabela):
        db = conectar_db()
        cursor = db.cursor()
        query = """
            UPDATE vendas 
            SET cep = %s, rua = %s, bairro = %s, cidade = %s, estado = %s, numero = %s, complemento = %s, forma_envio = %s, transportadora = %s,
                valor_total_compra = %s, valor_frete = %s, dt_registro = CONVERT_TZ(NOW(), '+00:00', '-03:00')
            WHERE id = %s
        """
        try:
            for id in id_tabela:
                cursor.execute(query, (cep, rua, bairro, cidade, estado, numero, complemento, forma_envio, transportadora, valor_total_compra, valor_frete, id))
            
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
            SELECT p.nome, p.tipo_produto, v.qtd_produto, v.forma_envio, v.cep, v.rua, v.bairro, v.cidade, v.estado, v.numero, v.complemento, v.valor_total_produto, v.valor_frete, v.valor_total_compra, v.transportadora
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
                transportadora = produto[14]

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
                    'valor_total_compra': valor_total_compra,
                    'transportadora': transportadora
                }
                produtos_decodificados.append(produto_decodificado)

        cursor.close()
        db.close()

        return produtos_decodificados

    def set_payment_cart(self, id_tabela, forma_pgmt, id_pagamento):
        db = conectar_db()
        cursor = db.cursor()
    
        try:
            update_vendas_query = """
                UPDATE vendas
                SET forma_pagamento = %s, temporario = 0, dt_registro = CONVERT_TZ(NOW(), '+00:00', '-03:00'), id_pagamento = %s, obs = 'OK'
                WHERE id = %s;
            """
    
            get_usuario_query = """
                SELECT id_usuario
                FROM vendas
                WHERE id = %s;
            """
    
            update_usuario_query = """
                UPDATE usuarios
                SET first_buy = 0
                WHERE id = %s;
            """
    
            for id in id_tabela:
                cursor.execute(update_vendas_query, (forma_pgmt, id_pagamento, id))
    
                cursor.execute(get_usuario_query, (id,))
                resultado = cursor.fetchone()
    
                if resultado:
                    id_usuario = resultado[0]
    
                    cursor.execute(update_usuario_query, (id_usuario,))
    
            db.commit()
            Email_Routes.enviar_email_compra_cartao(id_tabela)
            return True
    
        except Exception as e:
            db.rollback()
            print(f"Erro ao salvar no banco: {e}")
            return False
    
        finally:
            cursor.close()
            db.close()
            
    def set_payment_pix(self, id_tabela, forma_pgmt, id_pagamento, valor_pago):
        db = conectar_db()
        cursor = db.cursor()
    
        try:
            update_vendas_query = """
                UPDATE vendas
                SET forma_pagamento = %s, temporario = 0, dt_registro = CONVERT_TZ(NOW(), '+00:00', '-03:00'), id_pagamento = %s, obs = 'pendente', valor_total_compra = %s
                WHERE id = %s;
            """
    
            get_usuario_query = """
                SELECT id_usuario
                FROM vendas
                WHERE id = %s;
            """
    
            update_usuario_query = """
                UPDATE usuarios
                SET first_buy = 0
                WHERE id = %s;
            """
    
            for id in id_tabela:
                cursor.execute(update_vendas_query, (forma_pgmt, id_pagamento, valor_pago, id))
    
                cursor.execute(get_usuario_query, (id,))
                resultado = cursor.fetchone()
    
                if resultado:
                    id_usuario = resultado[0]
    
                    cursor.execute(update_usuario_query, (id_usuario,))
    
            db.commit()
            Email_Routes.enviar_email_compra_pix(id_tabela)
            return True
    
        except Exception as e:
            db.rollback()
            print(f"Erro ao salvar no banco: {e}")
            return False
    
        finally:
            cursor.close()
            db.close()
    
    def get_id_payment_for_user(id_usuario):
        db = conectar_db()
        cursor = db.cursor()
        
        try:
            query = """
                SELECT v.id_pagamento, v.dt_registro, GROUP_CONCAT(p.nome SEPARATOR ', ') AS nomes_produtos, v.valor_total_compra, v.forma_pagamento, v.rua, v.numero, v.bairro, v.cidade, v.forma_envio, v.obs
                FROM vendas v
                JOIN produtos p ON v.id_produto = p.id
                WHERE v.id_usuario = %s AND temporario = 0
                GROUP BY v.id_pagamento, v.dt_registro, v.valor_total_compra, v.forma_pagamento, v.rua, v.numero, v.bairro, v.cidade
                ORDER BY v.dt_registro DESC
            """
            cursor.execute(query, (id_usuario,))
            
            resultados = cursor.fetchall()
            
            return resultados
        except Exception as e:
            print(f"Erro ao buscar IDs dos pagamentos: {e}")
            return []
        finally:
            cursor.close()
            db.close()
            
    def delete_from_vendas_temporario():
        db = conectar_db()
        cursor = db.cursor()
        
        try:
            query = """
                DELETE FROM vendas WHERE temporario = 1 AND id_pagamento IS NULL AND dt_registro <= DATE_SUB(CONVERT_TZ(NOW(), '+00:00', '-03:00'), INTERVAL 1 DAY) AND obs IS NULL;
            """
            cursor.execute(query)
            db.commit() 
            
            return cursor.rowcount
        except Exception as e:
            db.rollback() 
            print(f"Erro ao excluir vendas: {e}")
            return 0 
        finally:
            cursor.close()
            db.close()
            
    def avise_me_quando_chegar(self, email, id_produto):
        db = conectar_db()
        cursor = db.cursor()
    
        idUser = usersRoutes.getIdUserByEmail(email)
    
        if idUser is None:
            return False, None 
    
        query_tipo_produto = "SELECT tipo_produto FROM produtos WHERE id = %s"
        
        try:
            cursor.execute(query_tipo_produto, (id_produto,))
            tipo_produto = cursor.fetchone()
            
            if tipo_produto is None:
                return False, None 
            
            tipo_produto = tipo_produto[0]  
    

            query_insert = """
                INSERT INTO avise_quando_chegar (id_produto, id_usuario, dt_solicitacao)
                VALUES (%s, %s, CONVERT_TZ(NOW(), '+00:00', '-03:00'))
            """
            
            cursor.execute(query_insert, (id_produto, idUser))
            db.commit()
            
            return True, tipo_produto
            
        except Exception as e:
            db.rollback()
            print(f"Erro ao salvar no banco: {e}")
            return False, None  
            
        finally:
            cursor.close()
            db.close()

    def get_discount_client(self, email):
        db = conectar_db()
        cursor = db.cursor()
    
        query = """
            SELECT first_buy
            FROM usuarios 
            WHERE email = %s;
        """
        
        try:
            cursor.execute(query, (email,))
            resultado = cursor.fetchone()
            if resultado:
                return resultado[0]
            else:
                return None
        except mysql.connector.Error as err:
            print(f"Erro ao executar a query: {err}")
            return None
        finally:
            cursor.close()
            db.close()


@produtos.route("/cart", methods=['POST'])
@login_required
def cart():
    product_ids = json.loads(request.form['product_ids'])
    product_quantities = json.loads(request.form['product_quantities'])
    
    if not product_ids:
        return render_template('cart.html', product_cart=[])

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
    
    peso_total = 0
    largura_total = 0
    altura_total = 0
    comprimento_total = 0
    
    for key in request.form:
        if key.startswith("id_produto_"):
            produto_id = request.form[key]
            quantidade = request.form.get(f"quantidade_{produto_id}")
            valor_total = request.form.get(f"valor_total_{produto_id}")
            
            peso = float(request.form.get(f"peso_{produto_id}", 0))
            largura = float(request.form.get(f"largura_{produto_id}", 0)) 
            altura = float(request.form.get(f"altura_{produto_id}", 0)) 
            comprimento = float(request.form.get(f"comprimento_{produto_id}", 0)) 
            
            # Acumulando os totais
            peso_total += peso * int(quantidade)  
            largura_total += largura * int(quantidade) 
            altura_total += altura * int(quantidade) 
            comprimento_total += comprimento * int(quantidade) 
            
            session['peso_total'] = peso_total
            
            # Converter valor_total para o formato correto
            if valor_total:
                valor_total = float(valor_total.replace(',', '.')) 

            produtos.append({
                "id_produto": produto_id,
                "quantidade": quantidade,
                "valor_total": valor_total
            })

    produtoRoute = Produtos_Routes()
        
    session['peso_total'] = peso_total
    session['largura_total'] = largura_total
    session['altura_total'] = altura_total
    session['comprimento_total'] = comprimento_total
    
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
    transportadora_texto = request.form.get('forma_envio_text')
    transportadora = transportadora_texto.split(' - ')[0] + ' - ' + transportadora_texto.split(' - ')[1]
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

    if float(forma_envio.replace(',', '.')) > 0:
        forma_envio = "Envio"
    else:
        forma_envio = "Retirada"

    produtoRoute = Produtos_Routes()
    try:
        resultado = produtoRoute.save_shipping_data(cep, rua, bairro, cidade, estado, numero, complemento, forma_envio, transportadora, valor_total_compra, valor_frete, id_tabela)
        
        if resultado:
            session['id_tabela'] = id_tabela
            return redirect(define_rota('/payments#payments')) 
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
    email = session.get('user_email')
    
    if not id_tabela:
        flash("Erro: Nenhum ID de tabela encontrado na sessão.", "danger")
        return redirect(define_rota('/'))
    
    produtoRoute = Produtos_Routes()
    
    discount = produtoRoute.get_discount_client(email)

    try:
        produtos = produtoRoute.get_products_for_payments(id_tabela)
        
        if produtos:
            return render_template('payments.html', produtos=produtos, discount=discount)
        else:
            flash("Nenhum produto encontrado para o pagamento.", "danger")
            return redirect(define_rota('/'))

    except Exception as e:
        flash(f"Erro ao carregar os produtos: {str(e)}", "danger")
        return redirect(define_rota('/'))
        
@produtos.route('/avise/<int:id>')
@login_required
def avise_me(id):
    email = session.get('user_email')
    id_produto = id
    
    produtoRoute = Produtos_Routes()
    
    if not email:
        flash("Erro: Nenhum Email encontrado na sessão.", "danger")
        return redirect(define_rota('/'))
    
    sucesso, tipo_produto = produtoRoute.avise_me_quando_chegar(email, id_produto)
    
    if not sucesso:
        flash("Erro: Algo deu errado ao tentar registrar o aviso.", "danger")
        return redirect(define_rota('/'))
    
    flash("Você será avisado quando o produto estiver disponível.", "success")

    if tipo_produto == "Maquiagem":
        return redirect(define_rota('/maquiagem'))
    else:
        return redirect(define_rota('/skincare'))

