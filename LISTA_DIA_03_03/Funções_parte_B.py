import sqlite3

arquivoBD="banco.bd"
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

def adicionar_contato(nome,email,telefone,nascimento):
    with sqlite3.connect(arquivoBD) as conexão:
        c = conexão.cursor()
        try:
            c.execute("insert into contato(nome,email,telefone,nascimento) values (?,?,?,?)",
                      (nome,email,telefone,nascimento))
            conexão.commit()
            sucesso=c.rowcount ==1
        except sqlite3.IntegrityError:
            sucesso=False
        return sucesso

def remover_contato(email):
    with sqlite3.connect(arquivoBD) as conexão:
        c = conexão.cursor()
        try:
            c.execute("delete from aluno where email=?",(email,))
            sucesso = c.rowcount == 1
            c.commit()
        except sqlite3.IntegrityError:
            sucesso = False
        return sucesso

def atualizar_contato(novo_numero,email):
    with sqlite3.connect(arquivoBD) as conexão:
        c = conexão.cursor()
        try:
            c.execute("update contato set telefone = ? where email = ?",(novo_numero,email))
            conexão.commit()
            sucesso = c.rowcount ==1
        except sqlite3.IntegrityError:
            sucesso = False
        return sucesso


def buscar_contato(email):
    with sqlite3.connect(arquivoBD) as conexão:
        c = conexão.cursor()
        c.execute("select * from contato where email = ?", (email,))
        linha = c.fetchone()

    return linha


def listar_todos():
    with sqlite3.connect(arquivoBD) as conexão:
        c = conexão.cursor()
        c.execute("select *  from contato")
        tabela = c.fatchall()
    return tabela

