#INSERINDO DADOS NO BANCO DE DADOS

# Importa a pasta SQL  para dentro do python
import sqlite3 

# Conecta o banco de dados com Python
conexao = sqlite3.connect('atividade_db.sqlite3')
# Cursor para executar comandos SQL, tanto os DML como os DDL 
cursor = conexao.cursor()

############################################################
for i in range(0,10):
    nome = "Danilo" + str(i) #input("Digite o seu nome: ")
    id = i
    cpf = "11111111111" + str(i)
    data_cadastro = "05/10/2022" + str(i)
    endereco = "RIO TINTO" + str(i)

    comando = f"""
        INSERT INTO funcionarios VALUES ({id}, "{nome}", "{cpf}", "{data_cadastro}", "{endereco}");
    """
    cursor.execute(comando)
############################################################
conexao.commit()

conexao.close()
