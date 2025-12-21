
from typing import Optional
import typing


class Person():

    def __init__(self,  name:str, number:int):
        self.name = name 
        self.number = number

things = [
    7,
    Person("Michael", 42),
    7.14,
    "Seven",
    [1,1]
]

for t in things:
    print(t)


# Collections, the "right" way
# from typing import List
# numbers: List[int]=[2,3,5,7,11,13] # Works in 3.5+
numbers: list[int]=[2,3,5,7,11,13] # 3.9+
people: list[Person] = [
    Person("Michael", 42),
    Person("Sarah", 3),
    Person("Zoe", 100),
]

# More complex data structures
user_lookup_by_id: dict[int, Person] = {
    p.number: p
    for p in people
}

u1 = user_lookup_by_id.get("Seven") # <- Error, wrong key type
u2: str = user_lookup_by_id.get(42) # <- Error, not a str
u3 = user_lookup_by_id.get(3)
u4: Optional[Person] = user_lookup_by_id.get(3)
u5: Person = user_lookup_by_id.get(3)
u6: Person | None = user_lookup_by_id.get(3)

print(user_lookup_by_id)


t:typing.Tuple[int, int, Person, str] = (7,7, Person("Alejandro", 2), "")


def get_data()->typing.Tuple[int, int, Person, str]:
    return 7, 7, Person("Alejandro",2), ""

t2 = get_data()
t2[1]