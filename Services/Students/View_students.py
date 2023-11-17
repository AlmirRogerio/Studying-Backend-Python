from Repositories.Students.repository import student_repository

class View_students():
     
    async def view_students():
        return await student_repository.view_students()