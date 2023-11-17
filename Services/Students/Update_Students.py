from Repositories.Students.repository import student_repository

class Update_students():
     
    async def update_student(dto):
        return await student_repository.update_student(dto)