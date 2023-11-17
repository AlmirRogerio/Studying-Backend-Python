from Repositories.Courses.repository import Course_repository

class View_courses():
 
    async def view_courses():
        return await Course_repository.view_courses()