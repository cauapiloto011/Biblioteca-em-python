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