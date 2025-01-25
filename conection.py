import mysql.connector

def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="phpmyadmin"
    )

# def conectar_db():
#     return mysql.connector.connect(
#         host="localhost",
#         user="u228502032_TesteLdl2",
#         password="Js19738246*",
#         database="u228502032_TesteLdl2"
#     )