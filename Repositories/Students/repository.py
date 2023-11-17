from fastapi import FastAPI, Response, status
from fastapi.responses import JSONResponse
from models.models import Student
from models.models import Course

from Dto.Output.Students.created_student_dto import created_student
from Dto.Output.Students.view_student_dto import view_student, view_student_error
from Dto.Output.Students.deleted_student_dto import deleted_student

class student_repository():
    
    async def create_student(dto) -> created_student:
        try:
            new_student = Student(name=dto.name , email=dto.email , course_id=dto.course_id)
            await new_student.save()
            
            return created_student(name=dto.name, created=True)
        except:
            return created_student(name=dto.name, created=False)
    
    async def view_students() -> view_student:
        try:
            response = []
            students = await Student.all()
            
            for student in students:
                student.course_id = await Course.filter(id=student.course_id).values("name")
                response.append(view_student(student_id=student.id,name = student.name, email = student.email, course=student.course_id[0]["name"]))
                                    
            return response
        except:
            return view_student_error(msg="Erro ao exibir os usuários", status=400)
    
    async def update_student(dto) -> deleted_student:
        try:
            return dto
        except:
            return "Quebrou"
    
    async def delete_student(dto) -> deleted_student:
        try:
            await Student.filter(id=dto.id, email=dto.email).delete()
            
            return deleted_student(email=dto.email, deleted=True)
        except:
            return deleted_student(email=dto.email, deleted=False)
