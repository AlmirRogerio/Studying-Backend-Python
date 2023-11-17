from pydantic import BaseModel

class delete_student(BaseModel):
    id: int
    email: str