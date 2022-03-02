create table produtos(
ID integer primary key not null,
NOME text not null,
VAlOR float not null,
QUANTIDADE int not null,
MEDIDA text not null);

select * from produtos

insert into produtos (NOME,VALOR,QUANTIDADE,MEDIDA) values ('Arroz',1.90,33,'Kg');
insert into produtos (NOME,VALOR,QUANTIDADE,MEDIDA) values ('Feijão',3.85,82,'Kg');
insert into produtos (NOME,VALOR,QUANTIDADE,MEDIDA) values ('Miojo',1.20,22,'Unidade');
insert into produtos (NOME,VALOR,QUANTIDADE,MEDIDA) values ('Tomate',3.05,128,'Kg');
insert into produtos (NOME,VALOR,QUANTIDADE,MEDIDA) values ('Cenoura',2.50,173,'Kg');
insert into produtos (NOME,VALOR,QUANTIDADE,MEDIDA) values ('Batata',2.38,74,'Kg');
insert into produtos (NOME,VALOR,QUANTIDADE,MEDIDA) values ('Pão',10.25,570,'G');
insert into produtos (NOME,VALOR,QUANTIDADE,MEDIDA) values ('Queijo',12.50,120,'Kg');
insert into produtos (NOME,VALOR,QUANTIDADE,MEDIDA) values ('Água',2.21,88,'L');

select * from produtos
--2
select * from produtos order by VALOR desc limit 4;
----------------------------------------------------
--3
select * from produtos order by VALOR limit 4;
----------------------------------------------------
--4
select * from produtos where MEDIDA like 'G';
----------------------------------------------------
--5
select * from produtos where VALOR like '2%5';
----------------------------------------------------
--6
select avg (VALOR) as média from produtos;
----------------------------------------------------
--7
select avg(VALOR) as média from produtos where MEDIDA  = 'Kg';
----------------------------------------------------
--8
select count (*) as contagem from produtos;
----------------------------------------------------
--9
select sum(VALOR) from produtos where MEDIDA = 'Kg';
