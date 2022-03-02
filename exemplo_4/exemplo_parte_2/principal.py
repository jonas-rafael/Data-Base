import banco
import tratar_cliente


while True:
    print("-"*40)
    print("0 - Sair do programa")
    print("1 - Adicionar aluno")
    print("2 - atualizar aluno")
    print("3 - Remover aluno")
    print("4 - Busca aluno por matricula")
    print("5 - Lista alunos")
    opção = int(input("Escolha uma opção: "))


    if opção ==0:
        print("Saindo fo programa...")
    elif opção == 1:
        Nome, Curso,Matrícula ,Data_ingresso = tratar_cliente.ler()
        if banco.Adicionar(Nome, Curso,Matrícula ,Data_ingresso):
            print("Aluno adicionado")
        else:
            print("Não foi possivcel adicionar")