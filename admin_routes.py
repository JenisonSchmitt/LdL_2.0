from flask import Blueprint, render_template
from login_required import login_required_admin
from conection import conectar_db
from datetime import datetime, timedelta

admin_bp = Blueprint('admin', __name__)

class Admin_Routes:
     
    def obter_estatisticas():
        db = conectar_db()
        cursor = db.cursor()

        sete_dias_atras = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')

        query_total = """
        SELECT 
            Count(v.id) AS vendas_totais,
            SUM(v.valor_total_produto) AS faturamento_total
        FROM vendas v
        WHERE v.obs IS NOT NULL AND v.id_pagamento IS NOT NULL AND v.forma_pagamento IS NOT NULL;
        """
        
        query_ultimos_7_dias = f"""
        SELECT 
            Count(v.id) AS vendas_ultimos_7_dias,
            SUM(v.valor_total_produto) AS faturamento_ultimos_7_dias
        FROM vendas v
        WHERE v.dt_registro >= '{sete_dias_atras}' AND v.obs IS NOT NULL AND v.id_pagamento IS NOT NULL AND v.forma_pagamento IS NOT NULL;
        """

        cursor.execute(query_total)
        dados_totais = cursor.fetchone()

        cursor.execute(query_ultimos_7_dias)
        dados_ultimos_7_dias = cursor.fetchone()

        cursor.close()
        db.close()

        vendas_totais = dados_totais[0] if dados_totais[0] else 0
        faturamento_total = dados_totais[1] if dados_totais[1] else 0
        vendas_ultimos_7_dias = dados_ultimos_7_dias[0] if dados_ultimos_7_dias[0] else 0
        faturamento_ultimos_7_dias = dados_ultimos_7_dias[1] if dados_ultimos_7_dias[1] else 0

        return {
            'vendas_ultimos_7_dias': vendas_ultimos_7_dias,
            'faturamento_ultimos_7_dias': faturamento_ultimos_7_dias,
            'vendas_totais': vendas_totais,
            'faturamento_total': faturamento_total
        }


@admin_bp.route("/admin")
#@login_required_admin
def admin_home():
    dados_estatisticas = Admin_Routes.obter_estatisticas()

    return render_template('admin/templates/dashboard.html', 
                           vendas_ultimos_7_dias=dados_estatisticas['vendas_ultimos_7_dias'],
                           faturamento_ultimos_7_dias=dados_estatisticas['faturamento_ultimos_7_dias'],
                           vendas_totais=dados_estatisticas['vendas_totais'],
                           faturamento_total=dados_estatisticas['faturamento_total'])

@admin_bp.route("/redirect-admin/<string:diretorio>")
@login_required_admin
def redirect_route_admin(diretorio):
    return render_template(f"admin/templates/{diretorio}.html")