from flask import flash, Blueprint, request, redirect, session
from conection import conectar_db, define_rota
from login_required import login_required
from emails_routes import Email_Routes
import re
from validate_docbr import CPF
import requests
import bcrypt

users = Blueprint('users_routes', __name__)
PREFIXO = '@ldl##Lujinha_2519-!!!'

class Users_Routes:

    def gerar_hash_senha(senha):
        senha_com_prefixo = PREFIXO + senha
        salt = bcrypt.gensalt()  # Gera um salt aleatório
        hash_senha = bcrypt.hashpw(senha_com_prefixo.encode('utf-8'), salt)
        return hash_senha

    def verificar_senha(senha, hash_senha):
        senha_com_prefixo = PREFIXO + senha
        return bcrypt.checkpw(senha_com_prefixo.encode('utf-8'), hash_senha.encode('utf-8'))

    def validar_cpf(cpf):
        cpf_validator = CPF()
        return cpf_validator.validate(cpf)

    def verificar_email_hunter(email):
        api_key = '30c2a5e6d626e049f63a64908fe3377891b1b156'
        url = f'https://api.hunter.io/v2/email-verifier?email={email}&api_key={api_key}'
        response = requests.get(url)
        data = response.json()
        
        if data['data']['status'] == 'valid':
            return True
        return False

    def insert_user(self, CPF, nome, telefone, email, nascimento, rua, numero, complemento, cep, cidade, estado, senha):
        if not Users_Routes.validar_cpf(CPF):
            flash('CPF inválido!', 'danger')
            return

        if not Users_Routes.verificar_email_hunter(email):
            flash('Email inválido!', 'danger')
            return
        
        # Gera o hash da senha com o prefixo
        hash_senha = Users_Routes.gerar_hash_senha(senha)

        db = conectar_db()  
        cursor = db.cursor()
        try:
            query = '''
                INSERT INTO usuarios (CPF, nome, telefone, email, nascimento, rua, numero, complemento, cep, cidade, estado, senha)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''
            parameters = (CPF, nome, telefone, email, nascimento, rua, numero, complemento, cep, cidade, estado, hash_senha)

            cursor.execute(query, parameters) 
            db.commit()

            session['user_email'] = email
            Email_Routes.enviar_email_conta_nova()
            return True
        except Exception as e:
            flash(f'Erro ao cadastrar usuário: {str(e)}', 'danger')
            return False
        finally:
            db.close()

    def login_user(self, email, senha):
        db = conectar_db()  
        cursor = db.cursor()
        try:
            # Busca o hash da senha, id e nível do usuário no banco de dados
            query = '''
                SELECT senha, id, nivel FROM usuarios WHERE email = %s
            '''
            cursor.execute(query, (email,))
            result = cursor.fetchone()

            if result:
                hash_senha_armazenado = result[0]  # Hash da senha armazenada
                user_id = result[1]  # ID do usuário
                user_nivel = result[2]  # Nível do usuário

                # Verifica se a senha fornecida corresponde ao hash armazenado
                # Converte a senha fornecida para bytes (com o prefixo)
                senha_bytes = (PREFIXO + senha).encode('utf-8')
                
                # Converte o hash armazenado para bytes (se ainda não for)
                if isinstance(hash_senha_armazenado, str):
                    hash_senha_armazenado = hash_senha_armazenado.encode('utf-8')

                if bcrypt.checkpw(senha_bytes, hash_senha_armazenado):
                    return {
                        'success': True,
                        'id': user_id,
                        'nivel': user_nivel
                    }
            
            # Se o usuário não for encontrado ou a senha estiver incorreta
            return {
                'success': False,
                'message': 'E-mail ou senha incorretos.'
            }
        except Exception as e:
            flash(f'Erro ao realizar login: {str(e)}', 'danger')
            return {
                'success': False,
                'message': f'Erro ao realizar login: {str(e)}'
            }
        finally:
            db.close()

    def get_usuario_from_db(self, email):
        db = conectar_db()
        cursor = db.cursor()
        try:
            query = '''
                SELECT * FROM usuarios WHERE email = %s
            '''
            
            parameters = (email,)
            cursor.execute(query, parameters)
            result = cursor.fetchone()
    
            if result:
                # Converter bytearrays para string, se necessário
                result = tuple([x.decode('utf-8') if isinstance(x, bytearray) else x for x in result])
                return result
            else:
                return None
            
        except Exception as e:
            print(f"Erro ao consultar o banco de dados: {str(e)}")
            return None
        finally:
            db.close()

    def rec_user(self, CPF, email, senha):
        db = conectar_db()
        cursor = db.cursor()

        hash_senha = Users_Routes.gerar_hash_senha(senha)

        try:
            query = '''
                UPDATE usuarios SET senha = %s WHERE CPF = %s AND email = %s
            '''
            
            parameters = (hash_senha, CPF, email)
            cursor.execute(query, parameters)
            db.commit()
            
            if cursor.rowcount > 0:
                return True
            else:
                return False
                
        except Exception as e:
            print(f"Erro ao consultar o banco de dados: {str(e)}")
            return None
        finally:
            db.close()
            
    def update_user(self, CPF, nome, telefone, email, rua, numero, complemento, cep, cidade, estado):
        db = conectar_db()
        cursor = db.cursor()
        try:
            query = '''
                UPDATE usuarios SET telefone = %s, email = %s, rua = %s, numero = %s, complemento = %s, cep = %s, cidade = %s, estado = %s WHERE CPF = %s AND nome = %s
            '''
            
            parameters = (telefone, email, rua, numero, complemento, cep, cidade, estado, CPF, nome)
            cursor.execute(query, parameters)
            db.commit()
            
            if cursor.rowcount > 0:
                return True
            else:
                return False
                
        except Exception as e:
            print(f"Erro ao consultar o banco de dados: {str(e)}")
            return None
        finally:
            db.close()

    def getIdUserByEmail(self, email):
        db = conectar_db()
        cursor = db.cursor()
        try:
            query = '''
                SELECT id FROM usuarios WHERE email = %s
            '''
            
            parameters = (email,)
            cursor.execute(query, parameters)
            result = cursor.fetchone()
    
            if result:
                result = tuple([x.decode('utf-8') if isinstance(x, bytearray) else x for x in result])
                return result[0]
            else:
                return None
            
        except Exception as e:
            print(f"Erro ao consultar o banco de dados: {str(e)}")
            return None
        finally:
            db.close()
            
            
@users.route("/submit_create_user", methods=["POST"])
def submit_create_user():
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
    senha = request.form['confirme-senha']
    
    users_routes = Users_Routes()
    sucesso = users_routes.insert_user(CPF, nome, telefone, email, nascimento, rua, numero, complemento, cep, cidade, estado, senha)
    
    if sucesso: 
        flash('Usuário cadastrado com sucesso!', 'success')
        return redirect(define_rota('/'))
    else:
        flash(f'Erro ao cadastrar usuário. Verifique se o CPF e E-mail são Válidos ou já Existentes!', 'danger')
        return redirect(define_rota('/'))

@users.route("/submit_update_user", methods=["POST"])
@login_required
def update_user():
    CPF = request.form['cpf']
    nome = request.form['nome']

    telefone = request.form['telefone']
    email = request.form['email']
    rua = request.form['rua']
    numero = request.form['numero']
    complemento = request.form['complemento']
    cep = request.form['cep']
    cidade = request.form['cidade']
    estado = request.form['estado']

    users_routes = Users_Routes()

    sucesso = users_routes.update_user(CPF, nome, telefone, email, rua , numero ,complemento, cep, cidade, estado)
    
    if sucesso:
        flash("Dados atualizados com sucesso!", "success")
        return redirect(define_rota('/acess-account'))
    else:
        flash("Erro ao atualizar dados!", "danger")
        return redirect(define_rota('/acess-account'))
        
@users.route("/submit_rec_user", methods=["POST"])
def submit_rec_user():
    cpf = request.form['CPF']
    email = request.form['email']
    senha = request.form['senha']

    users_routes = Users_Routes()
    
    sucesso = users_routes.rec_user(cpf, email, senha)

    if sucesso:
        session['user_email'] = email
        flash("Senha recuperada com sucesso!", "success")
        return redirect(define_rota('/'))
    else:
        flash("Erro ao recuperar senha, tente novamente.", "danger")
        return redirect(define_rota('/rec-senha'))
        
@users.route("/submit_login_user", methods=["POST"])
def submit_login_user():
    email = request.form['email']
    senha = request.form['senha']

    users_routes = Users_Routes()
    
    resultado = users_routes.login_user(email, senha)

    if resultado['success']:
        session['user_email'] = email
        nivel = resultado['nivel']

        if nivel == "Admin":
            session['user_id'] = resultado['id']
            session['user_nivel'] = resultado['nivel']
        flash("Login realizado com sucesso!", "success")
        return redirect(define_rota('/'))
    else:
        flash("Email ou senha incorretos.", "danger")
        return redirect(define_rota('/account'))
