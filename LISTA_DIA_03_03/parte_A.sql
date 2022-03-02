CREATE TABLE contato(
    id INTEGER PRIMARY KEY NOT NULL,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    telefone INT NOT NULL,
    nascimento DATE NOT NULL
);

select * from contato