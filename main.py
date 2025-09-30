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
