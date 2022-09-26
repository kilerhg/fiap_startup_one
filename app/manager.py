import parameters
from models import request_body, postgres_dao

def create_student(student : request_body.Student):
    status_valid = postgres_dao.StudentDAO.create_student_db(student)
    return status_valid

def get_student_by_id(id):
    content, status_valid = postgres_dao.StudentDAO.get_student_by_id(id)
    return content, status_valid

def update_student(id : int, student : request_body.Student):
    status_valid = postgres_dao.StudentDAO.update_student_db(id, student)
    return status_valid

###

def create_department(department : request_body.Departments):
    status_valid = postgres_dao.DepartmentDAO.create_department_db(department)
    return status_valid

def get_all_department():
    content, status_valid = postgres_dao.DepartmentDAO.get_all_department()
    return content, status_valid

###

def create_bootcamp(bootcamp : request_body.Bootcamp):
    status_valid = postgres_dao.BootcampDAO.create_bootcamp_db(bootcamp)
    return status_valid

def get_all_bootcamp():
    content, status_valid = postgres_dao.BootcampDAO.get_all_bootcamp()
    return content, status_valid

###

def create_certificates(certificate : request_body.Certificate):
    status_valid = postgres_dao.CertificateDAO.create_certificate(certificate)
    return status_valid

def get_all_certificates():
    content, status_valid = postgres_dao.CertificateDAO.get_all_certificate()
    return content, status_valid

###

def create_forms(form : request_body.Form):
    status_valid = postgres_dao.FormDAO.create_form(form)
    return status_valid

def get_all_forms():
    content, status_valid = postgres_dao.FormDAO.get_all_form()
    return content, status_valid

###

def create_classroom(classroom : request_body.Classroom):
    status_valid = postgres_dao.ClassroomDAO.create_classroom(classroom)
    return status_valid

def get_all_classroom():
    content, status_valid = postgres_dao.ClassroomDAO.get_all_classroom()
    return content, status_valid