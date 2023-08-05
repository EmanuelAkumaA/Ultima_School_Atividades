import sqlite3

# Função para conectar ao banco de dados
def conectar_banco():
    return sqlite3.connect("todo_app.db")

# Função para criar um TODO
def criar_todo():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    tarefa = input("Digite a tarefa: ")
    data = input("Digite a data (formato YYYY-MM-DD): ")
    categoria_id = int(input("Digite o ID da categoria: "))

    cursor.execute("INSERT INTO todos (tarefa, data, categoria_id, concluido) VALUES (?, ?, ?, 0)",
                   (tarefa, data, categoria_id))

    conexao.commit()
    conexao.close()

# Função para atualizar um TODO
def atualizar_todo():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    todo_id = int(input("Digite o ID do TODO que deseja atualizar: "))
    tarefa = input("Digite a nova tarefa: ")
    data = input("Digite a nova data (formato YYYY-MM-DD): ")
    categoria_id = int(input("Digite o novo ID da categoria: "))

    cursor.execute("UPDATE todos SET tarefa=?, data=?, categoria_id=? WHERE id=?",
                   (tarefa, data, categoria_id, todo_id))

    conexao.commit()
    conexao.close()

# Função para excluir um TODO
def excluir_todo():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    todo_id = int(input("Digite o ID do TODO que deseja excluir: "))

    cursor.execute("DELETE FROM todos WHERE id=?", (todo_id,))

    conexao.commit()
    conexao.close()

# Função para listar todos os TODOs de um dia especifico.
def lista_todos_dia():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    data = input("Digite a data da tarefa que deseja selecionar: ")

    cursor.execute("SELECT * FROM todos WHERE data = ?", (data,))

    conexao.commit()
    conexao.close()

# Função para marcar uma tarefa como concluida
def marca_concluido():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    todo_id = int(input("Digite o ID da tarefa que deseja marcar como concluída :"))

    cursor.execute("UPDATE todo SET concluido = 1 WHERE id = ?", (todo_id,))

    conexao.commit()
    conexao.close()

# Programa principal
if __name__ == "__main__":
    print("Bem-vindo ao CLI TODO App!")
    print("Selecione uma opção:")
    print("1 - Criar um TODO")
    print("2 - Atualizar um TODO")
    print("3 - Excluir um TODO")
    print("4 - Lista dos afazeres de um dia especifico")
    print("5 - Marcar como concluído")
    opcao = int(input())

    if opcao == 1:
        criar_todo()
    elif opcao == 2:
        atualizar_todo()
    elif opcao == 3:
        excluir_todo()
    elif opcao == 4:
        lista_todos_dia()
    elif opcao == 5:
        marca_concluido()
    else:
        print("Opção inválida.")