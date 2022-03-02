def ler_aluno():
    Nome = input("Digite o nome do aluno: ")
    Curso = input("Digite o curso de aluno: ")
    Matrícula = int(input("Digite a matricula do aluno: "))
    Data_ingresso = input("Digite a data de ingresso do aluno: ")
    return Nome, Curso,Matrícula ,Data_ingresso



def imprimir(lista):
    print("ID:", lista[0])
    print("Nome:", lista[1])
    print("Curso:", lista[2])
    print("Matricula:", lista[3])
    print("Data_ingresso", lista[4])