from typing import Optional # this Optional is complete up to you, just to make the code more readable.
from pydantic import BaseModel

class Student(BaseModel):
    name : str
    rm : int
    cellphone : Optional[str]
    email : str
    cep : int

class Departments(BaseModel):
    id : str
    name : str

class Bootcamp(BaseModel):
    name : str
    date_start : int
    date_end : str

class Certificate(BaseModel):
    id_student : int
    id_bootcamp : int

class Form(BaseModel):
    name : str
    cellphone : Optional[str]
    email : str
    cep : str
    area_interesse : int

class Classroom(BaseModel):
    id_bootcamp : int
    id_student : int
    id_area : int