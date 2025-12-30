import mysql.connector

autor_busca = input("Digite o nome do autor:")
con = mysql.connector.connect(host='localhost', database='livros_db', user='root', password='Anninha16!')
cursor = con.cursor()

sql = "SELECT nome_livro FROM tb_livro WHERE nome_autor= %s"
cursor.execute(sql, (autor_busca,))

for (nome_livro,) in cursor:
    print(f"Livro encontrado: {nome_livro}")
    
cursor.close
con.close