import mercadopago
from conection import conectar_db, define_rota
from flask import flash, Blueprint, request, redirect, session, render_template, url_for
from login_required import login_required
from produtos_routes import Produtos_Routes

payments = Blueprint('payments_routes', __name__)

#mp = mercadopago.SDK("APP_USR-4600469553095867-013016-55bc599374c7634168cd16c281315305-2239560181")
mp = mercadopago.SDK("TEST-4600469553095867-013016-8d645f3c4561f09c2f6a6b6e68ec5188-2239560181")
SECRET_KEY = "5f98ab6376ab6a34b3a06211532f79caf05f32bb86d7d28405a6cb4b93b0793b"
class Payments_Routes:

    @staticmethod
    @payments.route('/make-payment', methods=['GET', 'POST'])
    @login_required 
    def make_payment():
        valor_total = float(request.form.get('valor-final'))

        item = {
            "title": "Compra Total", 
            "quantity": 1,
            "unit_price": valor_total 
        }

        preference_data = {
            "items": [item],
            "back_urls": {
                "success": define_rota('/sucess-payments'),
                "failure": define_rota('/error-payments'),
                "pending": define_rota('/pending-payments'),
            },
            "auto_return": "approved",
            "payment_methods": {
                "excluded_payment_methods": [
                    {"id": "ticket"}        # Exclui boleto
                ],
                "excluded_payment_types": [
                    {"id": "ticket"}        # Exclui boleto
                ]
            }
        }

        preference = mp.preference().create(preference_data)

        if preference['status'] == 201:
            preference_data = preference['response']
            if 'init_point' in preference_data:
                payment_link = preference_data['init_point']
                return redirect(payment_link) 
            else:
                print("Erro: 'init_point' não encontrado na resposta.")
                flash('Ocorreu um erro ao criar o pagamento. Tente novamente.')
                return redirect(define_rota('/error-payments'))
        else:
            print("Erro ao criar a preferência de pagamento:", preference)
            flash('Ocorreu um erro ao criar o pagamento. Tente novamente.')
            return redirect(define_rota('/error-payments'))
            
    @staticmethod
    @payments.route('/make-payment-pix', methods=['GET', 'POST'])
    @login_required 
    def make_payment_pix():
        valor_total = float(request.form.get('valor-final'))
        valor_total = valor_total * 0.95

        item = {
            "title": "Compra Total", 
            "quantity": 1,
            "unit_price": valor_total 
        }

        preference_data = {
            "items": [item],
            "back_urls": {
                "success": define_rota('/sucess-payments-pix'),
                "failure": define_rota('/error-payments-pix'),
                "pending": define_rota('/pending-payments-pix'),
            },
            "auto_return": "approved",
            "payment_methods": {
                "excluded_payment_methods": [
                    {"id": "credit_card"},  # Exclui cartão de crédito
                    {"id": "ticket"}        # Exclui boleto
                ],
                "excluded_payment_types": [
                    {"id": "credit_card"},  # Exclui cartão de crédito
                    {"id": "ticket"}        # Exclui boleto
                ]
            }
        }

        preference = mp.preference().create(preference_data)

        if preference['status'] == 201:
            preference_data = preference['response']
            if 'init_point' in preference_data:
                payment_link = preference_data['init_point']
                return redirect(payment_link) 
            else:
                print("Erro: 'init_point' não encontrado na resposta.")
                flash('Ocorreu um erro ao criar o pagamento. Tente novamente.')
                return redirect(define_rota('/error-payments'))
        else:
            print("Erro ao criar a preferência de pagamento:", preference)
            flash('Ocorreu um erro ao criar o pagamento. Tente novamente.')
            return redirect(define_rota('/error-payments'))
            
    @payments.route('/notifications', methods=['POST'])
    def notifications():
        try:
            data = request.get_json()
        
            if data and data.get('action') == 'payment.created':
                payment_id = data['data']['id'] 
    
                payment = mp.payment().get(payment_id)  
    
                return '', 200  
    
            else:
                print('Status não 201 ou dados faltando')
                return 'Status não 201 ou dados faltando', 400
    
        except Exception as e:
            print(f"Erro ao processar notificação: {str(e)}")
            return 'Erro no processamento da notificação', 400

    
    @staticmethod
    @login_required
    @payments.route('/sucess-payments')
    def sucess_payments():
        payment_id = request.args.get('payment_id')
        payment = mp.payment().get(payment_id)
    
        payment_method = payment.get('response', {}).get('payment_method', {}).get('type', 'Indefinido')
        
        id_tabela = session.get('id_tabela')

        if not id_tabela:
            flash("Erro: Nenhum ID de tabela encontrado na sessão.", "danger")
            return redirect(define_rota('/'))
    
        produtoRoute = Produtos_Routes()
        
        produtoRoute.set_payment_cart(id_tabela, payment_method, payment_id)
        
        return render_template('sucess-payments.html', payment_method=payment_method)

    @staticmethod
    @login_required
    @payments.route('/error-payments')
    def error_payments():
        return render_template('error-payments.html')

    @staticmethod
    @login_required
    @payments.route('/pending-payments')
    def pending_payments():
        payment_id = request.args.get('payment_id')
        payment = mp.payment().get(payment_id)
    
        payment_method = payment.get('response', {}).get('payment_method', {}).get('type', 'Indefinido')
        
        id_tabela = session.get('id_tabela')

        if not id_tabela:
            flash("Erro: Nenhum ID de tabela encontrado na sessão.", "danger")
            return redirect(define_rota('/'))
    
        produtoRoute = Produtos_Routes()
        
        produtoRoute.set_payment_pix(id_tabela, payment_method, payment_id)
        
        return render_template('pending-payments.html')
        

    @staticmethod
    @login_required
    @payments.route('/sucess-payments-pix')
    def sucess_payments_pix():
        payment_id = request.args.get('payment_id')
        payment = mp.payment().get(payment_id)
        
        payment_method = payment.get('response', {}).get('payment_method', {}).get('type', 'Indefinido')
        valor_pago = payment.get('response', {}).get('transaction_amount', 0)  
        print(valor_pago)
        
        id_tabela = session.get('id_tabela')

        if not id_tabela:
            flash("Erro: Nenhum ID de tabela encontrado na sessão.", "danger")
            return redirect(define_rota('/'))
        
        produtoRoute = Produtos_Routes()
        produtoRoute.set_payment_pix(id_tabela, payment_method, payment_id, valor_pago)
        
        return render_template('sucess-payments.html', payment_method=payment_method)


    @staticmethod
    @login_required
    @payments.route('/pending-payments-pix')
    def pending_payments_pix():
        payment_id = request.args.get('payment_id')
        payment = mp.payment().get(payment_id)
    
        payment_method = payment.get('response', {}).get('payment_method', {}).get('type', 'Indefinido')
        valor_pago = payment.get('response', {}).get('transaction_amount', 0)  
        print(valor_pago)
        
        id_tabela = session.get('id_tabela')

        if not id_tabela:
            flash("Erro: Nenhum ID de tabela encontrado na sessão.", "danger")
            return redirect(define_rota('/'))
    
        produtoRoute = Produtos_Routes()
        
        produtoRoute.set_payment_pix(id_tabela, payment_method, payment_id, valor_pago)
        
        return render_template('pending-payments.html')
        