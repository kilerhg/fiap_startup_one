CREATE TABLE startfuture_backend.alunos (
	id serial primary key,
	nome varchar(70) NOT NULL,
	rm int4 NOT null unique,
	telefone varchar(12) NULL,
	email varchar(50) NOT null unique,
	cep varchar(8) not null
);

CREATE TABLE startfuture_backend.areas (
	id int4 primary key,
	nome varchar(30) not null
);

CREATE TABLE startfuture_backend.formulario (
	id serial primary key,
	nome varchar(70) NOT null,
	telefone varchar(12) NULL,
	email varchar(50) NOT null unique,
	cep varchar(8) not null,
	area_interesse int4 references areas(id)
);

CREATE TABLE startfuture_backend.bootcamps (
	id serial primary key,
	nome varchar(20) NOT NULL,
	data_inicio date not null,
	data_fim date not null
);

CREATE TABLE startfuture_backend.turma (
	id serial primary key,
	id_bootcamp int4 references bootcamps(id),
	id_aluno int4 references alunos(id),
	id_area int4 references areas(id)
);

CREATE TABLE startfuture_backend.certificados (
	id serial primary key,
	id_aluno int4 references alunos(id),
	id_bootcamp int4 references bootcamps(id)
);