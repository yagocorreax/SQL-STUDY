import pymysql

def conecta():
    global con
    con = pymysql.connect(
        host='localhost',
        user='root',
        database='db_meusLivros',
        password='16092005',
      cursorclass= pymysql.cursors.DictCursor
        )
    
def consulta_editora():
        conecta()

with con.cursor() as c:
        sql = "SELECT * FROM tbl_autores"
        c.execute(sql)
        res = c.fetchall()

        for linha in res:
            print(f'Editora: {linha['IdEditora']}: {linha['NomeEditora']}')

def consulta_autor():
    conecta()

    with con.cursor() as c:
        sql = "SELECT * FROM tbl_autores"
        c.execute(sql)
        res = c.fetchall()

        for linha in res:
            print(f"Autor: {linha['NomeAutor']} {linha['SobrenomeAutor']}")
            
def altera_livro(Livro_atual, Novo_livro):
    
        try:
            conecta()

            cursor = con.cursor
     
            sql = "UPDATE tbl_livros SET NomeLivro = %s WHERE NomeLivro = %s;"
            valores = (Livro_atual, Novo_livro)
        
            cursor.execute(sql, valores)
            con.commit()
            print(f"Livro alterado com sucesso!")

        except Exception as e:
             print("Erro ao atualizar o livro", e)

        finally:
             con.close()
             cursor.close()

editora_id = input("Qual o ID da editora que deseja excluir?")

sql = "DELETE FROM tbl_editoras WHERE IDeditora = " + editora_id
try:
     cursor = con.cursor
     cursor.execute(sql)
     con.commit()

     print("Editora excluída com sucesso!")
except Exception as e:
     con.rollback()
     print(f"Erro ao excluir editora: {e}")

finally:
     con.close()
     cursor.close()

     
     


