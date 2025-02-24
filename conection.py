import mysql.connector

def define_rota(caminho):
    rota = "https://testeecommerce.shop"
    #rota = "http://127.0.0.1:5000"

    return rota + caminho

# def conectar_db():
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="lujinhadeluxo"
#     )

def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="u228502032_TesteLdl2",
        password="Js19738246*",
        database="u228502032_TesteLdl2"
    )