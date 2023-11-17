from fastapi import FastAPI, Response, status
from fastapi.responses import JSONResponse
from models.models import Course

from Dto.Output.Courses.created_course_dto import createdCourse
from Dto.Output.Courses.update_course_dto import editedCourse
from Dto.Output.Courses.deleted_course_dto import deletedCourse

class Course_repository():
    
    async def insert_new_course(dto) -> createdCourse:
        try:
            new_course = Course(name=dto.name)
            await new_course.save()
            return createdCourse(course_name = dto.name, created = True)
        except:
            return createdCourse(course_name = dto.name, created = False)
    
    async def view_courses():
        return await Course.all()

    async def update_course(dto) -> editedCourse:
        try:
            await Course.filter(id=dto.course_id).update(name = dto.name)
            
            return editedCourse(course_name = dto.name, edited = True)
        except:
            return editedCourse(course_name = dto.name, edited = False)
    
    async def delete_course(dto) -> deletedCourse:
        try:
            await Course.filter(id=dto.course_id).delete()
            
            return deletedCourse(course_id=dto.course_id, deleted = True)
        except:
            return deletedCourse(course_id=dto.course_id, deleted = False)
            