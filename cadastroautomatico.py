import mysql.connector

novo_livro = {
    "Título": "Aprendendo python",
    "autor": "Joâo almeida",
}

con = mysql.connector.connect(host="localhost", database="livros_db", user="root", password="Anninha16!")
cursor= con.cursor()

sql= "INSERT INTO tb_livros (aprendendo python, Joâo almeida) VALUES (%s, %s)"
valores = (novo_livro['Título'], novo_livro['autor'])

cursor.execute(sql, valores)
con.commit()
print(f"livro'{novo_livro['Título'] }' inserido com sucesso!")

cursor.close()
con.close()