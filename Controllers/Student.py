from fastapi import APIRouter

from Dto.Input.Students.create_student_dto import create_student
from Dto.Input.Students.update_student_dto import update_student
from Dto.Input.Students.delete_student_dto import delete_student


from Services.Students.Create_Students import Create_Students
from Services.Students.View_students import View_students
from Services.Students.Update_Students import Update_students
from Services.Students.Delete_Students import Delete_Students

router = APIRouter()

@router.post("/create")
async def insert_new_student(dto: create_student):
    return await Create_Students.create_student(dto)

@router.get("/view")
async def view_students():
    return await View_students.view_students()

@router.put("/update")
async def read_root(dto: update_student):
    return await Update_students.update_student(dto)

@router.delete("/delete")
async def delete_students(dto: delete_student):
    return await Delete_Students.delete_student(dto)