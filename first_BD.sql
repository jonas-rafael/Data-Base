create table clinica (
    numero integer primary key not null,
    nome text not null
);
-- lembrar de startar as tables
create table medico (
    crm integer primary key not null,
    nome text not null,
    especialidade text not null,
    cpf text not null unique,
    num_clinica integer not null,
    foreign key(num_clinica) references clinica(numero)
)


-- int pra não auto incrementar, integer primary key para auto incrementar






create table pessoa (
    cpf TEXT PRIMARY KEY NOT NULL,
    titulo_eleitor integer not null unique,
    nome text not null,
    cidade text not null);

create table livro (
id integer primary key not null,
título text not null,
numero_paginas integer not null,
nome_autor text not null
);


