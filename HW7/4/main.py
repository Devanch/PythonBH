# импортируем базовую модель
from textwrap import indent
from pydantic import BaseModel
import json

# словарь который требуется сохранить в json строку
data = {
    'age': 45,
    'name': 'Peter',
    'children': [
        {
            'age': 3,
            'name': 'Alice'
        }
    ],
    'married': True,
    'city': None
}


class Children(BaseModel):
    age: int
    name: str


class Person(BaseModel):
    age: int
    name: str
    children: list[Children] = []
    married: bool
    city: None




# создаем объект и заполняем его из словаря
pers_a = Person(**data)

# методом json() из библиотеки pydantic сериализуем объект в строку
pers_a_Json = pers_a.json()


with open("main.json", "w") as json_file:
    b = json.loads(pers_a_Json)
    json.dump(b, json_file, indent=4)

with open("main.json", "r") as json_file:
    a = json.load(json_file)

print(a)