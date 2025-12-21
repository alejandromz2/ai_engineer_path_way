import typing

#student_name: str = input("What is the student's name?")
student_name: typing.LiteralString = "Robert Tables"
query: typing.LiteralString = f"SELECT * FROM Students WHERE name ='{student_name}'"
print(query)