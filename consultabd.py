import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(
        host='localhost',
        database='db_meus_livros',
        user='root',
        password='sua_senha'
    )

    consulta_sql = "SELECT * FROM tbl_autores"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()

    print("Número total de registros retornados: ", cursor.rowcount)

    print("\nMostrando os autores cadastrados:")
    for linha in linhas:
        print("ID:", linha[0])
        print("Nome:", linha[1])
        print("Sobrenome:", linha[2], "\n")

except Error as e:
    print("Erro ao acessar a tabela MySQL", e)

finally:
    if con.is_connected():
        cursor.close()
        con.close()
        print("Conexão ao MySQL encerrada")