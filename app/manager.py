import parameters
from models import request_body, postgres_dao

def create_student(student : request_body.Student):
    status_valid = postgres_dao.StudentDAO.create_student_db(student)
    return status_valid

def get_user_by_id(id):
    content, status_valid = postgres_dao.StudentDAO.get_student_by_id(id)
    return content, status_valid
