import logging

import psycopg2
import psycopg2.extras

import parameters
from models import request_body

class ConnectDB:

    def __init__(self, hostname, username, port, password, db, schema):
        self.hostname = hostname 
        self.username = username 
        self.port = port 
        self.password = password
        self.db = db
        self.schema = schema

    def __enter__(self):
        try:
            self.db = psycopg2.connect(
                host=self.hostname,
                user=self.username,
                password=self.password,
                port=self.port,
                dbname=self.db
            )
            self.cursor = self.db.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            self.cursor.execute(f"set schema '{self.schema}'")
        except Exception as erro:
            logging.error(f"Error database can't connect: {erro}")
        else:
            return self.cursor

    def __exit__(self, *args):
        try:
            self.db.commit()
            self.db.close()
        except Exception as erro:
            logging.error(f'Database error: {erro}')
        else:
            return self.cursor

class StudentDAO:
    def create_student_db(student : request_body.Student):
        with ConnectDB(db=parameters.DB_NAME, schema=parameters.DB_SCHEMA, hostname=parameters.DB_HOST, username=parameters.DB_USERNAME, port=parameters.DB_PORT, password=parameters.DB_PASSWORD) as cursor:
            try:
                query = f'''
                        insert into alunos(nome, rm, telefone, email, cep)
                        values ('{student.name}', '{student.rm}', '{student.cellphone}', '{student.email}', '{student.cep}')
                        ;'''
                cursor.execute(query)
            except Exception as erro:
                status_valid = False
                print(erro)
                logging.debug(f'Database error - query: {erro}')
            else:
                status_valid = True
        return status_valid

    def get_student_by_id(id : int):
        with ConnectDB(db=parameters.DB_NAME, schema=parameters.DB_SCHEMA, hostname=parameters.DB_HOST, username=parameters.DB_USERNAME, port=parameters.DB_PORT, password=parameters.DB_PASSWORD) as cursor:
            try:
                query = f'''
                        select nome, rm, telefone, email, cep from alunos
                        where id = '{id}'
                        ;'''
                cursor.execute(query)
                content = cursor.fetchone()
            except Exception as erro:
                status_valid = False
                content = None
                logging.debug(f'Database error - query: {erro}')
            else:
                status_valid = True
        return content, status_valid
    
    def update_student_db(id : int, student : request_body.Student):
        with ConnectDB(db=parameters.DB_NAME, schema=parameters.DB_SCHEMA, hostname=parameters.DB_HOST, username=parameters.DB_USERNAME, port=parameters.DB_PORT, password=parameters.DB_PASSWORD) as cursor:
            try:
                query = f'''
                        update alunos
                        set nome = '{student.name}',
                        rm = '{student.rm}',
                        telefone = '{student.cellphone}',
                        email = '{student.email}',
                        cep = '{student.cep}'
                        where id = {id};
                        ;'''
                cursor.execute(query)
            except Exception as erro:
                status_valid = False
                print(erro)
                logging.debug(f'Database error - query: {erro}')
            else:
                status_valid = True
        return status_valid

class DepartmentDAO:
    def create_department_db(department : request_body.Departments):
        with ConnectDB(db=parameters.DB_NAME, schema=parameters.DB_SCHEMA, hostname=parameters.DB_HOST, username=parameters.DB_USERNAME, port=parameters.DB_PORT, password=parameters.DB_PASSWORD) as cursor:
            try:
                query = f'''
                        insert into areas(id, nome)
                        values ('{department.id}', '{department.name}')
                        ;'''
                cursor.execute(query)
            except Exception as erro:
                status_valid = False
                print(erro)
                logging.debug(f'Database error - query: {erro}')
            else:
                status_valid = True
        return status_valid

    def get_all_department():
        with ConnectDB(db=parameters.DB_NAME, schema=parameters.DB_SCHEMA, hostname=parameters.DB_HOST, username=parameters.DB_USERNAME, port=parameters.DB_PORT, password=parameters.DB_PASSWORD) as cursor:
            try:
                query = f'''
                        select nome from areas
                        ;'''
                cursor.execute(query)
                content = cursor.fetchall()
            except Exception as erro:
                status_valid = False
                content = None
                logging.debug(f'Database error - query: {erro}')
            else:
                status_valid = True
        return content, status_valid

