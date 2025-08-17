from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'Anshu'
    age: Optional[int] = None
    email: EmailStr
    CGPA: float = Field(gt=0, lt=10, default=5, description="Decimal value representing the cgpa of" \
    "the student")

new_student = {'age': '32', 'email': 'abc@gmail.com'} #type coercing by itself by pydantic

student = Student(**new_student)

student_dict = dict(student)
print(student_dict['age'])

student_json = student.model_dump_json()

print(student_json)