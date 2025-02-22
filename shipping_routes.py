from flask import Blueprint, jsonify, request, session
import requests
import json

shipping = Blueprint('shipping_routes', __name__)

SECRET_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNzk4N2MzZWU4YTVkMTBmZGE1MzQyNGZiM2M2YWFkZjBmMWE5NDM1YmFlMmQ0N2QwNThlODExYTg0ZTI4ZGE2ZGUzMjJmMTA0ODBmNzE0NjQiLCJpYXQiOjE3Mzg1MDQzNTAuODQ5NjE2LCJuYmYiOjE3Mzg1MDQzNTAuODQ5NjE3LCJleHAiOjE3NzAwNDAzNTAuODM3MjU2LCJzdWIiOiI5YWY3NjRlZS0xOTU2LTRlM2MtODUwZS00OGVmYjlkMGQyNzQiLCJzY29wZXMiOlsic2hpcHBpbmctY2FsY3VsYXRlIl19.VES2A0ymrd57WGIn0guKi8iDKsraPlLrrzDn4E-eYoY8iw__nqJS2g_NxmaxMyS6O19OpIjAJQgV8DuY61MNxoTywQPFXFELTbH6LtonVxhXIXPOXl5qUsdEyFS1IPqQbelEDlaaICHLxCjqNQv7b_24y9E6E2zPh73ZlHjP9YHBrG22HWzYhsI_6Pi292ahoUbh4OIkW32E-xI4zLk2zeYBdsDdxFu6J261eK-zx1QuExisItTa3NlLNrEBXwJolFLUyM-XHU0e4z7nKuk0KZVkgTtd4K_7txlBsQ3btVmd9gdcUYWeJeiZTO46ASTHeCXZRz5DMB5IqgsqMPtnaoun1lKwJ_WQbLc-LsprgmtX0sw4RLM5bmjjMg_iivwMbbNiBnQ62tziTeU09jS0ZUMZU2N9QSMDbjDQyOVoeWg3IYFLMvqfyCdiGrfRC6JCpWO70B7n5AfFh-V-O-8QSLcMUPl2q4T12XrnCVcNfHtWNlOyf9E2tYKVKtbr9YNDeyDORVfBS3nGvUSje1bGHP6Bpi9smlRJ9GV6sKSGQJAC45kQp8jEBTBT8WCFbkAZzL4FRicCzmBTLQ6mYQWtbjGsCAiyjMBRcx0iKq3qKa-SHEKpl-7Br4fZK3o2MEIHb-lcx7D1R08fHj2bA_974o1PMo3xkTEHFW1Tqijfgfw"

@shipping.route('/calculate_shipping', methods=['POST'])
def calculate_shipping():
    altura = round(session.get('altura_total', 0), 2)
    largura = round(session.get('largura_total', 0), 2)
    comprimento = round(session.get('comprimento_total', 0), 2)
    peso = round(session.get('peso_total', 0), 2)
    peso = peso / 1000
    
    cep = request.json.get('cep')
    if not cep:
        return jsonify({'error': 'CEP não fornecido'}), 400

    payload = {
        "from": {"postal_code": "88701270"},
        "to": {"postal_code": cep},
        "package": {"height": altura, "width": largura, "length": comprimento, "weight": peso}
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {SECRET_KEY}'
    }

    url = 'https://www.melhorenvio.com.br/api/v2/me/shipment/calculate'
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Erro ao fazer a requisição'}), 500

    if response.status_code == 200:
        session['peso_total'] = 0
        session['largura_total'] = 0
        session['altura_total'] = 0
        session['comprimento_total'] = 0
        
        shipping_options = response.json()

        # Filtrar as opções que não contêm o erro
        filtered_options = [option for option in shipping_options if 'error' not in option]

        result = []
        for option in filtered_options:
            shipping_data = {}

            if 'price' in option:
                shipping_data['price'] = option['price']
            if 'company' in option and 'name' in option['company']:
                shipping_data['namecompany'] = option['company']['name']
            if 'name' in option:
                shipping_data['name'] = option['name']
            if 'custom_delivery_range' in option:
                shipping_data['custom_delivery_range'] = option['custom_delivery_range']

            result.append(shipping_data)

        return jsonify(result), 200
    else:
        return jsonify({"error": "Erro ao obter as opções de frete."}), 500
