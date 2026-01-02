import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        global con
        con = mysql.connector.connect(
            host='localhost',
            database='db_meusprodutos',
            user='root',
            password='Anninha16!'
        )
        return True
    except Error as erro:
        print(f"Erro de conexão: {erro}")
        return False

def consulta(idprod): 
    try:
        if conectar():
            consulta_sql = "SELECT * FROM produtos WHERE id_produto = " + str(idprod)
            cursor = con.cursor()
            cursor.execute(consulta_sql)
            linhas = cursor.fetchall()

            if not linhas:
                print("Produto não encontrado.")
            
            for linha in linhas:
                print("id:", linha[0])
                print("produto:", linha[1]) 
                print("valor:", linha[2])
            
            cursor.close()
            con.close()
    except Error as erro:
        print("Falha ao consultar a tabela: {}".format(erro))

def atualiza(comando_sql): 
    try:
        if conectar():
            cursor = con.cursor() 
            cursor.execute(comando_sql)
            con.commit()
            print("Preço alterado com sucesso!")
            
            cursor.close()
            con.close()
    except Error as erro:
        print("Falha ao atualizar dados: {}".format(erro))

if __name__ == '__main__':
    print("\n--- Atualização de Produtos ---")
    id_prod = input("Digite o ID do produto: ")

    
    consulta(id_prod)

    novo_valor = input("\nDigite o novo valor do produto: ")

    
    declaracao_update = "UPDATE produtos SET valor = " + novo_valor + " WHERE id_produto = " + id_prod
    
    atualiza(declaracao_update)