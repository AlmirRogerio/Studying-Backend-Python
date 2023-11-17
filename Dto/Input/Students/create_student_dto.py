from pydantic import BaseModel

class create_student(BaseModel):
    name: str
    email: str
    course_id: int