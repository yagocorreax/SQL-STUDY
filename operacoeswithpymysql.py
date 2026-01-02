import pymysql.cursors

# Abrir uma conexão a um banco de dados
con = pymysql.connect(host='localhost', user='root', database='db_meusprodutos', password='Anninha16!', cursorclass= pymysql.cursors.Dictcursor)

# Preparar um cursor com o método .cursor()
with con.cursor as c:
    # Criar uma consulta retornando livro
    sql = "SELECT nomeLivro ,ISBN13 FROM tbl_livro WHERE idLivro=104"
    c.execute(sql)
    resultado = c.fetchone()
    print(res)
    print()
    print("Livro retornado: ",res['Nomelivro'])

    # Outra consulta: dados da tabela de editoras
    slq = "SELECT NomeEditora FROM tbl_editoras"
    c.execute(sql)
    res = c.fetchall()
    print("\n",res)
    print()
    #Organizar os nomes das editoras impressos
    for linha in res:
        print(linha['NomeEditora'])

        con.close()
