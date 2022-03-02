create table clinica (
    numero integer primary key not null,
    nome text not null unique
);

select * from clinica

insert into clinica (numero,nome) values (1,'Miguel')

create table medico (
    crm int primary key not null,
    nome text not null,
    especialidade text not null,
    cpf text not null unique,
    num_clinica integer not null,
    foreign key(num_clinica) references  clinica (numero)

);
select * from medico

insert into medico (crm,nome,especialidade,cpf) values (12134,'miguel','neurologia', '12354676512')

create table Conta (
    id integer primary key not null,
    número integer not null unique,
    agência integer not null unique,
    saldo integer not null,
    CRM integer not null,
    foreign key (CRM) references medico (crm)


);

select * from conta

insert into conta(número,agência,saldo) values (123123,0001,10)

