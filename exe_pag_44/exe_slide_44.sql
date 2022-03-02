create table produto (
  id integer primary key not null,
  nome text  not null,
  valor float ,
  quantidade int ,
  medida text not null

);

select * from produto

insert into produto (id,nome,valor,quantidade,medida) values (1,'Arroz',1.90,33,'Kg')
insert into produto (id,nome,valor,quantidade,medida) values (2,'Feijão',1.90,82,'Kg')
insert into produto (id,nome,valor,quantidade,medida) values (3,'Miojo',1.20,22,'Unidade')
insert into produto (id,nome,valor,quantidade,medida) values (4,'Tomate',3.05,128,'Kg')
insert into produto (id,nome,valor,quantidade,medida) values (5,'Cenoura',2.50,173,'Kg')
insert into produto (id,nome,valor,quantidade,medida) values (6,'Batata',2.38,74,'Kg')
insert into produto (id,nome,valor,quantidade,medida) values (7,'Pão',10.25,570,'g')
insert into produto (id,nome,valor,quantidade,medida) values (8,'Queijo',12.50,120,'Kg')
insert into produto (id,nome,valor,quantidade,medida) values (9,'Água',2.21,88,'l')

select * from produto
update produto set medida = '100' where id =1
update produto set medida = '100' where id =2
update produto set medida = '100' where id =4
update produto set medida = '100' where id =5
update produto set medida = '100' where id =6
update produto set medida = '100' where id =8
select * from produto
delete from produto where valor = 1.90,1.20
delete from produto where quantidade =33
delete from produto where quantidade = 82
delete from produto where quantidade = 22
delete from produto where quantidade = 74
delete from produto where quantidade =88
select * from produto

update produto set valor = 6.10 where id=4
 update produto set valor = 5 where id=5
 update produto set valor = 20.50 where id=7
 update produto set valor = 24.10 where id=8
 select * from produto
