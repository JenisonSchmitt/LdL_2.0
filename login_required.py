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
        if 'user_email' not in session or 'user_id' not in session:
            flash("Você precisa estar logado para acessar essa página!", "danger")
            return redirect(define_rota('/account'))
        else:
            id_user = session.get('user_id')
            user_nivel = session.get('user_nivel')
    
            if user_nivel == "Admin" and id_user in [29, 8]:
                return f(*args, **kwargs)
            else:
                flash("Você não tem permissão para acessar essa página!", "danger")
                return redirect(define_rota('/'))
    
    return decorated_function_admin