#Este registro possui mais de um campo para inserção de dados: tbl_autores
import pymysql

def conecta():
    global con
    con = pymysql.connector(
        host='localhost',
        user='root',
        database='db_meusLivros',
        password='16092005'
    )

nome_autor = input("Digite o nome do autor a cadastrar?")
sobrenome_autor = input("Digite o sobrenome do autor?")

try:
    conecta()
    cursor = con.cursor
    sql = 'INSERT INTO tbl_autores (nome_autor, sobrenome_autor) VALUES (%s, %s)'
    cursor.execute(sql, (nome_autor, sobrenome_autor))
    con.commit()

    print(f'o autor {nome_autor} {sobrenome_autor} foi cadastrado com sucesso!')
except pymysql.Error as e:
    print('Erro ao cadastrar o autor', e)
    con.rollback()
finally:
       cursor.close()
       con.close()
       print("Até mais, operação realizada!")
       
 

    