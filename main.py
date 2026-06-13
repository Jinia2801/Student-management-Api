from fastapi import FastAPI
import json
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/about")
def read_about():
    return {"About": "This is a simple FastAPI application."}

def load_data():
    with open("students.json", "r") as file:
        data = json.load(file)
    return data

@app.get("/view")
def view():
    data = load_data()
    return data 

@app.get("/view/{student_id}")
def view_student(student_id: int):
    data = load_data()
    for student in data:
        if student["id"] == student_id:
            return student
    return {"error":"student not found"}