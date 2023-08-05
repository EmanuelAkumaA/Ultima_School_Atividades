import sqlite3

conexao = sqlite3.connect('evento_db.sqlite3')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS organizadores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    cpf TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS eventos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    data TEXT NOT NULL,
    local TEXT NOT NULL,
    organizador_id INTEGER NOT NULL,
    FOREIGN KEY (organizador_id) REFERENCES organizadores(id)
);
''')
conexao.commit()

#TESTE PARA ADD INFOS

cursor.execute('''
INSERT INTO organizadores (nome, email, cpf) VALUES
('João', 'joao@gmail.com', '111.111.111-11'),
('Maria', 'maria@gmail.com', '222.222.222-22'),
('Pedro', 'pedro@gmail.com', '333.333.333-33');
''')


cursor.execute('''
INSERT INTO eventos (titulo, data, local, organizador_id) VALUES
('Festa de Aniversário', '30/05/2022', 'Rua X, nº 50', 1),
('Palestra de Tecnologia', '10/06/2022', 'Auditório da Empresa Y', 2),
('Curso de Programação', '15/07/2022', 'Universidade Z', 3);
''')

conexao.commit()
conexao.close()

