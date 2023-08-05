# SELECIONANDO DADOS
# importa a pasta SQL  para dentro do python
import sqlite3 

conexao = sqlite3.connect('atividade_db.sqlite3')
cursor = conexao.cursor()

comando = f"""
    SELECT * FROM funcionarios WHERE id < 10;
"""

############################################################
dadoos = cursor.execute(comando)
for dado in dadoos:
    print(dado)
############################################################

conexao.commit()
conexao.close()