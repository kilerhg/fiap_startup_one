insert into alunos(nome, rm, telefone, email, cep) values ('teste', '123456789', '23456789', 'teste@gmail.com', '12345612');
insert into areas(id, nome) values (1, 'teste');
insert into bootcamps(nome, data_inicio, data_fim) values ('workstation', '2022-01-01', '2022-02-01');
insert into certificados(id_aluno, id_bootcamp) values (1, 1);
insert into formulario(nome, telefone, email, cep, area_interesse) values ('lucas', '123456789', 'teste@gmail.com', '12345612', 1);
insert into turma(id_bootcamp, id_aluno, id_area) values (1, 1, 1);