from Repositories.Courses.repository import Course_repository

class update_courses():
 
    async def update_course(dto):
        return await Course_repository.update_course(dto)