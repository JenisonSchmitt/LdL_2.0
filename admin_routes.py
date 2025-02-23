from flask import Blueprint, render_template, request, flash, redirect, jsonify
from login_required import login_required_admin
from conection import conectar_db, define_rota
from datetime import datetime, timedelta
import os
import random

admin_bp = Blueprint('admin', __name__)

class Admin_Routes:
     
    def obter_estatisticas():
        db = conectar_db()
        cursor = db.cursor()

        sete_dias_atras = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')

        query_total = """
        SELECT 
            Count(v.id) AS vendas_totais,
            SUM(v.valor_total_produto) AS faturamento_total
        FROM vendas v
        WHERE v.obs IS NOT NULL AND v.id_pagamento IS NOT NULL AND v.forma_pagamento IS NOT NULL;
        """
        
        query_ultimos_7_dias = f"""
        SELECT 
            Count(v.id) AS vendas_ultimos_7_dias,
            SUM(v.valor_total_produto) AS faturamento_ultimos_7_dias
        FROM vendas v
        WHERE v.dt_registro >= '{sete_dias_atras}' AND v.obs IS NOT NULL AND v.id_pagamento IS NOT NULL AND v.forma_pagamento IS NOT NULL;
        """

        cursor.execute(query_total)
        dados_totais = cursor.fetchone()

        cursor.execute(query_ultimos_7_dias)
        dados_ultimos_7_dias = cursor.fetchone()

        cursor.close()
        db.close()

        vendas_totais = dados_totais[0] if dados_totais[0] else 0
        faturamento_total = dados_totais[1] if dados_totais[1] else 0
        vendas_ultimos_7_dias = dados_ultimos_7_dias[0] if dados_ultimos_7_dias[0] else 0
        faturamento_ultimos_7_dias = dados_ultimos_7_dias[1] if dados_ultimos_7_dias[1] else 0

        return {
            'vendas_ultimos_7_dias': vendas_ultimos_7_dias,
            'faturamento_ultimos_7_dias': faturamento_ultimos_7_dias,
            'vendas_totais': vendas_totais,
            'faturamento_total': faturamento_total
        }
    
    def obter_tipo_produto():
        db = conectar_db()
        cursor = db.cursor()

        query_tipos = """
        SELECT id, nome FROM tipo_produtos;
        """
        cursor.execute(query_tipos)
        tipos = cursor.fetchall()

        query_categorias = """
        SELECT categoria FROM tipo_produtos GROUP BY categoria;
        """
        cursor.execute(query_categorias)
        categorias = cursor.fetchall()

        cursor.close()
        db.close()

        # Processar tipos de produtos
        tipos_produto = []
        for tipo in tipos:
            tipos_produto.append({
                "id_tipo_produto": tipo[0],
                "nome_tipo_produto": tipo[1].decode('utf-8') if isinstance(tipo[1], bytearray) else tipo[1]
            })

        # Processar categorias
        categorias_produto = []
        for categoria in categorias:
            categorias_produto.append({
                "categoria_tipo_produto": categoria[0].decode('utf-8') if isinstance(categoria[0], bytearray) else categoria[0]
            })

        return {
            "tipos_produto": tipos_produto,
            "categorias_produto": categorias_produto
        }
    
    @staticmethod
    def inserir_produto(nome, descricao, valor, tipo_produto, dt_cadastro, qtd_comprada, variacao, tipo, peso, altura, largura, comprimento, imagem):
        db = conectar_db()
        cursor = db.cursor()

        try:
            query = """
            INSERT INTO produtos (nome, descricao, valor, tipo_produto, dt_cadastro, qtd_comprada, variacao, tipo, peso, altura, largura, comprimento, imagem)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
            valores = (nome, descricao, valor, tipo_produto, dt_cadastro, qtd_comprada, variacao, tipo, peso, altura, largura, comprimento, imagem)
            cursor.execute(query, valores)
            db.commit()

            return True
        except Exception as e:
            print(f"Erro ao inserir produto: {e}")
            db.rollback()
            return False
        finally:
            cursor.close()
            db.close()

    @staticmethod
    def procurar_produtos(termo):
        db = conectar_db()
        cursor = db.cursor()

        consulta = "SELECT id, nome, valor FROM produtos WHERE LOWER(nome) COLLATE utf8_general_ci LIKE LOWER(%s)"
        cursor.execute(consulta, ('%' + termo + '%',))
        produtos = cursor.fetchall()

        db.close()
    
        return produtos
    
    @staticmethod
    def buscar_clientes(termo):
        db = conectar_db()
        cursor = db.cursor()

        consulta = """
            SELECT id, nome, cep, rua, cidade, estado, numero, complemento 
            FROM usuarios 
            WHERE LOWER(nome) COLLATE utf8_general_ci LIKE LOWER(%s)
        """
        cursor.execute(consulta, ('%' + termo + '%',))
        clientes = cursor.fetchall()

        db.close()

        return clientes
    
    @staticmethod
    def buscar_clientes_por_ID(id):
        db = conectar_db()
        cursor = db.cursor()

        consulta = """
            SELECT cep, rua, cidade, estado, numero, complemento 
            FROM usuarios 
            WHERE id = %s
        """
        cursor.execute(consulta, (id,)) 
        clientes = cursor.fetchall()

        db.close()

        if not clientes:
            return NotImplemented

        cliente = clientes[0]

        cep = cliente[0].decode('utf-8') if isinstance(cliente[0], bytearray) else cliente[0]
        rua = cliente[1].decode('utf-8') if isinstance(cliente[1], bytearray) else cliente[1]
        cidade = cliente[2].decode('utf-8') if isinstance(cliente[2], bytearray) else cliente[2]
        estado = cliente[3].decode('utf-8') if isinstance(cliente[3], bytearray) else cliente[3]
        numero = cliente[4]
        complemento = cliente[5].decode('utf-8') if isinstance(cliente[5], bytearray) else cliente[5]

        infos_clientes = [cep, rua, cidade, estado, numero, complemento]

        return infos_clientes
    
    @staticmethod
    def inserir_venda_admin(id_produto, id_usuario, qtd_produto, dt_registro, forma_envio, transportadora, cep, rua, bairro, cidade, estado, numero, complemento,
                            valor_total_produto, valor_frete, valor_total_compra, forma_pagamento, temporario, obs, id_pagamento):
        db = conectar_db()
        cursor = db.cursor()

        try:
            query = """
                INSERT INTO vendas (
                    id_produto, id_usuario, qtd_produto, dt_registro, forma_envio, transportadora, cep, rua, bairro, cidade, estado, numero, complemento,
                    valor_total_produto, valor_frete, valor_total_compra, forma_pagamento, temporario, obs, id_pagamento
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                id_produto, id_usuario, qtd_produto, dt_registro, forma_envio, transportadora, cep, rua, bairro, cidade, estado, numero, complemento,
                valor_total_produto, valor_frete, valor_total_compra, forma_pagamento, temporario, obs, id_pagamento
            )

            cursor.execute(query, valores)
            db.commit()
            return True
        except Exception as e:
            print(f"Erro ao inserir produto: {e}")
            db.rollback()
            return False
        finally:
            cursor.close()
            db.close()

    @staticmethod
    def select_valor_admin(produto_id):
        db = conectar_db()
        cursor = db.cursor()

        query = "SELECT valor FROM produtos WHERE id = %s"
        cursor.execute(query, (produto_id,))  # Passando produto_id como uma tupla
        valor_produto = cursor.fetchone()[0]  # Obtendo o valor do produto

        cursor.close()
        db.close()

        return valor_produto

