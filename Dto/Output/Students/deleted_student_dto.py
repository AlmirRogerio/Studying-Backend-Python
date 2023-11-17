from pydantic import BaseModel

class deleted_student(BaseModel):
    email: str
    deleted: bool