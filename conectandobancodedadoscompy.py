import mysql.connector

try:
    con = mysql.connector.connect(host='localhost',database='loja_db',user='root',password='Anninha16!')
    if con.is_connected():
        print('conexão realizada com sucesso')
except mysql.connector.Error as error:
    print(f"ERRO: não foi possível conectar ao banco 'loja_db'. Detalhes: {error}")
finally:
    if 'con' in locals() and con.is_connected():
        con.close()
        