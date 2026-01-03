import pymysql

#função para chamar e não precisar escrever esse código toda hora
def conecta():
    global con
    con = pymysql.connect( 
        host='localhsot',
        user='root',
        database='db_meusprodutos',
        password='Anninha16!',
        cursorclass=pymysql.cursors.DictCursor
        )
#função para realizar consulta na tabela produtos
def consulta_produtos():
    conecta()

    with con.cursor() as c:
        sql = "SELECT * FROM produtos"
    c.execute
    res = c.fetchall()
    print(res)
    print()

#mostrar os dados retornados, um por linha, iterando sobre o resultado
    for linha in res:
        print(f"Produto {linha['id_produto']}: {linha['nome_produto']}")

def consulta_autor():
    conecta()

    with con.cursor() as c:
        sql = "SELECT * FROM tbl_autores"
        c.execute(sql)
        res = c.fetchall()

        for linha in res:
            print(f"Autor: {linha['NomeAutor']} {linha['SobrenomeAutor']}")

#Cadastro de um novo registro no sistema: novo produto
Produto = input("Digite o novo produto para cadastro:")

try:
    conecta()

    cursor = con.cursor()

    sql = 'INSERT INTO produtos (NomeProduto) VALUES (%s)' #usando placeholders para evitar SQL injection
    cursor.execute(sql, (Produto))
    con.commit

    print(f"O produto {Produto} foi cadastrado com sucesso!")
except pymysql.Error as e:
    print('Erro ao cadastrar na editora', e)
    con.rollback()

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
        print("Conexão finalizada com sucesso!")

