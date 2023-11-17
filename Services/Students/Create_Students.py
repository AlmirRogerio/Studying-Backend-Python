from Repositories.Students.repository import student_repository

class Create_Students():
 
    async def create_student(dto):
        return await student_repository.create_student(dto)