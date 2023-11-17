from pydantic import BaseModel

class updateCourse(BaseModel):
    course_id: int
    name: str