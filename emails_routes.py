import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, flash, Blueprint, request, redirect, session, render_template
import os
from dotenv import load_dotenv
from conection import define_rota, conectar_db
from login_required import login_required_admin

load_dotenv()

emails = Blueprint('emails_routes', __name__)

smtp_server = os.getenv("SMTP_SERVER")
smtp_port = int(os.getenv("SMTP_PORT"))
email_from = os.getenv("EMAIL_FROM")
email_password = os.getenv("EMAIL_PASSWORD")
email_to = os.getenv("EMAIL_TO")
link = "https://testeecommerce.shop"
link_admin = "https://testeecommerce.shop/admin"
linkwhatsapp = "https://api.whatsapp.com/send?phone=48991383245&text=Olá,%20realizei%20o%20meu%20pagamento,%20segue%20o%20comprovante:"
email_marina = "marinalunasa@gmail.com"
email_jenison = "schmitt.jeni02@outlook.com"


class Email_Routes:
    @staticmethod
    def get_usuario_for_email():
        email = session.get('user_email') 
        db = conectar_db()
        cursor = db.cursor()
        try:
            query = '''
                SELECT id, nome, telefone, email, nascimento FROM usuarios WHERE email = %s
            '''
            
            parameters = (email,)
            cursor.execute(query, parameters)
            result = cursor.fetchone()
            
            if result:
                id_user = result[0]
                nome = result[1].decode('utf-8') if isinstance(result[1], bytearray) else result[1]
                telefone = result[2].decode('utf-8') if isinstance(result[3], bytearray) else result[3]
                email = result[3].decode('utf-8') if isinstance(result[3], bytearray) else result[3]
                nascimento = result[4]
                
                return (id_user, nome, telefone, email, nascimento)
            else:
                return None
                
        except Exception as e:
            print(f"Erro ao consultar o banco de dados: {str(e)}")
            return None
        finally:
            db.close()
            
    @staticmethod
    def get_infos_venda_email(primeiro_id):
        db = conectar_db()
        cursor = db.cursor()
        try:
            query = '''
                SELECT
                    v.id_produto, u.nome AS nome_usuario, v.dt_registro, v.forma_envio, v.transportadora, v.valor_frete, v.valor_total_compra, v.id_pagamento, v.forma_pagamento, u.email AS email_usuario
                FROM
                    vendas v
                JOIN
                    usuarios u ON v.id_usuario = u.id
                WHERE v.id = %s
            '''
            
            parameters = (primeiro_id,)
            cursor.execute(query, parameters)
            result = cursor.fetchone()
            
            if result:
                id_venda = result[0]
                nome = result[1].decode('utf-8') if isinstance(result[1], bytearray) else result[1]
                dt_registro = result[2]
                forma_envio = result[3].decode('utf-8') if isinstance(result[3], bytearray) else result[3]
                transportadora = result[4].decode('utf-8') if isinstance(result[4], bytearray) else result[4]
                valor_frete = result[5]
                valor_total_compra = result[6]
                id_pagamento = result[7].decode('utf-8') if isinstance(result[8], bytearray) else result[8]
                forma_pagamento = result[8].decode('utf-8') if isinstance(result[8], bytearray) else result[8]
                email = result[9].decode('utf-8') if isinstance(result[9], bytearray) else result[9]
                
                return (id_venda, nome, dt_registro, forma_envio, transportadora, valor_frete, valor_total_compra, id_pagamento, forma_pagamento, email)
            else:
                return None
                    
        except Exception as e:
            print(f"Erro ao consultar o banco de dados: {str(e)}")
            return None
        finally:
            cursor.close()
            db.close()
    
    @staticmethod
    def get_all_emails():
        db = conectar_db()
        cursor = db.cursor()
        try:
            query = '''
                SELECT nome, email FROM usuarios
            '''
            cursor.execute(query)
            results = cursor.fetchall()
            
            emails = []
            for result in results:
                nome = result[0].decode('utf-8') if isinstance(result[0], bytearray) else result[0]
                email = result[1].decode('utf-8') if isinstance(result[1], bytearray) else result[1]
                emails.append((nome, email))
            
            return emails
        except Exception as e:
            print(f"Erro ao consultar o banco de dados: {str(e)}")
            return []
        finally:
            db.close()
    
    @staticmethod
    def enviar_email_conta_nova():
        email = Email_Routes.get_usuario_for_email()
        
        if email is None:
            flash("Erro: Nenhum usuário encontrado com o e-mail fornecido.", "error")
            return ""
    
        email_cliente = email[3]
        nome_cliente = email[1]
        Email_Routes.enviar_email_conta_nova_jenison_marina(nome_cliente)
        subject = f"Olá, {nome_cliente}! Bem-vindo(a) a Lujinha de Luxo"
        
        body = f"""
        <div style="font-family: Arial, sans-serif; color: #333; background-color: #F9F3EC; padding: 20px;">
            <div style="background-color: #603F8B; padding: 20px; border-radius: 10px; color: #FFF; text-align: center;">
                <h1 style="margin: 0;">Bem-vindo(a) a Lujinha de Luxo!</h1>
            </div>
            <div style="background-color: #FFF; padding: 20px; border-radius: 10px; margin-top: 20px;">
                <p>Olá, {nome_cliente},</p>
                <p>Estamos muito felizes em tê-lo(a) conosco! Aqui na nossa 'Lujinha', você encontrará os melhores produtos com os melhores preços.</p>
                <p>Acesse agora o nosso site e fique por dentro de todas as novidades com os melhores preços e qualidade!</p>
                <a href="{link}">
                    <div style="background-color: #FFA4DB; padding: 15px; border-radius: 5px; text-align: center; margin: 20px 0;">
                        <h2 style="margin: 0;">Acessar LDL</h2>
                    </div>
                </a>
                <p>Aproveite e comece a comprar agora mesmo!</p>
                <p>Se tiver alguma dúvida, estamos à disposição.</p>
                <p>Atenciosamente,</p>
                <p><strong>Equipe Lujinha de Luxo</strong></p>
            </div>
        </div>
        """
    
        msg = MIMEText(body, "html")
        msg["From"] = email_from
        msg["To"] = email_cliente
        msg["Subject"] = subject
    
        try:
            with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
                server.login(email_from, email_password) 
                server.sendmail(email_from, email_cliente, msg.as_string())
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}", "error")
        
        return ""
        
    @staticmethod
    def enviar_email_conta_nova_jenison_marina(cliente):
        nome_cliente = cliente
        subject = f"Olá! Você possui um novo cliente Cadastrado!"
        
        body = f"""
        <div style="font-family: Arial, sans-serif; color: #333; background-color: #F9F3EC; padding: 20px;">
            <div style="background-color: #603F8B; padding: 20px; border-radius: 10px; color: #FFF; text-align: center;">
                <h1 style="margin: 0;">Novo Cliente Cadastrado!</h1>
            </div>
            <div style="background-color: #FFF; padding: 20px; border-radius: 10px; margin-top: 20px;">
                <p>Olá, você possui um novo cliente: {nome_cliente},</p>
                <p>Acesse agora o painel administrativo e fique por dentro das novidades!</p>
                <a href="{link_admin}">
                    <div style="background-color: #FFA4DB; padding: 15px; border-radius: 5px; text-align: center; margin: 20px 0;">
                        <h2 style="margin: 0;">Acessar LDL</h2>
                    </div>
                </a>
                <p>Atenciosamente,</p>
                <p><strong>Equipe Lujinha de Luxo</strong></p>
            </div>
        </div>
        """
    
        destinatarios = [email_marina, email_jenison]
    
        try:
            with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
                server.login(email_from, email_password) 
    
                for destinatario in destinatarios:
                    msg = MIMEText(body, "html")  
                    msg["From"] = email_from
                    msg["To"] = destinatario
                    msg["Subject"] = subject
    
                    server.sendmail(email_from, destinatario, msg.as_string())

        except Exception as e:
            print(f"Erro ao enviar e-mails: {e}", "error")
        
        return ""  
        
    @staticmethod
    def get_infos_venda_email_admin(id_pagamento):
        db = conectar_db()
        id_pagamento = str(id_pagamento)
        cursor = db.cursor()
        try:
            query = "SELECT id FROM vendas WHERE id_pagamento = %s LIMIT 1;"
            cursor.execute(query, (id_pagamento,))
            result = cursor.fetchone()
            

            if result:
                id_venda = result[0]
                return id_venda
            else:
                return None
                        
        except Exception as e:
            print(f"Erro ao consultar o banco de dados: {str(e)}")
            return None
        finally:
            cursor.close()
            db.close()
    
    @staticmethod
    def enviar_email_compra_cartao(id_tabela):
        primeiro_id = id_tabela[0]
        infos_venda = Email_Routes.get_infos_venda_email(primeiro_id)

        if not infos_venda:
            return ""
    
        nome_cliente = infos_venda[1]
        dt_compra = infos_venda[2]
        forma_envio = infos_venda[3]
        transportadora = infos_venda[4]
        valor_frete = infos_venda[5]
        valor_total_compra = infos_venda[6]
        id_pagamento = infos_venda[7]
        forma_pagamento = infos_venda[8]
        email = infos_venda[9]
        
        if forma_pagamento == "bank_transfer":
            forma_pagamento = "PIX"
        elif forma_pagamento == "credit_card":
            forma_pagamento = "Cartão de Crédito"
        
        if email is None:
            print("E-mail do cliente não encontrado.")
            return ""
            
        Email_Routes.enviar_email_venda_nova_jenison_marina(nome_cliente, dt_compra, forma_envio, transportadora, valor_frete, valor_total_compra, id_pagamento, forma_pagamento)
        subject = f"Olá, {nome_cliente}! Recebemos seu Pedido N° {id_pagamento}"
        
        body = f"""
        <div style="font-family: Arial, sans-serif; color: #333; background-color: #F9F3EC; padding: 20px;">
            <div style="background-color: #603F8B; padding: 20px; border-radius: 10px; color: #FFF; text-align: center;">
                <h1 style="margin: 0;">Recebemos seu Pedido!</h1>
            </div>
            <div style="background-color: #FFF; padding: 20px; border-radius: 10px; margin-top: 20px;">
                <p>Olá, <strong>{nome_cliente}</strong>, recebemos seu Pedido N° <strong>{id_pagamento}</strong></p>
                <p>Ficamos felizes em receber o seu pedido e queremos dizer que já estamos preparando tudo com muito carinho e cuidado!</p>
                <br><p>Segue o resumo do seu pedido:</p>
                <p>Data: <strong>{dt_compra}</strong></p>
                <p>Forma de Envio: <strong>{forma_envio}</strong></p>
                <p>Transporte: <strong>{transportadora}</strong></p>
                <p>Valor Frete: <strong>{valor_frete}</strong></p>
                <p>Valor Total Compra: <strong>{valor_total_compra}</strong></p>
                <p>Forma de Pagamento: <strong>{forma_pagamento}</strong></p>
                <p>Acesse agora o nosso site e descubra ainda mais novidades!</p>
                <a href="{link}">
                    <div style="background-color: #FFA4DB; padding: 15px; border-radius: 5px; text-align: center; margin: 20px 0;">
                        <h2 style="margin: 0;">Acessar LDL</h2>
                    </div>
                </a>
                <p>Entraremos em contato para lhe enviar mais informações!</p>
                <p>Se tiver alguma dúvida, estamos à disposição.</p>
                <p>Atenciosamente,</p>
                <p><strong>Equipe Lujinha de Luxo</strong></p>
            </div>
        </div>
        """
        
        msg = MIMEText(body, "html")
        msg["From"] = email_from
        msg["To"] = email
        msg["Subject"] = subject
        
        try:
            with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
                server.login(email_from, email_password) 
                server.sendmail(email_from, email, msg.as_string())
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}", "error")
        
        return ""
        
    @staticmethod
    def enviar_email_compra_cartao_admin(id_tabela):
        primeiro_id = id_tabela
        infos_venda = Email_Routes.get_infos_venda_email(primeiro_id)

        if not infos_venda:
            return ""
    
        nome_cliente = infos_venda[1]
        dt_compra = infos_venda[2]
        forma_envio = infos_venda[3]
        transportadora = infos_venda[4]
        valor_frete = infos_venda[5]
        valor_total_compra = infos_venda[6]
        id_pagamento = infos_venda[7]
        forma_pagamento = infos_venda[8]
        email = infos_venda[9]
        
        if forma_pagamento == "bank_transfer":
            forma_pagamento = "PIX"
        elif forma_pagamento == "credit_card":
            forma_pagamento = "Cartão de Crédito"
        
        if email is None:
            print("E-mail do cliente não encontrado.")
            return ""
            
        Email_Routes.enviar_email_venda_nova_jenison_marina(nome_cliente, dt_compra, forma_envio, transportadora, valor_frete, valor_total_compra, id_pagamento, forma_pagamento)
        subject = f"Olá, {nome_cliente}! Recebemos seu Pedido N° {id_pagamento}"
        
        body = f"""
        <div style="font-family: Arial, sans-serif; color: #333; background-color: #F9F3EC; padding: 20px;">
            <div style="background-color: #603F8B; padding: 20px; border-radius: 10px; color: #FFF; text-align: center;">
                <h1 style="margin: 0;">Recebemos seu Pedido!</h1>
            </div>
            <div style="background-color: #FFF; padding: 20px; border-radius: 10px; margin-top: 20px;">
                <p>Olá, <strong>{nome_cliente}</strong>, recebemos seu Pedido N° <strong>{id_pagamento}</strong></p>
                <p>Ficamos felizes em receber o seu pedido e queremos dizer que já estamos preparando tudo com muito carinho e cuidado!</p>
                <br><p>Segue o resumo do seu pedido:</p>
                <p>Data: <strong>{dt_compra}</strong></p>
                <p>Forma de Envio: <strong>{forma_envio}</strong></p>
                <p>Transporte: <strong>{transportadora}</strong></p>
                <p>Valor Frete: <strong>{valor_frete}</strong></p>
                <p>Valor Total Compra: <strong>{valor_total_compra}</strong></p>
                <p>Forma de Pagamento: <strong>{forma_pagamento}</strong></p>
                <p>Acesse agora o nosso site e descubra ainda mais novidades!</p>
                <a href="{link}">
                    <div style="background-color: #FFA4DB; padding: 15px; border-radius: 5px; text-align: center; margin: 20px 0;">
                        <h2 style="margin: 0;">Acessar LDL</h2>
                    </div>
                </a>
                <p>Entraremos em contato para lhe enviar mais informações!</p>
                <p>Se tiver alguma dúvida, estamos à disposição.</p>
                <p>Atenciosamente,</p>
                <p><strong>Equipe Lujinha de Luxo</strong></p>
            </div>
        </div>
        """
        
        msg = MIMEText(body, "html")
        msg["From"] = email_from
        msg["To"] = email
        msg["Subject"] = subject
        
        try:
            with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
                server.login(email_from, email_password) 
                server.sendmail(email_from, email, msg.as_string())
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}", "error")
        
        return ""
        
    @staticmethod 
    def enviar_email_compra_pix(id_tabela):
        primeiro_id = id_tabela[0]
        infos_venda = Email_Routes.get_infos_venda_email(primeiro_id)

        if not infos_venda:
            return ""
    
        nome_cliente = infos_venda[1]
        dt_compra = infos_venda[2]
        forma_envio = infos_venda[3]
        transportadora = infos_venda[4]
        valor_frete = infos_venda[5]
        valor_total_compra = infos_venda[6]
        id_pagamento = infos_venda[7]
        forma_pagamento = infos_venda[8]
        email = infos_venda[9]
        
        if forma_pagamento == "bank_transfer":
            forma_pagamento = "PIX"
        elif forma_pagamento == "credit_card":
            forma_pagamento = "Cartão de Crédito"
        
        if email is None:
            print("E-mail do cliente não encontrado.")
            return ""
        
        Email_Routes.enviar_email_venda_nova_jenison_marina(nome_cliente, dt_compra, forma_envio, transportadora, valor_frete, valor_total_compra, id_pagamento, forma_pagamento)
        subject = f"Olá, {nome_cliente}! Recebemos seu Pedido N° {id_pagamento}"
        
        body = f"""
        <div style="font-family: Arial, sans-serif; color: #333; background-color: #F9F3EC; padding: 20px;">
            <div style="background-color: #603F8B; padding: 20px; border-radius: 10px; color: #FFF; text-align: center;">
                <h1 style="margin: 0;">Recebemos seu Pedido!</h1>
            </div>
            <div style="background-color: #FFF; padding: 20px; border-radius: 10px; margin-top: 20px;">
                <p>Olá, <strong>{nome_cliente}</strong>, recebemos seu Pedido N° <strong>{id_pagamento}</strong></p>
                <p>Ficamos felizes em receber o seu pedido! Verifique se o pagamento foi realizado com sucesso e se possível, encaminhe o comprovante via WhatsApp para validar e continuarmos o nosso processo!</p>
                <br><p>Segue o resumo do seu pedido:</p>
                <p>Data: <strong>{dt_compra}</strong></p>
                <p>Forma de Envio: <strong>{forma_envio}</strong></p>
                <p>Transporte: <strong>{transportadora}</strong></p>
                <p>Valor Frete: <strong>{valor_frete}</strong></p>
                <p>Valor Total Compra: <strong>{valor_total_compra}</strong></p>
                <p>Forma de Pagamento: <strong>{forma_pagamento}</strong></p>
                <p>Status Pedido: <strong>Pendente (Envie o Compravante pelo WhatsApp)</strong></p>
                <p>Acesse agora o nosso site e descubra ainda mais novidades!</p>
                <a href="{linkwhatsapp}">
                    <div style="background-color: #FFA4DB; padding: 15px; border-radius: 5px; text-align: center; margin: 20px 0;">
                        <h2 style="margin: 0;">Enviar Comprovante de Pagamento</h2>
                    </div>
                </a>
                <p>Entraremos em contato para lhe enviar mais informações!</p>
                <p>Se tiver alguma dúvida, estamos à disposição.</p>
                <p>Atenciosamente,</p>
                <p><strong>Equipe Lujinha de Luxo</strong></p>
            </div>
        </div>
        """

        msg = MIMEText(body, "html")
        msg["From"] = email_from
        msg["To"] = email
        msg["Subject"] = subject
        
        try:
            with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
                server.login(email_from, email_password) 
                server.sendmail(email_from, email, msg.as_string())
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}", "error")
        
        return ""

    @staticmethod
    def enviar_email_venda_nova_jenison_marina(nome_cliente, dt_compra, forma_envio, transportadora, valor_frete, valor_total_compra, id_pagamento, forma_pagamento):
        forma_pagamento = forma_pagamento

        if forma_pagamento == "bank_transfer":
            forma_pagamento = "PIX"
        elif forma_pagamento == "credit_card":
            forma_pagamento = "Cartão de Crédito"
            
        subject = f"Olá! Você recebeu um novo Pedido!"
        
        body = f"""
        <div style="font-family: Arial, sans-serif; color: #333; background-color: #F9F3EC; padding: 20px;">
            <div style="background-color: #603F8B; padding: 20px; border-radius: 10px; color: #FFF; text-align: center;">
                <h1 style="margin: 0;">Novo Pedido Solicitado!</h1>
            </div>
            <div style="background-color: #FFF; padding: 20px; border-radius: 10px; margin-top: 20px;">
                <p>Olá, você possui um novo Pedido: <strong>{id_pagamento}</strong>,</p>
                <br><p>Segue o resumo do pedido:</p>
                <p>Cliente: <strong>{nome_cliente}</strong></p>
                <p>Data: <strong>{dt_compra}</strong></p>
                <p>Forma de Envio: <strong>{forma_envio}</strong></p>
                <p>Transporte: <strong>{transportadora}</strong></p>
                <p>Valor Frete: <strong>{valor_frete}</strong></p>
                <p>Valor Total Compra: <strong>{valor_total_compra}</strong></p>
                <p>Forma de Pagamento: <strong>{forma_pagamento}</strong></p>
                <p>Acesse agora o painel administrativo e fique por dentro das novidades!</p>
                <a href="{link_admin}">
                    <div style="background-color: #FFA4DB; padding: 15px; border-radius: 5px; text-align: center; margin: 20px 0;">
                        <h2 style="margin: 0;">Acessar LDL</h2>
                    </div>
                </a>
                <p>Atenciosamente,</p>
                <p><strong>Equipe Lujinha de Luxo</strong></p>
            </div>
        </div>
        """
    
        destinatarios = [email_marina, email_jenison]
    
        try:
            with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
                server.login(email_from, email_password) 
    
                for destinatario in destinatarios:
                    msg = MIMEText(body, "html")  
                    msg["From"] = email_from
                    msg["To"] = destinatario
                    msg["Subject"] = subject
    
                    server.sendmail(email_from, destinatario, msg.as_string())

        except Exception as e:
            print(f"Erro ao enviar e-mails: {e}", "error")
        
        return "" 
        
