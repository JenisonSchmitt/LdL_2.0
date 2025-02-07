import mercadopago
from conection import conectar_db, define_rota
from flask import flash, Blueprint, request, redirect, session, render_template, url_for
from login_required import login_required
from produtos_routes import Produtos_Routes

payments = Blueprint('payments_routes', __name__)

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
        }

        preference = mp.preference().create(preference_data)

        print("Resposta completa da API:", preference)  # Para depuração
        if preference['status'] == 201:  # Verifica se o status de criação foi bem-sucedido
            preference_data = preference['response']
            if 'init_point' in preference_data:
                payment_link = preference_data['init_point']
                return redirect(payment_link)  # Redireciona para o link de pagamento
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
            # Captura os dados da notificação
            data = request.get_json()
    
            print(f"Dados recebidos: {data}")
    
            # Verifica se o status na resposta é igual a 201 (indica sucesso na criação)
            if data and data.get('action') == 'payment.created':
                payment_id = data['data']['id']  # ID do pagamento que foi criado
    
                # Faz uma solicitação para obter os detalhes do pagamento
                payment = mp.payment().get(payment_id)  # Usa o SDK do Mercado Pago para obter o pagamento
    
                print(f"Detalhes do pagamento: {payment}")
    
                print(f'Pagamento aprovado')
                return '', 200  # Resposta 200 OK para o Mercado Pago
    
            else:
                print('Status não 201 ou dados faltando')
                return 'Status não 201 ou dados faltando', 400
    
        except Exception as e:
            # Em caso de erro, imprime o erro e retorna uma resposta 400
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
        
        produtoRoute.set_payment_cart(id_tabela, payment_method)
        
        print(f'Forma de pagamento: {payment_method}')
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
        return render_template('pending-payments.html')
        
