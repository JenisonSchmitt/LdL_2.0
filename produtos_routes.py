from conection import conectar_db

class Produtos_Routes:
    
    # Função para buscar os produtos mais vendidos
    def obter_produtos():
        db = conectar_db()
        cursor = db.cursor()

        query = "SELECT nome, valor, tipo_produto FROM produtos WHERE dt_cadastro >= '2025-01-01 00:00:00' ORDER BY dt_cadastro DESC LIMIT 10"
        cursor.execute(query)
        
        produtos = cursor.fetchall()
        cursor.close()
        db.close()

        produtos_decodificados = []
        for produto in produtos:
            nome_produto = produto[0].decode('utf-8') if isinstance(produto[0], bytearray) else produto[0]
            valor_produto = produto[1].decode('utf-8') if isinstance(produto[1], bytearray) else produto[1]
            produtos_decodificados.append((nome_produto, valor_produto))
        
        return produtos_decodificados