from fastapi import FastAPI
from typing import Optional # this Optional is complete up to you, just to make the code more readable.
from models import request_body

import parameters
# uvicorn app:app --reload

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Index"}, 200

@app.get("/health")
def health():
    return {"message": "Aplication is healthy"}, 200

@app.get("/students")
def show_students():
    return {"message": "students"}, 200

@app.post("/students")
def create_student(student: request_body.Student):
    return {"message": "students"}, 200

@app.get("/departments")
def show_departments():
    return {"message": "departments"}, 200

@app.post("/departments")
def create_departments(departments : request_body.Departments):
    return {"message": "departments"}, 200

@app.get("/bootcamps")
def bootcamps():
    return {"message": "bootcamps"}, 200

@app.post("/bootcamps")
def create_bootcamps(bootcamp : request_body.Bootcamp):
    return {"message": "bootcamps"}, 200

@app.get("/certificates")
def get_certificates_user():
    return {"message": "certificates"}, 200

@app.post("/certificates")
def create_certificates(certificates : request_body.Certificate):
    return {"message": "certificates"}, 200

@app.get("/forms")
def forms():
    return {"message": "forms"}, 200

@app.post("/forms")
def insert_data_form(forms : request_body.Form):
    return {"message": "forms"}, 200

@app.get("/classroom")
def show_classroom():
    return {"message": "classroom"}, 200

@app.post("/classroom")
def create_classroom(classroom : request_body.Classroom):
    return {"message": "classroom"}, 200