@admin_bp.route("/admin")
#@login_required_admin
def admin_home():
    dados_estatisticas = Admin_Routes.obter_estatisticas()

    return render_template('admin/templates/dashboard.html', 
                           vendas_ultimos_7_dias=dados_estatisticas['vendas_ultimos_7_dias'],
                           faturamento_ultimos_7_dias=dados_estatisticas['faturamento_ultimos_7_dias'],
                           vendas_totais=dados_estatisticas['vendas_totais'],
                           faturamento_total=dados_estatisticas['faturamento_total'])

@admin_bp.route("/redirect-admin/<string:diretorio>")
#@login_required_admin
def redirect_route_admin(diretorio):
    return render_template(f"admin/templates/{diretorio}.html")

@admin_bp.route("/cadastrar-produto-admin")
#@login_required_admin
def cadastrar_produto_admin():
    dados = Admin_Routes.obter_tipo_produto()
    return render_template('admin/templates/cadastrar-produto.html', 
                           tipos_produto=dados['tipos_produto'],
                           categorias_produto=dados['categorias_produto'])

@admin_bp.route("/cadastrar-produto-insert", methods=['POST'])
#@login_required_admin
def cadastrar_produto_insert():
    try:
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        valor = float(request.form.get('valor').replace(',', '.'))
        tipo_produto = request.form.get('tipo_produto')
        dt_cadastro = datetime.now()
        qtd_comprada = int(request.form.get('qtd_comprada'))
        variacao = int(request.form.get('variacoes')) if request.form.get('variacoes') else 0
        tipo = request.form.get('Tipo')
        peso = float(request.form.get('peso'))
        altura = float(request.form.get('altura'))
        largura = float(request.form.get('largura'))
        comprimento = float(request.form.get('comprimento'))
        
        imagem = request.files['imagem']
        imagem_filename = None
        if imagem and imagem.filename:
            upload_dir = "/public_html/static/images/"
            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)

            imagem_filename = os.path.join(upload_dir, imagem.filename)
            imagem.save(imagem_filename)

        print("enviando dados: " + nome, descricao, valor, tipo_produto, dt_cadastro, qtd_comprada, variacao, tipo, peso, altura, largura, comprimento, imagem_filename )
        sucesso = Admin_Routes.inserir_produto(nome, descricao, valor, tipo_produto, dt_cadastro, qtd_comprada, variacao, tipo, peso, altura, largura, comprimento, imagem_filename)

        if sucesso:
            flash("Produto cadastrado com sucesso!", "success")
        else:
            flash("Erro ao cadastrar produto. Tente novamente.", "danger")
    
    except Exception as e:
        print(f"Erro ao processar cadastro: {e}")
        flash("Erro interno ao cadastrar produto.", "danger")

    return redirect(define_rota('/admin'))

