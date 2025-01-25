from functools import wraps
from flask import session, redirect, url_for, flash

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_email' not in session:
            flash("Você precisa estar logado para acessar essa página!", "danger")
            return redirect('https://testeecommerce.shop/account')
        return f(*args, **kwargs) 
    return decorated_function
