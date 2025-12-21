# Fase 0 - Semana 3: Typing serio + mypy/pyright (strict progresivo)

## 1. Autor
Este contenido ha sido extraido del siguiente repositorio: https://github.com/talkpython/rock-solid-python-with-type-hints-course/tree/main/code

## 2. Static vs Dynamic
### Static Languages vs Dynamic Languages
Existen algunos lenguajes Dinamicos como Python, JavaScript, Ruby, etc. que resuelven el tipado de las variables en tiempo de ejecución. Por otro lado, existeen lenguajes como C# o Java, que validan el tipado antes de la ejecución del programa. 

### Duck Typing and Strong Typing
Strong Typing: Tipado fuerte y estricto
Duck Typing: Si actua como pato y hace como pato, es un pato xd

## 3. Typing in Python
## 3.1. Variables
### 3.1.1 Typing Variables
El tipado de variables nos permite ser más estrictos con el código que escribimos, evitar errores en producción y estandarizar la forma en la que programamos. En el caso de las variables, podemos tipearlas de las siguientes maneras

```python
u: int = 27
v: float = 1.234
c: complex = complex(0, -v)
text: str = "Some text"
b: bytes = b"Bytes text"
lst: list[int] = [1,23,2,4]
s: set[int] = {1, 1, 2, 3, 4}
```

En el caso de que nosotros tipemos una variable, al momento de volver a modificar la variable, si lo hacemos con un tipo de dato diferente al que hemos definido nos va a dar un warning, pero no un error como tal ya que Python no revisa los errores previa la compilación.
```python
y: int = 10
y = "Sad Numebers" # <- Error
```
Estos errores podemos detectarlo usando herramientas como pyright.

### 3.1.2 Nullable Types
Cuando nosotros definimos un tipo de dato en una variable, esta no puede ser None. Tiene que ser si o si del tipo de variable que se ha definido. Existen diferentes opciones para permitir None en una variable tipada:
```python
z: int = 42 # Definimos la variable
z = None # <- En este caso es incorrecto, ya que z no puede ser None

z3: typing.Optional[int] = 43
z3 = None # En este caso si es correcto, ya que int es optional

z4: int | None = 43
z4 = None # Otro caso correcto, disponible a partir de Python 3.5
```
### 3.1.3 Unions
Si queremos definir una variable que permita más de un tipo de dato, podemos utilizar Union. 
```python
un1: typing.Union[int, str] = 1
un2: int | str = 2
un3: int | str = "Three"
```
Si no conoces el tipo de dato de tu variable, puedes utilizar el método de typing llamado Any.
```python
unknown: typing.Any = 78
unknown = 3
unknown = 3.4
unknown = "Seventy"
```

### 3.1.4 Constant
Si tenemos una variable, cuyo valor no queremos que se modificado (Por ejemplo, pi). Entonces usamos Final
```python
CONST = "Fixed value" # Implicit conventional constant
CONST = "No longer fixed!"

CONST_2: typing.Final = "Valor" # Ahora, si se intenta modificar dara error al validar el código
```

### 3.1.5 Beware Litel Bobby Tables
Es importante proteger nuestras variables, por ejemplo en este caso que se muestra a continuación:
```python
# Tenemos un caso de Inyección SQL, donde el usuario pueda modificar una variable. Este bloqueo es estático, y solo nos ayuda a detectar código peligroso usando pyright
student_name = "'; DROP TABLE Students; --"
query = f"SELECT * FROM Students WHERE name ='{student_name}'"
print(query)

# En este caso, tenemos metodos como LiteralString que previenen esto
student_name: typing.LiteralString = "Robert Tables"
query: typing.LiteralString = f"SELECT * FROM Students WHERE name ='{student_name}'"
print(query)

```

## 3.2 Funciones
Existe tipado para funciones, para asegurarnos que los tipos de datos que ingresan sean los correctos. 

```python
def fib(n: int)->int:
    current, nxt = 0, 1
    for _ in range(n):
        current, nxt = nxt, nxt+current
    return current
```

Hay casos, donde tendremos respuestas de tipo None. Para esto, podemos utilizar Optional
```python
def fib_small(n:int)-> Optional[int]:
    if n <= 0:
        return None
    return fib(n)
```
En el caso de que la entrada sea una función, podemos utilizar el método de typing Callable
```python
def use_function_explicit(f: typing.Callable[[str, int], None]):
    f("Michael", 42)
```

## 3.3 Collection
Es recomendable tener colecciones con un solo tipo de datos. Por ejemplo, esto no es una buena práctica. 
```python
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
```
Las colecciones tambien pueden ser tipadas. Por ejemplo, si trabajamos con una lista de int, o una lista de objectos lo podemos definir de la siguiente manera
```python
numbers: list[int]=[2,3,5,7,11,13] # 3.9+
people: list[Person] = [
    Person("Michael", 42),
    Person("Sarah", 3),
    Person("Zoe", 100),
]
```

Un caso adicional que podemos encontrar, es cuando utilizamos un diccionario y queremos obtener un valor, pero este valor puede ser None, en ese caso tenemos las siguientes maneras de manejarlo: 
```python
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
```

En el caso de las Tuplas, podemos definirlas de la siguiente manera:

```python
t:typing.Tuple[int, int, Person, str] = (7,7, Person("Alejandro", 2), "")
```

## 3.4 Classes
Si tenemos una clase y hemos definido un método de tipo @classmethod. Podemos definir la salida de ese méotodo del tipo typing.Self.
```python
class Motorcycle:
    wheel_count: int = 2

    def __init__(self, model: str, style: MotorcycleType, engine_size: int, off_road: bool):
        self.off_road: bool = off_road
        self.engine_size: int = engine_size
        self.style: MotorcycleType = style
        self.model: str = model
        @classmethod

    def create_adventure(cls, model: str, engine_size: int) -> typing.Self:
        return cls(model, MotorcycleType.adventure, engine_size, True)
```

## 3.5 External Types
Podemos definir los métodos de una función, afuera de esta utilizando un archivo .pyi

```python
# calculator.py
def add(x, y):
    return x + y


#calculator.pyi
from typing import Union

RealNumber = Union[int, float]
def add(x: float, y: float) -> float: ...

# p5_external_type.py
import calculator


def main():
    s = calculator.add(1, 3)
    s2 = calculator.add(1.1, 3) #<- esta función ya se encuentra tipada al momento de importarla
    print(s, s2)


if __name__ == "__main__":
    main()

```

## 3.6 Generics
Existen funciones de tipo genericas, las cuales tienen la ventaja de ser reutilizables sin importar el tipo de dato que ingrese.

```python
# 1) Funciones que “devuelven lo mismo que reciben” 
def first[T](items: list[T]) -> T:
    return items[0]

# Beneficio: si pasas list[int], el retorno queda tipado como int (no Any). 
```

```python
# 2) Contenedores/estructuras de datos genéricas
class Box[T]:
    def __init__(self, value: T):
        self.value = value

    def get(self) -> T:
        return self.value
# Beneficio: Box[int].get() retorna int; Box[str].get() retorna str.
```

## 3.7 Gradual Typing
“Gradual typing” (tipado gradual) significa que en Python puedes mezclar código sin tipos y código con tipos, e ir “subiendo el volumen” del tipado poco a poco, archivo por archivo, función por función, sin tener que tipar todo el proyecto desde el día 1.

```python
class Person: ...

def get_user(id: int) -> Person:
    ...

u = get_user(1)   # no anotaste u, pero ahora u es Person por inferencia
u.name            # autocomplete / type checking funciona
```
