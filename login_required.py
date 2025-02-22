from functools import wraps
from flask import session, redirect, url_for, flash
from conection import define_rota
from conection import conectar_db

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_email' not in session:
            flash("Você precisa estar logado para acessar essa página!", "danger")
            return redirect(define_rota('/account'))
        return f(*args, **kwargs) 
    return decorated_function


def login_required_admin(f):
    @wraps(f)
    def decorated_function_admin(*args, **kwargs):
        if 'user_email' not in session:
            flash("Você precisa estar logado para acessar essa página!", "danger")
            return redirect(define_rota('/account'))
        else:
            email = session.get('user_email')
            print(email)
            user_nivel =  getNivelByEmail(email)
            if user_nivel != "Admin":
                flash("Você não tem permissão para acessar essa página!", "danger")
                return redirect(define_rota('/'))
        return f(*args, **kwargs) 
    return decorated_function_admin

def getNivelByEmail(email):
        db = conectar_db()
        cursor = db.cursor()
        try:
            query = '''
                SELECT nivel FROM usuarios WHERE email = %s
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