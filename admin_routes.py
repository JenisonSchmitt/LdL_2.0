from flask import Blueprint, render_template, request, flash, redirect, jsonify
from login_required import login_required_admin
from conection import conectar_db, define_rota
from datetime import datetime, timedelta
from emails_routes import Email_Routes
import os
import unicodedata
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
        WHERE v.obs = "OK" AND v.id_pagamento IS NOT NULL AND v.forma_pagamento IS NOT NULL;
        """
        
        query_ultimos_7_dias = f"""
        SELECT 
            Count(v.id) AS vendas_ultimos_7_dias,
            SUM(v.valor_total_produto) AS faturamento_ultimos_7_dias
        FROM vendas v
        WHERE v.dt_registro >= '{sete_dias_atras}' AND v.obs = "OK" AND v.id_pagamento IS NOT NULL AND v.forma_pagamento IS NOT NULL;
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
            VALUES (%s, %s, %s, %s, CONVERT_TZ(NOW(), '+00:00', '-03:00'), %s, %s, %s, %s, %s, %s, %s, %s);
            """
            valores = (nome, descricao, valor, tipo_produto, qtd_comprada, variacao, tipo, peso, altura, largura, comprimento, imagem)
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
    def procurar_produtos_update(termo):
        db = conectar_db()
        cursor = db.cursor()
    
        consulta = "SELECT id, nome, valor, qtd_comprada FROM produtos WHERE LOWER(nome) COLLATE utf8_general_ci LIKE LOWER(%s)"
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
    def inserir_venda_admin(id_produto, id_usuario, qtd_produto, dt_registro, forma_envio, transportadora, cep, rua, bairro, cidade, estado, numero, complemento, valor_total_produto, valor_frete, valor_total_compra, forma_pagamento, temporario, obs, id_pagamento):
        db = conectar_db()
        cursor = db.cursor()

        try:
            query = """
                INSERT INTO vendas (
                    id_produto, id_usuario, qtd_produto, dt_registro, forma_envio, transportadora, cep, rua, bairro, cidade, estado, numero, complemento,
                    valor_total_produto, valor_frete, valor_total_compra, forma_pagamento, temporario, obs, id_pagamento
                ) VALUES (%s, %s, %s, CONVERT_TZ(NOW(), '+00:00', '-03:00'), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                id_produto, id_usuario, qtd_produto, forma_envio, transportadora, cep, rua, bairro, cidade, estado, numero, complemento,
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
        cursor.execute(query, (produto_id,))  
        valor_produto = cursor.fetchone()[0]

        cursor.close()
        db.close()

        return valor_produto

    @staticmethod
    def obter_todos_os_produtos():
        db = conectar_db()
        cursor = db.cursor()
        
        query = """
            SELECT 
                p.*, 
                COALESCE(SUM(v.qtd_produto), 0) AS qtd_vendida,
                (p.qtd_comprada - COALESCE(SUM(v.qtd_produto), 0)) AS quantidade_restante
            FROM 
                produtos p 
            LEFT JOIN 
                vendas v ON p.id = v.id_produto 
            WHERE v.obs IS NOT NULL AND v.id_pagamento IS NOT NULL AND v.forma_pagamento IS NOT NULL
            GROUP BY 
                p.id 
            ORDER BY 
                quantidade_restante ASC;
        """
    
        try:
            cursor.execute(query) 
            produtos = cursor.fetchall() 
        except mysql.connector.Error as err:
            print(f"Erro ao executar a query: {err}")
            return []
        finally:
            cursor.close()
            db.close()
    
        produtos_decodificados = []
        for produto in produtos:
            id_produto = produto[0]
            nome_produto = produto[1].decode('utf-8') if isinstance(produto[1], bytearray) else produto[1]
            descricao_produto = produto[2].decode('utf-8') if isinstance(produto[2], bytearray) else produto[2]
            valor = produto[3].decode('utf-8') if isinstance(produto[3], bytearray) else produto[3]
            tipo_produto = produto[4].decode('utf-8') if isinstance(produto[4], bytearray) else produto[4]
            dt_cadastro = produto[5]
            qtd_comprada = produto[6]
            variacao = produto[7].decode('utf-8') if isinstance(produto[7], bytearray) else produto[7]
            tipo = produto[8].decode('utf-8') if isinstance(produto[8], bytearray) else produto[8]
            imagem = produto[9].decode('utf-8') if isinstance(produto[9], bytearray) else produto[9]
            peso = produto[10]
            altura = produto[11]
            largura = produto[12]
            comprimento = produto[13]
            qtd_vendida = produto[14]
            quantidade_restante = produto[15] 
    
            produtos_decodificados.append((
                id_produto, nome_produto, descricao_produto, valor, tipo_produto, dt_cadastro, 
                qtd_comprada, variacao, tipo, imagem, peso, altura, largura, comprimento, 
                qtd_vendida, quantidade_restante 
            ))
        
        return produtos_decodificados

    @staticmethod
    def insert_update_produto(produtos_id, qtd_final, dt_registro):
        db = conectar_db()
        cursor = db.cursor()
    
        try:
            query = """
                UPDATE produtos SET qtd_comprada = %s, dt_cadastro = %s WHERE id = %s
            """
    
            cursor.execute(query, (qtd_final, dt_registro, produtos_id))
            db.commit()
            return True
        except Exception as e:
            print(f"Erro ao atualizar produto: {e}")
            db.rollback()
            return False
        finally:
            cursor.close()
            db.close()

    @staticmethod
    def obter_todas_as_vendas():
        db = conectar_db()
        cursor = db.cursor()
        
        query = """
            SELECT
                v.id AS id_venda, v.id_produto, p.nome AS nome_produto, v.id_usuario, u.nome AS nome_usuario, v.qtd_produto, v.dt_registro, v.forma_envio,
                v.transportadora, v.cep, v.rua, v.bairro, v.cidade, v.estado, v.numero, v.complemento, v.valor_frete, v.valor_total_compra, v.id_pagamento, v.forma_pagamento,
                v.temporario, v.obs, v.qtd_produto
            FROM
                vendas v
            JOIN
                produtos p ON v.id_produto = p.id
            JOIN
                usuarios u ON v.id_usuario = u.id
            WHERE
                v.obs = "OK"
                AND v.id_pagamento IS NOT NULL
                AND v.forma_pagamento IS NOT NULL
            ORDER BY
                v.dt_registro DESC;
        """
        
        try:
            cursor.execute(query) 
            vendas = cursor.fetchall() 
        except mysql.connector.Error as err:
            print(f"Erro ao executar a query: {err}")
            return []
        finally:
            cursor.close()
            db.close()
    
        vendas_decodificados = []
        for venda in vendas:
            id_venda = venda[0]
            id_produto = venda[1]
            nome_produto = venda[2].decode('utf-8') if isinstance(venda[2], bytearray) else venda[2]
            id_usuario = venda[3]
            nome_usuario = venda[4].decode('utf-8') if isinstance(venda[4], bytearray) else venda[4]
            qtd_produto = venda[5]
            dt_registro = venda[6]
            forma_envio = venda[7].decode('utf-8') if isinstance(venda[7], bytearray) else venda[7]
            transportadora = venda[8].decode('utf-8') if isinstance(venda[8], bytearray) else venda[8]
            cep = venda[9].decode('utf-8') if isinstance(venda[9], bytearray) else venda[9]
            rua = venda[10].decode('utf-8') if isinstance(venda[10], bytearray) else venda[10]
            bairro = venda[11].decode('utf-8') if isinstance(venda[11], bytearray) else venda[11]
            cidade = venda[12].decode('utf-8') if isinstance(venda[12], bytearray) else venda[12]
            estado = venda[13].decode('utf-8') if isinstance(venda[13], bytearray) else venda[13]
            numero = venda[14].decode('utf-8') if isinstance(venda[14], bytearray) else venda[14]
            complemento = venda[15].decode('utf-8') if isinstance(venda[15], bytearray) else venda[15]
            valor_frete = venda[16]
            valor_total_compra = venda[17]
            id_pagamento = venda[18].decode('utf-8') if isinstance(venda[15], bytearray) else venda[15]
            forma_pagamento = venda[19].decode('utf-8') if isinstance(venda[19], bytearray) else venda[19]
            temporario = venda[20]
            obs = venda[21].decode('utf-8') if isinstance(venda[21], bytearray) else venda[21]
    
            vendas_decodificados.append((id_venda, id_produto, nome_produto, id_usuario, nome_usuario, qtd_produto, dt_registro, forma_envio, transportadora, cep, rua,
                bairro, cidade, estado, numero, complemento, valor_frete, valor_total_compra, id_pagamento, forma_pagamento, temporario, obs))
        
        return vendas_decodificados
        
    @staticmethod
    def obter_todas_as_vendas_cliente(cliente_id):
        db = conectar_db()
        cursor = db.cursor()
        
        query = """
            SELECT
                v.id AS id_venda, v.id_produto, p.nome AS nome_produto, v.id_usuario, u.nome AS nome_usuario, v.qtd_produto, v.dt_registro, v.forma_envio,
                v.transportadora, v.cep, v.rua, v.bairro, v.cidade, v.estado, v.numero, v.complemento, v.valor_frete, v.valor_total_compra, v.id_pagamento, v.forma_pagamento,
                v.temporario, v.obs, v.qtd_produto
            FROM
                vendas v
            JOIN
                produtos p ON v.id_produto = p.id
            JOIN
                usuarios u ON v.id_usuario = u.id
            WHERE
                v.obs = "OK"
                AND v.id_pagamento IS NOT NULL
                AND v.forma_pagamento IS NOT NULL
                AND id_usuario = %s
            ORDER BY
                v.dt_registro DESC;
        """
        
        try:
            cursor.execute(query, (cliente_id,)) 
            vendas = cursor.fetchall() 
        except mysql.connector.Error as err:
            print(f"Erro ao executar a query: {err}")
            return []
        finally:
            cursor.close()
            db.close()
    
        vendas_decodificados = []
        for venda in vendas:
            id_venda = venda[0]
            id_produto = venda[1]
            nome_produto = venda[2].decode('utf-8') if isinstance(venda[2], bytearray) else venda[2]
            id_usuario = venda[3]
            nome_usuario = venda[4].decode('utf-8') if isinstance(venda[4], bytearray) else venda[4]
            qtd_produto = venda[5]
            dt_registro = venda[6]
            forma_envio = venda[7].decode('utf-8') if isinstance(venda[7], bytearray) else venda[7]
            transportadora = venda[8].decode('utf-8') if isinstance(venda[8], bytearray) else venda[8]
            cep = venda[9].decode('utf-8') if isinstance(venda[9], bytearray) else venda[9]
            rua = venda[10].decode('utf-8') if isinstance(venda[10], bytearray) else venda[10]
            bairro = venda[11].decode('utf-8') if isinstance(venda[11], bytearray) else venda[11]
            cidade = venda[12].decode('utf-8') if isinstance(venda[12], bytearray) else venda[12]
            estado = venda[13].decode('utf-8') if isinstance(venda[13], bytearray) else venda[13]
            numero = venda[14].decode('utf-8') if isinstance(venda[14], bytearray) else venda[14]
            complemento = venda[15].decode('utf-8') if isinstance(venda[15], bytearray) else venda[15]
            valor_frete = venda[16]
            valor_total_compra = venda[17]
            id_pagamento = venda[18].decode('utf-8') if isinstance(venda[18], bytearray) else venda[18]
            forma_pagamento = venda[19].decode('utf-8') if isinstance(venda[19], bytearray) else venda[19]
            temporario = venda[20]
            obs = venda[21].decode('utf-8') if isinstance(venda[21], bytearray) else venda[21]
    
            vendas_decodificados.append((id_venda, id_produto, nome_produto, id_usuario, nome_usuario, qtd_produto, dt_registro, forma_envio, transportadora, cep, rua,
                bairro, cidade, estado, numero, complemento, valor_frete, valor_total_compra, id_pagamento, forma_pagamento, temporario, obs))
        
        return vendas_decodificados

    @staticmethod
    def insert_user_admin(CPF, nome, telefone, email, nascimento, rua, numero, complemento, cep, cidade, estado, senha):
        db = conectar_db()  
        cursor = db.cursor()
        try:
            query = '''
                INSERT INTO usuarios (CPF, nome, telefone, email, nascimento, rua, numero, complemento, cep, cidade, estado, senha)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''
            parameters = (CPF, nome, telefone, email, nascimento, rua, numero, complemento, cep, cidade, estado, senha)


            cursor.execute(query, parameters) 
            db.commit()

            Email_Routes.enviar_email_conta_nova()
            return True
        except Exception as e:
            flash(f'Erro ao cadastrar usuário: {str(e)}', 'danger')
            return False
        finally:
            db.close()

    @staticmethod
    def obter_todos_cientes_admin():
        db = conectar_db()
        cursor = db.cursor()
        
        query = """
            SELECT * from usuarios ORDER BY nome ASC;
        """
        
        try:
            cursor.execute(query) 
            clientes = cursor.fetchall() 
        except mysql.connector.Error as err:
            print(f"Erro ao executar a query: {err}")
            return []
        finally:
            cursor.close()
            db.close()
    
        clientes_decodificados = []
        for cliente in clientes:
            id_cliente = cliente[0]
            cpf = cliente[1].decode('utf-8') if isinstance(cliente[1], bytearray) else cliente[1]
            nome_cliente = cliente[2].decode('utf-8') if isinstance(cliente[2], bytearray) else cliente[2]
            telefone = cliente[3].decode('utf-8') if isinstance(cliente[3], bytearray) else cliente[3]
            email = cliente[4].decode('utf-8') if isinstance(cliente[4], bytearray) else cliente[4]
            nascimento = cliente[5].decode('utf-8') if isinstance(cliente[5], bytearray) else cliente[5]
            rua = cliente[6].decode('utf-8') if isinstance(cliente[6], bytearray) else cliente[6]
            numero = cliente[7]
            complemento = cliente[8].decode('utf-8') if isinstance(cliente[8], bytearray) else cliente[8]
            cep = cliente[9].decode('utf-8') if isinstance(cliente[9], bytearray) else cliente[9]
            cidade = cliente[10].decode('utf-8') if isinstance(cliente[10], bytearray) else cliente[10]
            estado = cliente[11].decode('utf-8') if isinstance(cliente[11], bytearray) else cliente[11]
            dt_cadastro = cliente[15].decode('utf-8') if isinstance(cliente[15], bytearray) else cliente[15]

            clientes_decodificados.append((id_cliente, cpf, nome_cliente, telefone, email, nascimento, rua, numero, complemento, cep, cidade, estado, dt_cadastro ))
        
        return clientes_decodificados
        
    @staticmethod
    def obter_todos_aniversariantes_admin():
        db = conectar_db()
        cursor = db.cursor()
        
        query = """
            SELECT *
            FROM usuarios
            WHERE 
                DATE(CONCAT(YEAR(CURDATE()), '-', MONTH(nascimento), '-', DAY(nascimento))) 
                BETWEEN CURDATE() AND DATE_ADD(CURDATE(), INTERVAL 7 DAY)
            ORDER BY 
                DAY(nascimento) ASC, MONTH(nascimento) ASC;
        """
        
        try:
            cursor.execute(query) 
            clientes = cursor.fetchall() 
        except mysql.connector.Error as err:
            print(f"Erro ao executar a query: {err}")
            return []
        finally:
            cursor.close()
            db.close()
    
        clientes_decodificados = []
        for cliente in clientes:
            id_cliente = cliente[0]
            cpf = cliente[1].decode('utf-8') if isinstance(cliente[1], bytearray) else cliente[1]
            nome_cliente = cliente[2].decode('utf-8') if isinstance(cliente[2], bytearray) else cliente[2]
            telefone = cliente[3].decode('utf-8') if isinstance(cliente[3], bytearray) else cliente[3]
            email = cliente[4].decode('utf-8') if isinstance(cliente[4], bytearray) else cliente[4]
            nascimento = cliente[5].decode('utf-8') if isinstance(cliente[5], bytearray) else cliente[5]
            rua = cliente[6].decode('utf-8') if isinstance(cliente[6], bytearray) else cliente[6]
            numero = cliente[7]
            complemento = cliente[8].decode('utf-8') if isinstance(cliente[8], bytearray) else cliente[8]
            cep = cliente[9].decode('utf-8') if isinstance(cliente[9], bytearray) else cliente[9]
            cidade = cliente[10].decode('utf-8') if isinstance(cliente[10], bytearray) else cliente[10]
            estado = cliente[11].decode('utf-8') if isinstance(cliente[11], bytearray) else cliente[11]
            dt_cadastro = cliente[15].decode('utf-8') if isinstance(cliente[15], bytearray) else cliente[15]
    
            clientes_decodificados.append((
                id_cliente, cpf, nome_cliente, telefone, email, nascimento, rua, numero, complemento, cep, cidade, estado, dt_cadastro
            ))
        
        return clientes_decodificados
        
    @staticmethod
    def avisar_quando_chegar():
        db = conectar_db()
        cursor = db.cursor()
        
        query = """
            SELECT 
                a.id AS id, a.id_produto, p.nome AS nome_produto, a.id_usuario, u.nome AS nome_usuario, a.dt_solicitacao
            FROM 
                avise_quando_chegar a
            JOIN 
                produtos p ON a.id_produto = p.id
            JOIN 
                usuarios u ON a.id_usuario = u.id
            ORDER BY 
                a.dt_solicitacao;
        """
        
        try:
            cursor.execute(query) 
            avisar = cursor.fetchall() 
        except mysql.connector.Error as err:
            print(f"Erro ao executar a query: {err}")
            return []
        finally:
            cursor.close()
            db.close()
    
        avisar_decodificados = []
        for aviso in avisar:
            id = aviso[0]
            nome_produto = aviso[2].decode('utf-8') if isinstance(aviso[2], bytearray) else aviso[2]
            nome_usuario = aviso[4].decode('utf-8') if isinstance(aviso[4], bytearray) else aviso[4]
            dt_solicitacao = aviso[5]
    
            avisar_decodificados.append((
                id, nome_produto, nome_usuario, dt_solicitacao
            ))
        
        return avisar_decodificados
    
    @staticmethod
    def obter_todos_pagamentos_pendentes():
        db = conectar_db()
        cursor = db.cursor()
        
        query = """
            SELECT
                v.id AS id_venda, v.id_produto, p.nome AS nome_produto, v.id_usuario, u.nome AS nome_usuario, v.qtd_produto, v.dt_registro, v.forma_envio,
                v.transportadora, v.cep, v.rua, v.bairro, v.cidade, v.estado, v.numero, v.complemento, v.valor_frete, v.valor_total_compra, v.id_pagamento, v.forma_pagamento,
                v.temporario, v.obs
            FROM
                vendas v
            JOIN
                produtos p ON v.id_produto = p.id
            JOIN
                usuarios u ON v.id_usuario = u.id
            WHERE
                v.obs = 'pendente'
                AND v.id_pagamento IS NOT NULL
                AND v.forma_pagamento = 'bank_transfer'
            GROUP BY
                v.id_pagamento
            ORDER BY
                v.dt_registro DESC;
        """
        
        try:
            cursor.execute(query)
            vendas = cursor.fetchall() 
        except mysql.connector.Error as err:
            print(f"Erro ao executar a query: {err}")
            return []
        finally:
            cursor.close()
            db.close()
    
        vendas_decodificados = []
        for venda in vendas:
            id_venda = venda[0]
            id_produto = venda[1]
            nome_produto = venda[2].decode('utf-8') if isinstance(venda[2], bytearray) else venda[2]
            id_usuario = venda[3]
            nome_usuario = venda[4].decode('utf-8') if isinstance(venda[4], bytearray) else venda[4]
            qtd_produto = venda[5]
            dt_registro = venda[6]
            forma_envio = venda[7].decode('utf-8') if isinstance(venda[7], bytearray) else venda[7]
            transportadora = venda[8].decode('utf-8') if isinstance(venda[8], bytearray) else venda[8]
            cep = venda[9].decode('utf-8') if isinstance(venda[9], bytearray) else venda[9]
            rua = venda[10].decode('utf-8') if isinstance(venda[10], bytearray) else venda[10]
            bairro = venda[11].decode('utf-8') if isinstance(venda[11], bytearray) else venda[11]
            cidade = venda[12].decode('utf-8') if isinstance(venda[12], bytearray) else venda[12]
            estado = venda[13].decode('utf-8') if isinstance(venda[13], bytearray) else venda[13]
            numero = venda[14].decode('utf-8') if isinstance(venda[14], bytearray) else venda[14]
            complemento = venda[15].decode('utf-8') if isinstance(venda[15], bytearray) else venda[15]
            valor_frete = venda[16]
            valor_total_compra = venda[17]
            id_pagamento = venda[18].decode('utf-8') if isinstance(venda[18], bytearray) else venda[18]
            forma_pagamento = venda[19].decode('utf-8') if isinstance(venda[19], bytearray) else venda[19]
            temporario = venda[20]
            obs = venda[21].decode('utf-8') if isinstance(venda[21], bytearray) else venda[21]
    
            vendas_decodificados.append((
                id_venda, id_produto, nome_produto, id_usuario, nome_usuario, qtd_produto, dt_registro, forma_envio, transportadora, cep, rua,
                bairro, cidade, estado, numero, complemento, valor_frete, valor_total_compra, id_pagamento, forma_pagamento, temporario, obs
            ))
        
        return vendas_decodificados
    
    @staticmethod
    def aprovar_pagamento_pix_admin(id_pagamento):
        db = conectar_db()
        cursor = db.cursor()
    
        query = """
            UPDATE vendas
            SET obs = 'OK'
            WHERE id_pagamento = %s;
        """
        
        try:
            cursor.execute(query, (id_pagamento,))
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            print(f"Erro ao aprovar pagamento: {e}")
            return False
        finally:
            cursor.close()
            db.close()

    @staticmethod
    def obter_todos_id_pagamentos_cliente(cliente_id):
        db = conectar_db()
        cursor = db.cursor()
                
        query = """
            SELECT
                v.id_pagamento, v.dt_registro, v.forma_envio, v.transportadora, v.valor_frete, v.valor_total_compra, v.forma_pagamento, v.temporario, v.obs, u.nome AS nome_usuario
            FROM
                vendas v
            JOIN
                usuarios u ON v.id_usuario = u.id
            WHERE
                v.obs = "OK"
                AND v.id_pagamento IS NOT NULL
                AND v.forma_pagamento IS NOT NULL
                AND v.id_usuario = %s
            GROUP BY
                v.id_pagamento, v.dt_registro, v.forma_envio, v.transportadora, v.valor_frete, v.valor_total_compra, v.forma_pagamento, v.temporario, v.obs, u.nome
            ORDER BY
                v.dt_registro DESC;
        """

        try:
            cursor.execute(query, (cliente_id,)) 
            vendas = cursor.fetchall() 
        except mysql.connector.Error as err:
            print(f"Erro ao executar a query: {err}")
            return []
        finally:
            cursor.close()
            db.close()
    
        vendas_decodificados = []
        for venda in vendas:
            id_pagamento = venda[0].decode('utf-8') if isinstance(venda[0], bytearray) else venda[0]
            dt_registro = venda[1]
            forma_envio = venda[2].decode('utf-8') if isinstance(venda[2], bytearray) else venda[2]
            transportadora = venda[3].decode('utf-8') if isinstance(venda[3], bytearray) else venda[3]
            valor_frete = venda[4]
            valor_total_compra = venda[5]
            forma_pagamento = venda[6].decode('utf-8') if isinstance(venda[6], bytearray) else venda[6]
            temporario = venda[7]
            obs = venda[8].decode('utf-8') if isinstance(venda[8], bytearray) else venda[8]
            cliente = venda[9].decode('utf-8') if isinstance(venda[9], bytearray) else venda[9]
    
            vendas_decodificados.append((id_pagamento, dt_registro, valor_total_compra, forma_envio, transportadora, valor_frete, forma_pagamento, temporario, obs, cliente))
        
        return vendas_decodificados
    
    @staticmethod
    def obter_todas_as_infos_os(id_pagamento):
        db = conectar_db()
        cursor = db.cursor()
        
        query = """
            SELECT
                v.id AS id_venda, v.id_produto, p.nome AS nome_produto, v.id_usuario, u.nome AS nome_usuario, v.qtd_produto, v.dt_registro, v.forma_envio,
                v.transportadora, v.cep, v.rua, v.bairro, v.cidade, v.estado, v.numero, v.complemento, v.valor_frete, v.valor_total_compra, v.id_pagamento, v.forma_pagamento,
                v.temporario, v.obs, v.qtd_produto
            FROM
                vendas v
            JOIN
                produtos p ON v.id_produto = p.id
            JOIN
                usuarios u ON v.id_usuario = u.id
            WHERE
                v.obs = "OK"
                AND v.id_pagamento IS NOT NULL
                AND v.forma_pagamento IS NOT NULL
                AND id_pagamento = %s
            ORDER BY
                v.dt_registro DESC;
        """
        
        try:
            cursor.execute(query, (id_pagamento,)) 
            vendas = cursor.fetchall() 
        except mysql.connector.Error as err:
            print(f"Erro ao executar a query: {err}")
            return []
        finally:
            cursor.close()
            db.close()
    
        vendas_decodificados = []
        for venda in vendas:
            id_venda = venda[0]
            id_produto = venda[1]
            nome_produto = venda[2].decode('utf-8') if isinstance(venda[2], bytearray) else venda[2]
            id_usuario = venda[3]
            nome_usuario = venda[4].decode('utf-8') if isinstance(venda[4], bytearray) else venda[4]
            qtd_produto = venda[5]
            dt_registro = venda[6]
            forma_envio = venda[7].decode('utf-8') if isinstance(venda[7], bytearray) else venda[7]
            transportadora = venda[8].decode('utf-8') if isinstance(venda[8], bytearray) else venda[8]
            cep = venda[9].decode('utf-8') if isinstance(venda[9], bytearray) else venda[9]
            rua = venda[10].decode('utf-8') if isinstance(venda[10], bytearray) else venda[10]
            bairro = venda[11].decode('utf-8') if isinstance(venda[11], bytearray) else venda[11]
            cidade = venda[12].decode('utf-8') if isinstance(venda[12], bytearray) else venda[12]
            estado = venda[13].decode('utf-8') if isinstance(venda[13], bytearray) else venda[13]
            numero = venda[14].decode('utf-8') if isinstance(venda[14], bytearray) else venda[14]
            complemento = venda[15].decode('utf-8') if isinstance(venda[15], bytearray) else venda[15]
            valor_frete = venda[16]
            valor_total_compra = venda[17]
            id_pagamento = venda[18].decode('utf-8') if isinstance(venda[18], bytearray) else venda[18]
            forma_pagamento = venda[19].decode('utf-8') if isinstance(venda[19], bytearray) else venda[19]
            temporario = venda[20]
            obs = venda[21].decode('utf-8') if isinstance(venda[21], bytearray) else venda[21]
    
            vendas_decodificados.append((id_venda, id_produto, nome_produto, id_usuario, nome_usuario, qtd_produto, dt_registro, forma_envio, transportadora, cep, rua,
                bairro, cidade, estado, numero, complemento, valor_frete, valor_total_compra, id_pagamento, forma_pagamento, temporario, obs))
        
        return vendas_decodificados
    
@admin_bp.route("/admin")
@login_required_admin
def admin_home():
    dados_estatisticas = Admin_Routes.obter_estatisticas()

    return render_template('admin/templates/dashboard.html', 
                           vendas_ultimos_7_dias=dados_estatisticas['vendas_ultimos_7_dias'],
                           faturamento_ultimos_7_dias=dados_estatisticas['faturamento_ultimos_7_dias'],
                           vendas_totais=dados_estatisticas['vendas_totais'],
                           faturamento_total=dados_estatisticas['faturamento_total'])

@admin_bp.route("/redirect-admin/<string:diretorio>")
@login_required_admin
def redirect_route_admin(diretorio):
    return render_template(f"admin/templates/{diretorio}.html")

@admin_bp.route("/todos-os-produtos-admin")
@login_required_admin
def todos_os_produtos_admin():
    todos_os_produtos = Admin_Routes.obter_todos_os_produtos()

    return render_template('admin/templates/todos-os-produtos.html', todos_os_produtos=todos_os_produtos)
    
@admin_bp.route("/todas-as-vendas-admin")
@login_required_admin
def todas_as_vendas_admin():
    todas_as_vendas = Admin_Routes.obter_todas_as_vendas()

    return render_template('admin/templates/todas-as-vendas.html', todas_as_vendas=todas_as_vendas)

@admin_bp.route("/vendas-por-clientes-admin", methods=["GET", "POST"])
@login_required_admin
def todas_as_vendas_admin_cliente():
    if request.method == "POST":
        cliente_id = request.form.get('cliente_id')
        todas_as_vendas_cliente = Admin_Routes.obter_todas_as_vendas_cliente(cliente_id)

        return render_template('admin/templates/vendas-por-cpf.html', todas_as_vendas_cliente=todas_as_vendas_cliente)
    else:
        return render_template('admin/templates/vendas-por-cpf.html', todas_as_vendas_cliente=None)

@admin_bp.route("/id_pagamento-por-clientes-admin", methods=["GET", "POST"])
@login_required_admin
def id_pagamento_admin_cliente():
    if request.method == "POST":
        cliente_id = request.form.get('cliente_id')
        id_pagamentos = Admin_Routes.obter_todos_id_pagamentos_cliente(cliente_id)

        return render_template('admin/templates/gerar-os.html', id_pagamentos=id_pagamentos)
    else:
        return render_template('admin/templates/gerar-os.html', id_pagamentos=None)

@admin_bp.route("/gerar-os-pagamento-admin", methods=["GET", "POST"])
@login_required_admin
def gerar_os_pagamento_admin():
    if request.method == "POST":
        id_pagamento = request.form.get('id_pagamento')
        os_gerada_pagamentos = Admin_Routes.obter_todas_as_infos_os(id_pagamento)

        return render_template('admin/templates/os-gerada.html', os_gerada_pagamentos=os_gerada_pagamentos)
    else:
        return render_template('admin/templates/os-gerada.html', os_gerada_pagamentos=None)

@admin_bp.route("/cadastrar-produto-admin")
@login_required_admin
def cadastrar_produto_admin():
    dados = Admin_Routes.obter_tipo_produto()
    return render_template('admin/templates/cadastrar-produto.html', 
                           tipos_produto=dados['tipos_produto'],
                           categorias_produto=dados['categorias_produto'])

@admin_bp.route("/todos-os-clientes-admin")
@login_required_admin
def todos_os_clientes_admin():
    clientes = Admin_Routes.obter_todos_cientes_admin()
    return render_template('admin/templates/todos-os-clientes.html', clientes=clientes)
    
@admin_bp.route("/todos-os-aniversariantes-admin")
@login_required_admin
def todos_os_aniversariantes_admin():
    clientes = Admin_Routes.obter_todos_aniversariantes_admin()
    return render_template('admin/templates/aniversariantes.html', clientes=clientes)

@admin_bp.route("/avise-quando-chegar-admin")
@login_required_admin
def avise_quando_chegar_admin():
    avisar = Admin_Routes.avisar_quando_chegar()
    return render_template('admin/templates/avisar-quando-chegar.html', avisar=avisar)

@admin_bp.route("/cadastrar-produto-insert", methods=['POST'])
@login_required_admin
def cadastrar_produto_insert():
    try:
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        valor = float(request.form.get('valor').replace(',', '.'))
        tipo_produto = request.form.get('tipo_produto')
        dt_cadastro = datetime.now()
        qtd_comprada = int(request.form.get('qtd_comprada'))
        variacao = int(request.form.get('variacoes')) if request.form.get('variacoes') else None
        tipo = request.form.get('Tipo')
        peso = float(request.form.get('peso'))
        altura = float(request.form.get('altura'))
        largura = float(request.form.get('largura'))
        comprimento = float(request.form.get('comprimento'))
        
        imagem = request.files['imagem']
        imagem_filename = None
        
        if imagem and imagem.filename:
            nome_imagem = nome.strip()
            nome_imagem = nome_imagem.replace(" ", "").lower()  # Remover espaços e colocar em minúsculo
            
            if tipo_produto == "Maquiagem":
                upload_dir = os.path.join(os.getcwd(), 'static/images/maquiagem/')
            else:
                upload_dir = os.path.join(os.getcwd(), 'static/images/skincare/')
            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)
            imagem_filename = os.path.join(upload_dir, f"{nome_imagem}.png")
            imagem.save(imagem_filename)

        sucesso = Admin_Routes.inserir_produto(nome, descricao, valor, tipo_produto, dt_cadastro, qtd_comprada, variacao, tipo, peso, altura, largura, comprimento, imagem_filename)

        if sucesso:
            flash("Produto cadastrado com sucesso!", "success")
            return redirect(define_rota('/admin'))
        else:
            flash("Erro ao cadastrar produto. Tente novamente.", "danger")
            return redirect(define_rota('/admin'))
    
    except Exception as e:
        print(f"Erro ao processar cadastro: {e}")
        flash("Erro interno ao cadastrar produto.", "danger")
        return redirect(define_rota('/admin'))


@admin_bp.route("/submit-create-user-admin", methods=['POST'])
@login_required_admin
def cadastrar_cliente_admin_insert():
    try:
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
        senha = "LDL987654321*"
        
        sucesso = Admin_Routes.insert_user_admin(CPF, nome, telefone, email, nascimento, rua, numero, complemento, cep, cidade, estado, senha)
        
        if sucesso:
            flash("Cliente cadastrado com sucesso!", "success")
        else:
            flash("Erro ao cadastrar cliente. Tente novamente.", "danger")
        
        return redirect(define_rota('/admin'))
    
    except Exception as e:
        print(f"Erro ao processar cadastro: {e}")
        flash("Erro interno ao cadastrar cliente.", "danger")

        return redirect(define_rota('/admin'))

@admin_bp.route('/buscar-produtos-admin', methods=['POST'])
@login_required_admin
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
    
@admin_bp.route('/buscar-produtos-update-admin', methods=['POST'])
@login_required_admin
def buscar_produtos_update():
    termo = request.form.get('q', '').strip() 

    if len(termo) < 3:
        return jsonify([])

    produtos = Admin_Routes.procurar_produtos_update(termo)

    produtos_formatados = [
        {"id": p[0], 
         "nome": p[1].decode("utf-8"),
         "valor": p[2],
         "qtd_comprada": p[3],
        } 
    for p in produtos]
    
    return jsonify(produtos_formatados)

@admin_bp.route('/buscar-clientes-admin', methods=['POST'])
@login_required_admin
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
@login_required_admin
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
            else:
                
                id_tabela = Email_Routes.get_infos_venda_email_admin(id_pagamento)
                Email_Routes.enviar_email_compra_cartao_admin(id_tabela)

                flash("Venda cadastrada com sucesso!", "success")
                return redirect(define_rota('/admin'))

    except Exception as e:
        print(f"Erro ao cadastrar venda: {e}")
        flash("Erro interno ao cadastrar venda.", "danger")
        return redirect(define_rota('/admin'))
        
@admin_bp.route('/quantidade-produto-update', methods=['POST'])
@login_required_admin
def cadastrar_produto_admin_update():
    try:
        produto_id = request.form.get('produto_id')
        produto_qtd_atual = int(request.form.get('produto_qtd'))
        produto_qtd_add = int(request.form.get('qtd_add'))
        dt_registro = datetime.now()
        
        qtd_final = produto_qtd_atual + produto_qtd_add
        
        insert_update_produto = Admin_Routes.insert_update_produto(produto_id, qtd_final, dt_registro)

        if not insert_update_produto:
            flash("Erro ao processar Atualização de Produto!", "danger")
            return redirect(define_rota('/admin'))
        else:
            flash("Venda cadastrada com sucesso!", "success")
            return redirect(define_rota('/admin'))

    except Exception as e:
        print(f"Erro ao atualizar produto: {e}")
        flash("Erro interno ao atualizar produto", "danger")
        return redirect(define_rota('/admin'))

@admin_bp.route("/aprovar-pagamento-pix")
@login_required_admin
def aprovar_pagamento_pix():
    pagamento = Admin_Routes.obter_todos_pagamentos_pendentes()
    return render_template('admin/templates/aprovar-pagamentos.html', pagamento=pagamento)   
    
@admin_bp.route("/aceitar-pagamento-pix-admin", methods=["POST"])
@login_required_admin
def aceitar_pagamento():
    id_pagamento = request.form.get('id_pagamento')

    try:
        
        sucess = Admin_Routes.aprovar_pagamento_pix_admin(id_pagamento)
        
        if sucess:
            flash("Pagamento Aceito com sucesso!", "success")
            return redirect(define_rota('/admin'))
        else:
            flash("Erro ao Aceitar Pagamento!", "danger")
            return redirect(define_rota('/admin'))
            
    except Exception as e:
        db.rollback()
        flash(f"Erro ao aprovar pagamento: {str(e)}", "danger")

    return redirect(define_rota('/admin'))