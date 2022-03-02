import sqlite3
Matrícula = int(input("Digite a matricula do aluno: "))



conexão = sqlite3.connect("bc_exemplo1.bd")

c = conexão.cursor()

c.execute("Update aluno set curso = ? where Matrícula = ?", (Matrícula,))
linhas=c.fatchone()

if linhas:
    print("ID:", linhas[0])
    print("Nome:", linhas[1])
    print("Curso:",linhas[2])
    print("Matricula:",linhas[3])
    print("Data_ingresso",linhas[4])

else:
    print("Matricula não encontrada!")




conexão.commit()
c.close()
conexão.close()