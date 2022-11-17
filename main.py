from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()

class Student(BaseModel):
    id: str
    name: str
    lastname: str
    #skills: List[str] = []

students = []

@app.get("/estudiantes") # Busqueda de manera general.
def get_students():
    return students

@app.get("/estudiantes/{id}") #Busqueda indexada por id.
def get_student(id: str):
    for student in students:
        if student["id"] == id: 
            return student
    return "No existe el estudiante"

@app.post("/estudiantes") # Crea estudiante.
def save_student(student: Student):
    student.id = str(uuid4())
    students.append(student.dict())
    return "Estudiante registrado"

@app.put("/estudiantes/{id}") # Actualizar estudiante por id.
def update_student(updated_updated: Student, id:str):
    for student in students:
        if student["id"] == id:
            student["name"] = updated_updated.name
            student["lastname"] = updated_updated.lastname
            #student["skills"] = updated_updated.skills
            return "Estudiante modificado"
    return "No existe el estudiante"

@app.delete("/estudiantes/{id}") #Eliminar estudiante por id.
def delete_student(id: str):
    for student in students:
        if student["id"] == id:
            students.remove(student)
            return "Estudiante eliminado"
    return "No existe el estudiante"

"""@app.get ("/saludo")
async def root():
    return {"message": "Hola MisionTIC 2022"}

@app.get ("/usuarios/{user_id}")

async def read_user(user_id: int):

    return {"user_id": user_id}

cursos = [{"curso":"Fundamentos de Programación"}, {"curso":"Programación Básica"}, {"cursos":"Desarrollo de AppWeb"}, {"curso":"Desarollo Móvil Android"}]
@app.get ("/cursos/")
async def read_item(skip: int=0 , limit: int=10):
    return cursos[skip: skip+limit]"""