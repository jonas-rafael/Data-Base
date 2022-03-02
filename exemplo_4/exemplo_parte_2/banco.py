import sqlite3

arquivo_banco = "exemplo_2.db"
def cria_banco():
    with sqlite3.connect(arquivo_banco) as conexão:
        conexão.execute("""CREATE TABLE contato(
    id INTEGER PRIMARY KEY NOT NULL,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    telefone INT NOT NULL,
    nascimento DATE NOT NULL
)""")

def Adicionar(Nome, Curso, Matrícula, Data_ingresso):
    try:
        with sqlite3.connect(arquivo_banco) as conexão:

            cursor = conexão.execute("insert into aluno (Nome,Curso,Matrícula,Data_ingresso) values (?,?,?,?)",
                      (Nome, Curso, Matrícula, Data_ingresso))
            sucesso = cursor.rowcount == 1

    except sqlite3.IntegrityError:
        sucesso = False

    return sucesso


def atualizar(Novo_Curso, Matrícula):
    try:
        with sqlite3.connect(arquivo_banco) as conexão:
            cursor = conexão.execute("Update aluno set curso = ? where Matrícula = ?", (Novo_Curso, Matrícula))
            sucesso = cursor.rowcount == 1
    except sqlite3.Error:
        sucesso = False
    return sucesso



def delete(Matrícula):
    try:
        with sqlite3.connect(arquivo_banco) as conexão:

            cursor = conexão.execute("delete from aluno where Matrícula = ?", (Matrícula,))
            sucesso = cursor.rowcount == 1

    except sqlite3.IntegrityError:
            sucesso = False
    return sucesso

def buscar_matricula(Matrícula):
    with sqlite3.connect(arquivo_banco) as conexão, conexão.cursor() as c:

        c.execute("select * from aluno where = ?", (Matrícula,))
        linhas = c.fatchone()

    return linhas

def listar():
    with sqlite3.connect(arquivo_banco) as conexão, conexão.cursor() as c:
        c.execute("select * from aluno")
        tabela = c.fatchall()
    return tabela

