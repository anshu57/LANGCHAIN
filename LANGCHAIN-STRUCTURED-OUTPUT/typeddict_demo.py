from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int


new_person: Person= {'name':'Anshu', 'age':28}

print(new_person)