from tortoise import fields
from tortoise.contrib.pydantic.creator import pydantic_model_creator

from models.base_model import BaseModel

DEFAULT_CHAR_FIELD_LENGTH = 255

class Course(BaseModel):
    name = fields.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH)
    
    class Meta:
        table = "Course"

class Student(BaseModel):
    name = fields.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH)
    email = fields.CharField(max_length=DEFAULT_CHAR_FIELD_LENGTH)
    course= fields.ForeignKeyField(
        "models.Course", "Student"
    )
    
    class Meta:
        table = "Student"

StudentPydantic = pydantic_model_creator(Student)
CoursePydantic = pydantic_model_creator(Course)