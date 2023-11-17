from Repositories.Students.repository import student_repository

class Delete_Students():
 
    async def delete_student(dto):
        return await student_repository.delete_student(dto)