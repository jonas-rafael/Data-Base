def ler_contato():
    nome= input("Digite o nome do contato: ")
    email= input("Digite o Email do contato: ")
    telefone=int(input("Digite o telefone do contato: "))
    nascimento=input("digite a data de nascimento (aa/bb/cccc)")
    return nome,email,telefone,nascimento

def imprimir(linha):
    print("ID:", linha[0])
    print("Nome:", linha[1])
    print("Curso:", linha[2])
    print("Matricula:", linha[3])
    print("Data_ingresso", linha[4])