@admin_bp.route('/buscar-produtos-admin', methods=['POST'])
#@login_required_admin
def buscar_produtos():
    termo = request.form.get('q', '').strip() 

    if len(termo) < 3:
        return jsonify([])

    produtos = Admin_Routes.procurar_produtos(termo)

    produtos_formatados = [
        {"id": p[0], 
         "nome": p[1].decode("utf-8"),
         "valor": p[2],
        } 
    for p in produtos]

    return jsonify(produtos_formatados)

@admin_bp.route('/buscar-clientes-admin', methods=['POST'])
#@login_required_admin
def buscar_clientes():
    termo = request.form.get('q', '').strip() 

    if len(termo) < 3:
        return jsonify([])

    clientes = Admin_Routes.buscar_clientes(termo)

    clientes_formatados = [{
        "id": p[0], 
        "nome": p[1].decode("utf-8") if p[1] else "",
        "cep": p[2].decode("utf-8") if p[2] else "",
        "rua": p[3].decode("utf-8") if p[3] else "",
        "cidade": p[4].decode("utf-8") if p[4] else "",
        "estado": p[5].decode("utf-8") if p[5] else "",
        "numero": p[6] if p[6] else 0,
        "complemento": p[7].decode("utf-8") if p[7] else ""
    } for p in clientes]


    return jsonify(clientes_formatados)

@admin_bp.route('/cadastrar-venda-insert', methods=['POST'])
def cadastrar_venda_admin():
    try:
        id_usuario = request.form.get('cliente_id')
        infos_cliente = Admin_Routes.buscar_clientes_por_ID(id_usuario)
        cep = infos_cliente[0]
        rua = infos_cliente[1]
        cidade = infos_cliente[2]
        estado = infos_cliente[3]
        numero = infos_cliente[4]
        complemento = infos_cliente[5]
        bairro = "Bairro" 
        produtos_ids = request.form.getlist('produto_id[]')
        produtos_quantidades = request.form.getlist('qtdproduto[]')
        produtos_valores = request.form.getlist('produto_valor[]')
        dt_registro = datetime.now()
        forma_envio = request.form.get('envio') 
        valor_frete = request.form.get('valorfrete')
        forma_pagamento = request.form.get('forma_pgt')
        temporario = 0
        obs = "OK"
        valor_total_compra = float(request.form.get('valor_total', 0))
        numero_aleatorio = random.randint(1000000, 9999999)
        id_pagamento = "LDL" + str(numero_aleatorio)
        
        if forma_envio == 'Envio':
            transportadora = "Transportadora - Melhor Envio"
        else:
            valor_frete = 0
            transportadora = "Combinar retirada R$0,00 (Tubarão/SC - Centro)"
        for id_produto, qtd_produto, valor in zip(produtos_ids, produtos_quantidades, produtos_valores):
            valor_total_produto = float(qtd_produto) * float(valor)
            insert_vendas = Admin_Routes.inserir_venda_admin(
                id_produto, id_usuario, qtd_produto, dt_registro, forma_envio, transportadora, cep, rua, bairro, cidade, estado, numero, complemento,
                valor_total_produto, valor_frete, valor_total_compra, forma_pagamento, temporario, obs, id_pagamento
            )

            if not insert_vendas:
                flash("Erro ao processar Venda!", "danger")
                return redirect(define_rota('/admin'))

        flash("Venda cadastrada com sucesso!", "success")
        return redirect(define_rota('/admin'))

    except Exception as e:
        print(f"Erro ao cadastrar venda: {e}")
        flash("Erro interno ao cadastrar venda.", "danger")
        return redirect(define_rota('/admin'))