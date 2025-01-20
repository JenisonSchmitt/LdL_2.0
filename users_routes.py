from flask import flash
import mysql.connector
from conection import conectar_db  # Supondo que essa função forneça a conexão com o MySQL/MariaDB

class Users_Routes:

    def insert_user(self):
        # Dados manualmente inseridos
        CPF = '54534234212'  # Removendo os pontos e o hífen
        nome = 'njsdghsajd'
        telefone = '56413513213'  # Removendo os parênteses e hífen
        email = 'skdjhsfk@gmail.com'
        nascimento = '2001-06-30'
        rua = '123'
        numero = 123  # Utilizando o tipo numérico correto
        complemento = '123'
        cep = '887012013'
        cidade = 'qwdasd'
        estado = 'dsfsfs'
        senha = '123456789'

        # Conectando ao banco de dados MySQL/MariaDB
        db = conectar_db()  # Certifique-se de que a função 'conectar_db' retorne uma conexão válida para MySQL/MariaDB
        cursor = db.cursor()
        try:
            query = '''
                INSERT INTO usuarios (CPF, nome, telefone, email, nascimento, rua, numero, complemento, cep, cidade, estado, senha)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''
            parameters = (CPF, nome, telefone, email, nascimento, rua, numero, complemento, cep, cidade, estado, senha)

            print(f"Executando consulta com os seguintes parâmetros: {parameters}")
            
            cursor.execute(query, parameters)  # Passando parâmetros corretamente
            db.commit()

            print(f"Linha inserida com sucesso! Último ID inserido: {cursor.lastrowid}")

            flash('Usuário cadastrado com sucesso!', 'success')
        except Exception as e:
            flash(f'Erro ao cadastrar usuário: {str(e)}', 'danger')
            print(f'Erro ao cadastrar usuário: {str(e)}')
        finally:
            db.close()
