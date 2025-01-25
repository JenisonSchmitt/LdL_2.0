from conection import conectar_db

class Skincare_Routes:

    # Função para buscar os produtos mais vendidos
    def obter_produtos_skincare_mais_vendidos():
        db = conectar_db()
        cursor = db.cursor()

        query = "SELECT id, nome, valor, tipo_produto, imagem FROM produtos WHERE tipo_produto = 'Skincare' ORDER BY nome ASC LIMIT 8"
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

            produtos_decodificados.append((id_produto, nome_produto, valor_produto, imagem_produto))
        
        return produtos_decodificados
        
    def obter_produtos_skincare():
        db = conectar_db()
        cursor = db.cursor()

        query = """
            SELECT p.id, p.nome, p.valor, tp.nome, p.imagem AS tipo
            FROM produtos p
            INNER JOIN tipo_produtos tp ON p.tipo = tp.id
            WHERE tp.categoria = 'Skincare' AND p.tipo_produto = 'Skincare'
            ORDER BY p.nome ASC
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

            produtos_decodificados.append((id_produto, nome_produto, valor_produto, tipo_produto, imagem_produto))
        
        return produtos_decodificados
    
    def obter_tipos_skincare():
        db = conectar_db()
        cursor = db.cursor()

        query = "SELECT id, nome FROM tipo_produtos WHERE categoria = 'Skincare'"
        cursor.execute(query)
        
        tipos = cursor.fetchall()
        cursor.close()
        db.close()

        tipos_decodificados = []
        for tipo in tipos:
            id_tipo = tipo[0].decode('utf-8') if isinstance(tipo[0], bytearray) else tipo[0]
            nome_tipo = tipo[1].decode('utf-8') if isinstance(tipo[1], bytearray) else tipo[1]
            tipos_decodificados.append((id_tipo, nome_tipo))
        
        return tipos_decodificados