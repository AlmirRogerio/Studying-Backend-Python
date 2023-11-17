from pydantic import BaseModel

class view_student(BaseModel):
    student_id: int
    name: str
    email: str
    course: str

class view_student_error(BaseModel):
    msg: str
    status: int