from Repositories.Courses.repository import Course_repository

class delete_courses():
 
    async def delete_course(dto):
        return await Course_repository.delete_course(dto)