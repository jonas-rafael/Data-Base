CREATE TABLE medico (
id INTEGER PRIMARY KEY NOT NULL,
nome TEXT NOT NULL,
rg INTEGER NOT NULL UNIQUE,
idade INTEGER NOT NULL,
salario REAL NOT NULL,
especialidade TEXT NOT NULL,
data_contrato DATE
);


INSERT INTO medico (nome, rg, idade, salario, especialidade) VALUES ('Natasha', 12200, 41, 1200, 'Cardiologia');
INSERT INTO medico (nome, rg, idade, salario, especialidade) VALUES ('Otávio', 12300, 23, 1400, 'Oftalmologia');
INSERT INTO medico (nome, rg, idade, salario, especialidade) VALUES ('Pedro', 12347, 22, 1150, 'Ortopedia');
INSERT INTO medico (nome, rg, idade, salario, especialidade, data_contrato)
VALUES ('Paulo', 1200, 42, 10000, 'Cardiologia', '2012-01-31');
INSERT INTO medico (nome, rg, idade, salario, especialidade, data_contrato)
VALUES ('Anna', 3234, 24, 11222, 'Cardiologia', '2012-01-17');
INSERT INTO medico (nome, rg, idade, salario, especialidade, data_contrato)
VALUES ('Arthur', 32234, 22, 8000, 'Ortopedia', '2012-12-15');
INSERT INTO medico (nome, rg, idade, salario, especialidade, data_contrato)
VALUES ('Felipe', 12122, 25, 19800, 'Dermatologia', '2012-12-31');
INSERT INTO medico (nome, rg, idade, salario, especialidade, data_contrato)
VALUES ('Gustavo', 51421, 45, 1400, 'Oftalmologia', '2012-05-05');
INSERT INTO medico (nome, rg, idade, salario, especialidade, data_contrato)
VALUES ('Pedro', 323200, 40, 5000, 'Neurologia', '2012-03-23');
INSERT INTO medico (nome, rg, idade, salario, especialidade, data_contrato)
VALUES ('Alan', 12034, 38, 19700, 'Neurologia', '2012-07-29');
INSERT INTO medico (nome, rg, idade, salario, especialidade, data_contrato)
VALUES ('Henrique', 32034, 39, 18000, 'Mastologia', '2012-09-10');
INSERT INTO medico (nome, rg, idade, salario, especialidade, data_contrato)
VALUES ('Daniela', 32340, 28, 8500, 'Ortopedia', '2012-09-11');

--exemplos de consulta
select * from medico;
select * from medico where medico idade > 26;
select rg,nome,data_contrato from medico;
select rg,nome,data_contrato from medico where idade >26 and salario >= 10000;
select distinct especialidade from medico;

-- consulta de 90%
select rg, salario, salario * 0.9    from medico;
-- consulta da quantidade completa de intens na lista
select count(*) from medico
select count(data_contrato) from medico;
select * from medico where especialidade = 'Cardiologia';
select count(*) from medico where especialidade = 'Cardiologia';

-- usando SUN
select * from medico;
select sun(salario) from medico;
select sun(salario) from medico  where especialidade = 'Cardiologia' and data_contrato is not null;

-- Usando avg = média
select avg(idade) from medico;
select avg(salario) from medico where especialidade = 'Cardiologia'
 -- Usando min e max
select max(salario), min(salario) where especialidade= 'Cardiologia'
-- Usando between
select * from medico where data_nascimento >= '2012-12-01' and data_nasscimento <= '2012-12-31';
select * from  medico where data_nascimento between '2012-12-01' and '2012-12-31';
select * from medico where data_nascimento not between '2012-12-01' and '2012-12-31';
select * from medico where idade between 25 and 45;
--Usando o in
select * from medico where especialidade in ('Ortopedia','Oftalmologia','Cardiologia')
select * from medico where especialidade not in ('Ortopedia','Oftalmologia','Cardiologia')
-- where atributo like 'padrão'
-- %: casa com qualquer cadeia de caracteres
--_: casa com exatamente um caractere

select * from medico where nome like 'p';
select * from medico where nome like '_2%00';

--Usando order by
-- asc prq acendente e desc para decrecente
select* from medico order by nome;
select * from medico where especialidade - 'Cardiologia' order by salario desc;
select * from medico order by especialidade,nome;

--Usando limit
select * from medico limit 4;
select * from medico;