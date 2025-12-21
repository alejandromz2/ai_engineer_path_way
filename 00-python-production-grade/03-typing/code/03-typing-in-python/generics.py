
# 1) Funciones que “devuelven lo mismo que reciben” 
def first[T](items: list[T]) -> T:
    return items[0]
# Beneficio: si pasas list[int], el retorno queda tipado como int (no Any).


# 2) Contenedores/estructuras de datos genéricas
class Box[T]:
    def __init__(self, value: T):
        self.value = value

    def get(self) -> T:
        return self.value
# Beneficio: Box[int].get() retorna int; Box[str].get() retorna str.