import sqlite3

#Função para conectar ao banco de dados
def connectar_banco():
    return sqlite3.connect("categoria_app.db")

# Função para criar uma Categoria
def criar_categoria():
    conexao = connectar_banco()
    cursor = conexao.cursor()

    # id = int(input("Digite o ID da sua categoria: "))
    nome = input("Digite o nome da sua categoria: ")

    cursor.execute("INSERT INTO categorias (nome) VALUES (?)", 
                   (nome,))
    
    conexao.commit()
    print("\nCategoria cadastrada com sucesso!")
    conexao.close()

# Função para atualizar uma Categoria
def atualizar_categoria():
    conexao = connectar_banco()
    cursor = conexao.cursor()

    categoria_id = int(input("Digite o ID da Categoria que você deseja atualizar: "))
    novo_nome = input("Digite o novo nome da Categoria? ")

    cursor.execute("UPDATE categorias SET novo_nome=? WHERE id=?"
                   (novo_nome, categoria_id,))
    
    conexao.commit()
    conexao.close()

# Função para excluir uma Categoria
def excluir_categoria():
    conexao = connectar_banco()
    cursor = conexao.cursor()

    categoria_id = int(input("Digite o ID da Categoria que você deseeja excluir: "))
    cursor.execute("DELETE FROM categorias WHERE id=?", (categoria_id,))

    conexao.commit()
    conexao.close()

# Função para listar todas as categorias
def lista_categoria():
    conexao = connectar_banco()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM categorias")

    conexao.commit()
    conexao.close()

# Programa Principal
if __name__ == "__main__":
    print("Bem-vindo ao CLI Categria APP!")
    print("Por favor, Selecione uma opção:")
    print("1 - Criar nova Categoria.")
    print("2 - Atualizar a Categoria.")
    print("3 - Excluir a Categoria.")
    print("4 - Listar todas as categorias.")
    opcao = int(input())

    if opcao == 1:
        criar_categoria()
    elif opcao == 2:
        atualizar_categoria()
    elif opcao == 3:
        excluir_categoria()
    elif opcao == 4:
        lista_categoria()
    else:
        print("Opção inválida! Tente outra opção.")



