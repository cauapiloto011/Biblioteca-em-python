import sqlite3

# Conexão com o banco
conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

# Criação da tabela livros
cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER,
    disponivel TEXT CHECK(disponivel IN ('Sim', 'Não')) DEFAULT 'Sim'
)
""")

conn.commit()

def cadastrar_livro(titulo, autor, ano):
    cursor.execute("""
        INSERT INTO livros (titulo, autor, ano, disponivel)
        VALUES (?, ?, ?, 'Sim')
    """, (titulo, autor, ano))
    conn.commit()
    print("Livro cadastrado com sucesso!")

def listar_livros():
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()
    print("\n--- Lista de Livros ---")
    for livro in livros:
        print(f"ID: {livro[0]} | Título: {livro[1]} | Autor: {livro[2]} | Ano: {livro[3]} | Disponível: {livro[4]}")
    print("------------------------\n")

def atualizar_disponibilidade(id_livro):
    cursor.execute("SELECT disponivel FROM livros WHERE id = ?", (id_livro,))
    resultado = cursor.fetchone()

    if resultado:
        nova_disponibilidade = "Não" if resultado[0] == "Sim" else "Sim"
        cursor.execute("UPDATE livros SET disponivel = ? WHERE id = ?", (nova_disponibilidade, id_livro))
        conn.commit()
        print(f"Disponibilidade atualizada para '{nova_disponibilidade}'!")
    else:
        print("Livro não encontrado.")

def remover_livro(id_livro):
    cursor.execute("DELETE FROM livros WHERE id = ?", (id_livro,))
    conn.commit()
    print("Livro removido com sucesso!")

def menu():
    while True:
        print("===== Menu =====")
        print("1. Cadastrar livro")
        print("2. Listar livros")
        print("3. Atualizar disponibilidade")
        print("4. Remover livro")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = input("Ano: ")
            cadastrar_livro(titulo, autor, ano)
        elif escolha == "2":
            listar_livros()
        elif escolha == "3":
            id_livro = input("ID do livro para atualizar: ")
            atualizar_disponibilidade(id_livro)
        elif escolha == "4":
            id_livro = input("ID do livro para remover: ")
            remover_livro(id_livro)
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
if __name__ == "__main__":
    menu()
    conn.close()