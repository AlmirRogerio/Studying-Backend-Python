from fastapi import APIRouter

from Dto.Input.Courses.create_course_dto import createCourse
from Dto.Input.Courses.update_course_dto import updateCourse
from Dto.Input.Courses.delete_course_dto import deleteCourse

from Services.Courses.Create_courses import Create_courses
from Services.Courses.View_courses import View_courses
from Services.Courses.Update_courses import update_courses
from Services.Courses.delete_courses import delete_courses

router = APIRouter()

@router.post("/create")
async def insert_new_course(dto: createCourse):
    return await Create_courses.Create_course(dto)

@router.get("/view")
async def view_courses():
    return await View_courses.view_courses()

@router.put("/update")
async def read_root(dto: updateCourse):
    return await update_courses.update_course(dto)

@router.delete("/delete")
async def read_root(dto: deleteCourse):
    return await delete_courses.delete_course(dto)
