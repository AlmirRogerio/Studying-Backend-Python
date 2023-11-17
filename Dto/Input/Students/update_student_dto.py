from pydantic import BaseModel

class update_student(BaseModel):
    id: int
    name: str
    email: str
    course_id: int