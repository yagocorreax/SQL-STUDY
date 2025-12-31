import mysql.connector
from mysql.connector import Error

try:
    cnx = mysql.connector.connect(host='localhost', database='db_meusprodutos', user='root', password='Anninha16!')

    inserir_produtos =      """
                        INSERT INTO produtos(id_produto, nome_produto, valor, quantidade)
                            VALUES
                            (1, 'Iphone 16', 6200, 5),
                            (2, 'Macbook', 10000, 7),
                            (3, 'Iphone 11', 1200, 6),
                            (4, 'Iphone 14', 3400, 3)
                            """

    cursor = cnx.cursor()
    cursor.execute(inserir_produtos)
    cnx.commit()

    print(cursor.rowcount, "Registros inseridos na tabela!")
    cursor.close()

except Error as erro:
    print("Falha ao inserir dados no MySQL: ", erro)
finally:
    if (cnx.is_connected()):
       cnx.close()
       print("Conexão ao MySQL finalizada!")
                            