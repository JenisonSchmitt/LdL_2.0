from flask import flash, Blueprint, request, redirect, session
import mysql.connector
from conection import conectar_db, define_rota
from login_required import login_required

users = Blueprint('users_routes', __name__)

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


            cursor.execute(query, parameters) 
            db.commit()


            flash('Usuário cadastrado com sucesso!', 'success')
            session['user_email'] = email
        except Exception as e:
            flash(f'Erro ao cadastrar usuário: {str(e)}', 'danger')
        finally:
            db.close()

    def login_user(self, email, senha):
        db = conectar_db()  
        cursor = db.cursor()
        try:
            query = '''
                SELECT COUNT(*) FROM usuarios WHERE email = %s AND senha = %s
            '''
            parameters = (email, senha)
            cursor.execute(query, parameters)
            result = cursor.fetchone()

            if result and result[0] > 0:
                return True
            else:
                return False
        except Exception as e:
            flash(f'Erro ao realizar login: {str(e)}', 'danger')
            return False
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
        try:
            query = '''
                UPDATE usuarios SET senha = %s WHERE CPF = %s AND email = %s
            '''
            
            parameters = (senha, CPF, email)
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
@login_required
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
    
    sucesso = users_routes.login_user(email, senha)

    if sucesso:
        session['user_email'] = email
        flash("Login realizado com sucesso!", "success")
        return redirect(define_rota('/'))
    else:
        flash("Email ou senha incorretos.", "danger")
        return redirect(define_rota('/account'))
