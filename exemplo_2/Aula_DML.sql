create table pessoa (
    id integer primary key not null,
    cpf text not null unique,
    rg integer not null unique,
    nome text not null,
    data_nascimento date
);

select * from pessoa;

insert into pessoa (id,cpf,rg,nome,data_nascimento) values (1,'11111111111',11111,'jonas', '1995/12/01')

-- Exemplos de atualização de registros
update pessoa set data_nascimento = '2010-21-24'  where id =1;