from flask import flash
import mysql.connector
from conection import conectar_db

class Users_Routes:

    def insert_user(self, CPF, nome, telefone, email, nascimento, rua, numero, complemento, cep, cidade, estado, senha):
        db = conectar_db()  
        cursor = db.cursor()
        try:
            query = '''
                INSERT INTO usuarios (CPF, nome, telefone, email, nascimento, rua, numero, complemento, cep, cidade, estado, senha)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''
            parameters = (CPF, nome, telefone, email, nascimento, rua, numero, complemento, cep, cidade, estado, senha)

            print(f"Executando consulta com os seguintes parâmetros: {parameters}")
            
            cursor.execute(query, parameters) 
            db.commit()

            print(f"Linha inserida com sucesso! Último ID inserido: {cursor.lastrowid}")

            flash('Usuário cadastrado com sucesso!', 'success')
        except Exception as e:
            flash(f'Erro ao cadastrar usuário: {str(e)}', 'danger')
            print(f'Erro ao cadastrar usuário: {str(e)}')
        finally:
            db.close()
