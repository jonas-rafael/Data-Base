create table aluno(
    Id integer primary key not null,
    Nome text not null,
    Curso text not null,
    Matrícula int unique not null,
    Data_ingresso date not null

);



select * from aluno;