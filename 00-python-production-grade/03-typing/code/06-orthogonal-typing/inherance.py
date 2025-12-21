import typing
import enum
class IManejo(typing.Protocol):
    
    def acelerar(self) -> bool: ...

    def frenar(self) -> bool: ...
    
    def mostrar_gasolina(self) -> str: ...


class Marcas(enum.StrEnum):
    toyota = "Toyota"
    mercerdez = "Mercedez"
    bmw = "BMW"

class Vehiculo:

    def __init__(self, marca: Marcas, asientos: int)->None:
        self.marca = marca
        self.asientos = asientos

@typing.final
class Moto(Vehiculo, IManejo):

    def __init__(self, marca: Marcas, asientos: int, gasolina_litros: float)->None:
        super().__init__(marca, asientos)
        self.gasolina = gasolina_litros

    def acelerar(self) -> bool:
        return True
    
    def frenar(self) -> bool:
        return True

    # def mostrar_gasolina(self) -> str:
    #     return f"Te quedan {self.gasolina} L." 


if __name__ == "__main__":
    moto_1: Moto = Moto(Marcas.bmw, 4, 2.0)
    print(moto_1.marca)
