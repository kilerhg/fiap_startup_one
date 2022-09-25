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