@emails.route("/send-email-client", methods=["GET", "POST"])
@login_required_admin
def send_email_client():
    infos_clientes = Email_Routes.get_all_emails()
    
    assunto = request.form.get('assunto')
    titulo = request.form.get('titulo')
    texto1 = request.form.get('texto1')
    texto2 = request.form.get('texto2')
    link_email_geral = request.form.get('linkemail')
    
    subject = f"{assunto}"
    
    enviados = 0
    falhas = 0
    erros = []

    for nome_cliente, email in infos_clientes:
        if not email or not isinstance(email, str) or "@" not in email:
            print(f"E-mail inválido para {nome_cliente}: {email}")
            falhas += 1
            erros.append(f"E-mail inválido para {nome_cliente}: {email}")
            continue

        body = f"""
        <div style="font-family: Arial, sans-serif; color: #333; background-color: #F9F3EC; padding: 20px;">
            <div style="background-color: #603F8B; padding: 20px; border-radius: 10px; color: #FFF; text-align: center;">
                <h1 style="margin: 0;">{titulo}</h1>
            </div>
            <div style="background-color: #FFF; padding: 20px; border-radius: 10px; margin-top: 20px;">
                <p>Olá, <strong>{nome_cliente}</strong></p>
                <p><strong>{texto1}</strong></p>
                <br><br>
                <p>{texto2}</p>
                <a href="{link_email_geral}">
                    <div style="background-color: #FFA4DB; padding: 15px; border-radius: 5px; text-align: center; margin: 20px 0;">
                        <h2 style="margin: 0;">Acessar</h2>
                    </div>
                </a>
                <p>Atenciosamente,</p>
                <p><strong>Equipe Lujinha de Luxo</strong></p>
            </div>
        </div>
        """

        msg = MIMEText(body, "html")
        msg["From"] = email_from
        msg["To"] = email
        msg["Subject"] = subject

        try:
            with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
                server.login(email_from, email_password)
                server.sendmail(email_from, email, msg.as_string())
            enviados += 1
        except Exception as e:
            print(f"Erro ao enviar e-mail para {email}: {e}")
            falhas += 1
            erros.append(f"Erro ao enviar e-mail para {email}: {e}")

    flash(f"E-mails enviados: {enviados}, E-mails com falha: {falhas}", "success")
    return redirect(define_rota('/admin'))