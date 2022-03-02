import sqlite3
Matrícula = int(input("Digite a matricula do aluno: "))



conexão = sqlite3.connect("bc_exemplo1.bd")

c = conexão.cursor()
try:
    c.execute("delete from aluno where Matrícula = ?", (Matrícula,))
    sucesso = c.rowcount == 1
except sqlite3.IntegrityError:
    sucesso=False

if sucesso:
    print("Aluno removido com sucesso!")
else:
    print("Não foi possível remover aluno, tente novamente!")



print("Linhas inseridas",c.rowcount)
conexão.commit()
c.close()
conexão.close()