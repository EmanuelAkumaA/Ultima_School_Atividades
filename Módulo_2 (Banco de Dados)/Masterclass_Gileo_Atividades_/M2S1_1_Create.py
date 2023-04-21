# importa a pasta SQL  para dentro do python
import sqlite3

# Conecta o banco de dados com Python
conexao = sqlite3.connect('atividade_db.sqlite3')
# Cursor para executar comandos SQL, tanto os DML como os DDL 
cursor = conexao.cursor()
############################################################
sql = """   CREATE TABLE funcionaeios (
            id INT PRIMARY KEY NOT NULL,
            nome TEXT NOT NULL,
            cpf VARCHAR(11) NOT NULL,
            data_cadastro DATE NOT NULL,
            endereco TEXT NOT NULL
            );
            """
###########################################################
cursor.execute(sql)
# A função “commit”, associada à variável “conexao”, chamada logo em seguida,
# Serve para efetivamente salvar as alterações realizadas no banco de dados. 
conexao.commit()
# "close" é chamada para fechar a conexão 
conexao.close()




