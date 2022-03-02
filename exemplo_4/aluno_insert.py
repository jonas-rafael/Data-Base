import sqlite3
Nome= input("Digite o nome do aluno: ")
Curso = input("Digite o curso de aluno: ")
Matrícula = int(input("Digite a matricula do aluno: "))
Data_ingresso = input("Digite a data de ingresso do aluno: ")



conexão = sqlite3.connect("bc_exemplo1.bd")

c = conexão.cursor()
try:
    c.execute("insert into aluno (Nome,Curso,Matrícula,Data_ingresso) values (?,?,?,?)",
             (Nome, Curso, Matrícula, Data_ingresso))
    sucesso = c.rowcount == 1
except sqlite3.IntegrityError:
    sucesso=False

if sucesso:
    print("Aluno adicionado com sucesso!")
else:
    print("Não foi possível adicionar aluno, tente novamente!")



print("Linhas inseridas",c.rowcount)
conexão.commit()
c.close()
conexão.close()