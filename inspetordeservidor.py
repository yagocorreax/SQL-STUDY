import mysql.connector

con = mysql.connector.connect(host='localhost',user='root',password='senha')
cursor=con.cursor()

print(f"Versão do servidor: {con.get_server_info()}")

cursor.execute("SELECT CURRENT_USER();") ### Nesse código vamos ao banco de dados, 
usuario = cursor.fetchone()              ## coletamos a versão dele e por fim, pedimos quem é o usuário logado.
print(f"Usuário logado: {usuario[0]}")

cursor.close()
con.close()