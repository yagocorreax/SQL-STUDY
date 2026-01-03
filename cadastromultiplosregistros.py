import pymysql

#Cadastrar múltiplos registros de uma vez no sistema, método cursor.executemany()

def conecta():
    global con
    con = pymysql.connect(
        host='localhost',
        user='root',
        database='db_meusLivros',
        password='16092005',
        cursorclass=pymysql.cursors.DictCursor
        )

editora1 = input("Qual nome da primeira editora?")
editora2 = input("Qual nome da segunda editora?")
editora3 = input("Qual nome da terceira editora?")

editoras=(editora1, editora2, editora3)

try:
    conecta()
    cursor = con.cursor()

#Inserir registros na tabela
    sql = 'INSERT INTO tbl_editoras (NomeEditora) VALUES (%S)'
    cursor.executemany(sql, editoras)
    con.commit()

    print(f"Editoras cadastradas com sucesso!")

except pymysql.Error as e:
    print(f"Erro ao cadastrar as editoras", e)
    con.rollback()
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print("Conexão encerrada!")




