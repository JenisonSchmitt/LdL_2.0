from conection import conectar_db

class Skincare_Routes:

    # Função para buscar os produtos mais vendidos
    def obter_produtos_skincare_mais_vendidos():
        db = conectar_db()
        cursor = db.cursor()

        query = """SELECT p.id, p.nome, p.valor, p.tipo_produto, p.imagem, p.qtd_comprada, COALESCE(SUM(v.qtd_produto), 0) AS qtd_vendida, p.variacao
        FROM produtos p LEFT JOIN vendas v ON p.id = v.id_produto
        WHERE p.tipo_produto = 'Skincare' AND v.obs IS NOT NULL AND v.id_pagamento IS NOT NULL AND v.forma_pagamento IS NOT NULL
        GROUP BY p.id
        ORDER BY v.qtd_produto DESC
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

            produtos_decodificados.append((id_produto, nome_produto, valor_produto, imagem_produto, qtd_comprada, qtd_vendida, variacao))
        
        return produtos_decodificados
        
    def obter_produtos_skincare():
        db = conectar_db()
        cursor = db.cursor()

        query = """
            SELECT p.id, p.nome, p.valor, tp.nome, p.imagem AS tipo, p.qtd_comprada, COALESCE(SUM(v.qtd_produto), 0) AS qtd_vendida, p.variacao
            FROM produtos p 
            LEFT JOIN vendas v ON p.id = v.id_produto 
            INNER JOIN tipo_produtos tp ON p.tipo = tp.id 
            WHERE tp.categoria = 'Skincare' AND p.tipo_produto = 'Skincare' AND v.obs IS NOT NULL AND v.id_pagamento IS NOT NULL AND v.forma_pagamento IS NOT NULL
            GROUP BY p.id
            ORDER BY p.nome ASC;
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