class BootcampDAO:
    def create_bootcamp_db(bootcamp : request_body.Bootcamp):
        with ConnectDB(db=parameters.DB_NAME, schema=parameters.DB_SCHEMA, hostname=parameters.DB_HOST, username=parameters.DB_USERNAME, port=parameters.DB_PORT, password=parameters.DB_PASSWORD) as cursor:
            try:
                query = f'''
                        insert into bootcamps(nome, data_inicio, data_fim)
                        values ('{bootcamp.name}', '{bootcamp.date_start}', '{bootcamp.date_end}')
                        ;'''
                cursor.execute(query)
            except Exception as erro:
                status_valid = False
                print(erro)
                logging.debug(f'Database error - query: {erro}')
            else:
                status_valid = True
        return status_valid

    def get_all_bootcamp():
        with ConnectDB(db=parameters.DB_NAME, schema=parameters.DB_SCHEMA, hostname=parameters.DB_HOST, username=parameters.DB_USERNAME, port=parameters.DB_PORT, password=parameters.DB_PASSWORD) as cursor:
            try:
                query = f'''
                        select nome, data_inicio, data_fim from bootcamps
                        ;'''
                cursor.execute(query)
                content = cursor.fetchall()
            except Exception as erro:
                status_valid = False
                content = None
                logging.debug(f'Database error - query: {erro}')
            else:
                status_valid = True
        return content, status_valid

class CertificateDAO:
    def create_certificate(certificate : request_body.Certificate):
        with ConnectDB(db=parameters.DB_NAME, schema=parameters.DB_SCHEMA, hostname=parameters.DB_HOST, username=parameters.DB_USERNAME, port=parameters.DB_PORT, password=parameters.DB_PASSWORD) as cursor:
            try:
                query = f'''
                        insert into certificados(id_aluno, id_bootcamp)
                        values ('{certificate.id_student}', '{certificate.id_bootcamp}')
                        ;'''
                cursor.execute(query)
            except Exception as erro:
                status_valid = False
                print(erro)
                logging.debug(f'Database error - query: {erro}')
            else:
                status_valid = True
        return status_valid
 
    def get_all_certificate():
        with ConnectDB(db=parameters.DB_NAME, schema=parameters.DB_SCHEMA, hostname=parameters.DB_HOST, username=parameters.DB_USERNAME, port=parameters.DB_PORT, password=parameters.DB_PASSWORD) as cursor:
            try:
                query = f'''
                        select id_aluno, id_bootcamp from certificados
                        ;'''
                cursor.execute(query)
                content = cursor.fetchall()
            except Exception as erro:
                status_valid = False
                content = None
                logging.debug(f'Database error - query: {erro}')
            else:
                status_valid = True
        return content, status_valid

class FormDAO:
    def create_form(form : request_body.Form):
        with ConnectDB(db=parameters.DB_NAME, schema=parameters.DB_SCHEMA, hostname=parameters.DB_HOST, username=parameters.DB_USERNAME, port=parameters.DB_PORT, password=parameters.DB_PASSWORD) as cursor:
            try:
                query = f'''
                        insert into formulario(nome, telefone, email, cep, area_interesse)
                        values ('{form.name}', '{form.cellphone}', '{form.email}', '{form.cep}', '{form.interested_deparment}')
                        ;'''
                cursor.execute(query)
            except Exception as erro:
                status_valid = False
                print(erro)
                logging.debug(f'Database error - query: {erro}')
            else:
                status_valid = True
        return status_valid
 
    def get_all_form():
        with ConnectDB(db=parameters.DB_NAME, schema=parameters.DB_SCHEMA, hostname=parameters.DB_HOST, username=parameters.DB_USERNAME, port=parameters.DB_PORT, password=parameters.DB_PASSWORD) as cursor:
            try:
                query = f'''
                        select nome, telefone, email, cep, area_interesse from formulario
                        ;'''
                cursor.execute(query)
                content = cursor.fetchall()
            except Exception as erro:
                status_valid = False
                content = None
                logging.debug(f'Database error - query: {erro}')
            else:
                status_valid = True
        return content, status_valid

class ClassroomDAO:
    def create_classroom(classrom : request_body.Classroom):
        with ConnectDB(db=parameters.DB_NAME, schema=parameters.DB_SCHEMA, hostname=parameters.DB_HOST, username=parameters.DB_USERNAME, port=parameters.DB_PORT, password=parameters.DB_PASSWORD) as cursor:
            try:
                query = f'''
                        insert into turma(id_bootcamp, id_aluno, id_area)
                        values ('{classrom.id_bootcamp}', '{classrom.id_student}', '{classrom.id_department}')
                        ;'''
                cursor.execute(query)
            except Exception as erro:
                status_valid = False
                print(erro)
                logging.debug(f'Database error - query: {erro}')
            else:
                status_valid = True
        return status_valid
 
    def get_all_classroom():
        with ConnectDB(db=parameters.DB_NAME, schema=parameters.DB_SCHEMA, hostname=parameters.DB_HOST, username=parameters.DB_USERNAME, port=parameters.DB_PORT, password=parameters.DB_PASSWORD) as cursor:
            try:
                query = f'''
                        select id_bootcamp, id_aluno, id_area from turma
                        ;'''
                cursor.execute(query)
                content = cursor.fetchall()
            except Exception as erro:
                status_valid = False
                content = None
                logging.debug(f'Database error - query: {erro}')
            else:
                status_valid = True
        return content, status_valid