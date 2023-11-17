from pydantic import BaseModel

class editedCourse(BaseModel):
    course_name: str
    edited: bool