import typing

# Typing Variables 
x = 7
y: int = 10
print(x, y)
x = "Happy numbers"
y = "Sad Numebers"
print(x, y)

u: int = 27
v: float = 1.234
c: complex = complex(0, -v)
text: str = "Some text"
b: bytes = b"Bytes text"
lst: list[int] = [1,23,2,4]
s: set[int] = {1, 1, 2, 3, 4}

# Nullable types
z: int = 42
print(z)
z = None
print(z)

z3: typing.Optional[int] = 43
z4: int | None = 43

print(z3)
z3 = None
print(z3)
z3 = "ABC"

# Unions

un1: typing.Union[int, str] = 1
un2: int | str = 2
un3: int | str = "Three"

print(un1+un2)

# What if you don't know??

unknown: typing.Any = 78

unknown = 3
unknown = 3.4
unknown = "Seventy"

# Constant 
not_const_1 = "Some value"
print(not_const_1)
not_const_1 = "Oter value"
print(not_const_1)

CONST_2 = "Fixel value" #   Implicit conventional constant
print(CONST_2)
CONST_2 = "No longer fixed!"

CONST_3: typing.Final = "Valor"

# Beware Litel Bobby Tables

# student_name = "'; DROP TABLE Students; -- "
# query = f"SELECT * FROM Students WHERE name ='{student_name}'"
# print(query)

# New way: 
student_name: str = input("What is the student's name?")
#student_name: typing.LiteralString = "Robert Tables"
query: typing.LiteralString = f"SELECT * FROM Students WHERE name ='{student_name}'"
print(query)

student_name = "'; DROP TABLE Students; --"
query = f"SELECT * FROM Students WHERE name ='{student_name}'"
print(query)

x: typing.Union[int, None] = 3
