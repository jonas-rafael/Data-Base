import Funções_parte_B
import tratar_cliente

Funções_parte_B.cria_banco()


while True:
    print("0 - Sair do programa")
    print("1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Atualizar contato")
    print("4 - consulta contato")
    print("5 - Listar todos os contatos")
    opção = int(input("Escolha uma opção: "))


    if opção == 0 :
        break
    if opção ==1:
        nome,email,telefone,nascimento = tratar_cliente.ler_contato()
        if Funções_parte_B.adicionar_contato(nome,email,telefone,nascimento):
            print("Contato adicionado!")
        else:
            print("Não foi possível adicionar")
    elif opção ==2:
        email=input("Digite o email do contato que deseja excluir: ")
        if Funções_parte_B.remover_contato(email):
            print("email excluido com sucesso")
        else:
            print("O contato não foi encontrado!")


    elif opção ==3:
        email=input("Digite o email que pertence ao contato que deseja atualizar: ")
        novo_numero= input("Digite o novo numero do contato : ")
        if Funções_parte_B.atualizar_contato(novo_numero,email):
            print("Adicionado com sucesso!")
        else:
            print("não foi possivel adicionar")

    elif opção ==4:
        email=input("Digite o email do contato que deseja consultar: ")
        contato=Funções_parte_B.buscar_contato(email)

        if contato:
            print("#")
            tratar_cliente.imprimir(contato)

        else:
            print("Não a contato para mostrar!")
    elif opção == 5:
        tabela = Funções_parte_B.listar_todos()

        if tabela:
            for linha in tabela:
                print("#")
                tratar_cliente.imprimir(linha)

        else:
            print("Nenhum aluno cadastrado!")
    else:
        print("Opção inválida ")
