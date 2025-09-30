#Deletando dados do banco
def deletar_aluno():
    try:
        conexao = sqlite3.connect("escola.db")
        cursor = conexao.cursor()
       
        id_aluno = int(input("Digite o id do aluno que deseja deletar: "))
        cursor.execute("DELETE FROM alunos WHERE id = ?", (id_aluno,))
        conexao.commit()
       
        #Verificar se o aluno foi realmente deletado
        if cursor.rowcount > 0:
            print("Aluno removido com sucesso!")
        else:
            print("Nenhum aluno cadastrado com o ID fornecido")
    except Exception as erro:
        print(f"Erro ao tentar excluir o aluno {erro}")
    finally:
        #Sempre fecha a conexão, com sucesso ou erro
        if conexao:
            conexao.close()

deletar_aluno()