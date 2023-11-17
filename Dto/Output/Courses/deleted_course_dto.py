from pydantic import BaseModel

class deletedCourse(BaseModel):
    course_id: str
    deleted: bool