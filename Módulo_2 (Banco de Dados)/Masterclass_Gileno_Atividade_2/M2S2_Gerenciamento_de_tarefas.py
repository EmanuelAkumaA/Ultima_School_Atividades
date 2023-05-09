import sqlite3

conexao = sqlite3.connect('gerenciador_tarefas_db.sqlite3')
cursor = conexao.cursor()

sql = """   CREATE TABLE categorias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
                ); """

cursor.execute(sql)
conexao.commit()

sql = """    CREATE TABLE tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                categoria_id INTEGER NOT NULL,
                data DATE NOT NULL,
                realizada INTEGER NOT NULL,
                FOREIGN KEY (categoria_id) REFERENCES categorias(id)
                ); """

cursor.execute(sql)
conexao.commit()

sql = """    CREATE TABLE status (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
                );
      """

cursor.execute(sql)
conexao.commit()
conexao.close()