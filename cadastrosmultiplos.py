import pymysql

#cadastrar múltiplos registros com múltiplos campos de uma vez no sistema, método cursor.executemany()

def conecta():
    global con
    con = pymysql.connect(
        host='localhost',
        user='root',
        database='db_meusLivros',
        password='16092005',
      cursorclass= pymysql.cursors.DictCursor
        )
    
nome_autor1 = input('Qual nome do primeiro autor?')
sobrenome_autor1 = input('Qual o sobrenome do primeiro autor?')
nome_autor2 = input('Qual nome do segundo autor?')
sobrenome_autor2 = input('Qual o sobrenome do segundo autor?')

autores = [(nome_autor1, sobrenome_autor1), (nome_autor2, sobrenome_autor2)]   
    

try:
    conecta()
    cursor = con.cursor()
    
    sql = 'INSERT INTO tbl_autores (Nome autor, Sobrenome Autor) VALUES (%s, %s)'
    cursor.executemany(sql, autores)
    con.commit()

    print(f'Autores cadastrados com sucesso!')

except pymysql.Error as e:
    print(f'Erro ao cadastrar os autores', e)
    con.rollback()

finally:
    cursor.close()
    con.close()
print('Conexão encerrada!')

