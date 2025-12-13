from typing import Self
from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self)->str:
        return f'{self.name} is {self.age} years old'
    
    # We are not refearing to the instance anymore, we are now editing the class directly. Any changes we do to this class will affect the actual class. We usually create in this methods a Factory or an alternative Constructor for our Person class
    # The class method is going to affect the actual
    @classmethod
    def age_from_year(cls, name: str, birth_year: int)-> Self:
        current_year: int = date.today().year
        age: int = current_year - birth_year
        return cls(name, age)
    
if __name__ == '__main__':
    alejandro = Person.age_from_year('Alejandro', 2000)
    print(alejandro.description())
