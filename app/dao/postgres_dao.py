import logging

import psycopg2

from app import parameters
from app import models

class ConnectDB:

    def __init__(hostname, username, port, password):
        self.hostname = hostname 
        self.username = username 
        self.port = port 
        self.password = password

    def __enter__(self):
        self.db = psycopg2.connect(
            hostname=self.hostname,
            username=self.username,
            password=self.password,
            port=self.port
        )
        self.cursor = self.db.cursor()

    def __exit__(self):
        try:
            self.db.commit()
            self.db.close()
        except Exception.error as erro:
            logging.error(f'Database error: {erro}')

# class StudentDAO:
def create_student(student : models.Student):
    print(student)