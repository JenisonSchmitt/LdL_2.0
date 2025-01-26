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
            return True
        except Exception as e:
            db.rollback()
            print(f"Erro ao salvar no banco: {e}")
            return False
        finally:
            cursor.close()
            db.close()
    
    def save_shipping_data(self, cep, rua, bairro, cidade, estado, numero, complemento, forma_envio, valor_total_compra, valor_frete):
        db = conectar_db()
        cursor = db.cursor()

        # Define a query para inserir os dados de envio
        query = """
            INSERT INTO vendas (cep, rua, bairro, cidade, estado, numero, complemento, forma_envio, valor_total_compra, valor_frete, dt_registro)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
        """

        try:
            # Executa a query com os parâmetros
            cursor.execute(query, (cep, rua, bairro, cidade, estado, numero, complemento, forma_envio, valor_total_compra, valor_frete))
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

    return render_template("shipping-method.html")

@produtos.route('/shipping-method', methods=['POST'])
@login_required
def shipping_method():
    # Obter os dados do formulário
    cep = request.form.get('cep')
    rua = request.form.get('rua')  # Presumindo que você irá capturar rua também (não no HTML atual)
    bairro = request.form.get('bairro')  # O mesmo para bairro
    cidade = request.form.get('cidade')  # E cidade
    estado = request.form.get('estado')  # E estado
    numero = request.form.get('numero')
    complemento = request.form.get('complemento')
    forma_envio = request.form.get('forma_envio')
    valor_total_compra = request.form.get('valor_total_compra')
    valor_frete = request.form.get('valor_frete')

    produtoRoute = Produtos_Routes()
    # Processar e salvar os dados no banco de dados
    # Você pode agora salvar esses dados em seu banco de dados como fez anteriormente
    try:
        # Chame a função que vai salvar os dados, passando as variáveis coletadas do formulário
        # Exemplo:
        resultado = produtoRoute.save_shipping_data(cep, rua, bairro, cidade, estado, numero, complemento, forma_envio, valor_total_compra, valor_frete)
        
        if resultado:
            flash("TUDO CERTO!", "sucess")
            return redirect(define_rota('/'))  # Altere o nome para o da sua próxima rota
        else:
            flash("Houve um erro ao processar sua solicitação, tente novamente!", "danger")
            return redirect(define_rota('/'))  # Altere o nome para o da sua próxima rota

    except Exception as e:
        flash(f"Erro: {str(e)}", "danger")
        return redirect(define_rota('/'))  # Altere o nome para o da sua próxima rota
