import sqlite3
Novo_Curso = input("Digite o novo curso de aluno: ")
Matrícula = int(input("Digite a matricula do aluno: "))



conexão = sqlite3.connect("bc_exemplo1.bd")

c = conexão.cursor()
try:
    c.execute("Update aluno set curso = ? where Matrícula = ?", (Novo_Curso,Matrícula))
    sucesso = c.rowcount == 1
except sqlite3.IntegrityError:
    sucesso=False

if sucesso:
    print("Aluno atualizado com sucesso!")
else:
    print("Não foi possível atualizar aluno, tente novamente!")



print("Linhas inseridas",c.rowcount)
conexão.commit()
c.close()
conexão.close()