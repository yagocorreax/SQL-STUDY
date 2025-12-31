import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(
        host='localhost',
        database='cadastro_produtos',
        user='root',
        password='sua_senha'
    )

    consulta_sql = "SELECT * FROM tbl_produtos"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()

    print("Número total de registros retornados: ", cursor.rowcount)

    print("\nMostrar os produtos cadastrados:")
    for linha in linhas:
        print("ID Produto:", linha[0])
        print("Nome:", linha[1])
        print("Preço:", linha[2])
        print("Quantidade:", linha[3], "\n")

except Error as e:
    print("Erro ao acessar tabela MySQL", e)

finally:
    if con.is_connected():
        cursor.close()
        con.close()
        print("Conexão ao MySQL encerrada")