from Repositories.Courses.repository import Course_repository

class Create_courses():
 
    async def Create_course(dto):
        return await Course_repository.insert_new_course(dto)