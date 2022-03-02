import sqlite3



conexão = sqlite3.connect("bc_exemplo1.bd")
c = conexão.cursor()

c.execute("select * from aluno")
tabela= c.fatchall()
if tabela:
    print("Listagem de Alunos Cadastro")
    for linhas in tabela:
        print("-"*20)
        print("ID:", linhas[0])
        print("Nome:", linhas[1])
        print("Curso:",linhas[2])
        print("Matricula:",linhas[3])
        print("Data_ingresso",linhas[4])

else:
    print("Nenhum Aluno cadastrado!")





c.close()
conexão.close()