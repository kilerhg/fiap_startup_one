from fastapi import FastAPI
from typing import Optional # this Optional is complete up to you, just to make the code more readable.
from models import request_body

import parameters
import manager
# uvicorn app:app --reload

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Index"}, 200

@app.get("/health")
def health():
    return {"message": "Aplication is healthy"}, 200

@app.get("/students/{id}")
def show_students(id: int):
    content, status_valid = manager.get_student_by_id(id)
    if status_valid:
        http_code = 200
    else:
        http_code = 400
    return {"message": "students", "content":content}, http_code

@app.post("/students")
def create_student(student: request_body.Student):
    status_valid = manager.create_student(student)
    if status_valid:
        return {"message": "Student created"}, 200
    else:
        return {"message": "Student cannot be created"}, 400

@app.put("/students/{id}")
def update_student(id: int, student: request_body.Student):
    status_valid = manager.update_student(id, student)
    if status_valid:
        return {"message": "Student created"}, 200
    else:
        return {"message": "Student cannot be created"}, 400

@app.get("/departments")
def show_all_departments():
    content, status_valid = manager.get_all_department()
    if status_valid:
        http_code = 200
    else:
        http_code = 400
    return {"message": "departments", "content": content}, http_code

@app.post("/departments")
def create_departments(department : request_body.Departments):
    status_valid = manager.create_department(department)
    if status_valid:
        return {"message": "Department created"}, 200
    else:
        return {"message": "Department cannot be created"}, 400

@app.get("/bootcamps")
def bootcamps():
    content, status_valid = manager.get_all_bootcamp()
    if status_valid:
        http_code = 200
    else:
        http_code = 400
    return {"message": "Bootcamp", "content": content}, http_code

@app.post("/bootcamps")
def create_bootcamps(bootcamp : request_body.Bootcamp):
    status_valid = manager.create_bootcamp(bootcamp)
    if status_valid:
        return {"message": "Bootcamp created"}, 200
    else:
        return {"message": "Bootcamp cannot be created"}, 400

@app.get("/certificates")
def get_certificates_user():
    content, status_valid = manager.get_all_certificates()
    if status_valid:
        http_code = 200
    else:
        http_code = 400
    return {"message": "Certificate", "content": content}, http_code

@app.post("/certificates")
def create_certificates(certificates : request_body.Certificate):
    status_valid = manager.create_certificates(certificates)
    if status_valid:
        return {"message": "Certificate created"}, 200
    else:
        return {"message": "Certificate cannot be created"}, 400

@app.get("/forms")
def get_all_forms():
    content, status_valid = manager.get_all_forms()
    if status_valid:
        http_code = 200
    else:
        http_code = 400
    return {"message": "Forms", "content": content}, http_code

@app.post("/forms")
def insert_data_form(form : request_body.Form):
    status_valid = manager.create_forms(form)
    if status_valid:
        return {"message": "Forms created"}, 200
    else:
        return {"message": "Forms cannot be created"}, 400

@app.get("/classroom")
def show_classroom():
    content, status_valid = manager.get_all_classroom()
    if status_valid:
        http_code = 200
    else:
        http_code = 400
    return {"message": "Classroom", "content": content}, http_code

@app.post("/classroom")
def create_classroom(classroom : request_body.Classroom):
    status_valid = manager.create_classroom(classroom)
    if status_valid:
        return {"message": "Classroom created"}, 200
    else:
        return {"message": "Classroom cannot be created"}, 400