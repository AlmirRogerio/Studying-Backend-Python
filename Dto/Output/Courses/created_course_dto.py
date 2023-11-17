from pydantic import BaseModel

class createdCourse(BaseModel):
    course_name: str
    created: bool