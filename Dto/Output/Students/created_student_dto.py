from pydantic import BaseModel

class created_student(BaseModel):
    name: str
    created: bool