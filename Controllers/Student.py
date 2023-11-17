from fastapi import APIRouter

from Dto.Input.Students.create_student_dto import create_student

from Services.Students.Create_Students import Create_Students
from Services.Students.View_students import View_students

router = APIRouter()

@router.post("/create")
async def insert_new_student(dto: create_student):
    return await Create_Students.create_student(dto)

@router.get("/view")
async def view_students():
    return await View_students.view_students()

@router.post("/update")
def read_root():
    return {'client': "teste"}

@router.post("/delete")
def read_root():
    return {'client': "teste"}