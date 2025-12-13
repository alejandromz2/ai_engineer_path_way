from typing import Self
from datetime import date

class Calculator:
    def __init__(self, version: int):
        self.version = version

    # Instance Method: Method that change depending of the input. Each instance had its own local instance variable. We use the version of the variable from the instance, not from the class
    def description(self):
        print(f'Currently running Calculator on version {self.version}')

    # Static Method: Method that can be used anywhere that doesn't rely on the class, because we don't use the instance inside the function
    @staticmethod
    def add_numbers(self, *numbers:float) -> float:
        return sum(numbers)
    
    


if __name__ == '__main__':

    calc1 = Calculator(10)
    calc2 = Calculator(200)

    calc1.description()
    calc2.description()

    print(Calculator.add_numbers(10, 20, 30))