from abc import ABC, abstractmethod


class Veiculo(ABC):
    def __init__(self, marca: str, modelo: str, cor: str, preco: float, placa: str) -> None:    
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__preco = preco
        self.__placa = placa
    
    @property
    def modelo(self) -> None:
        return self.__modelo

    @abstractmethod
    def buzina(self) -> None: pass
        
    @abstractmethod
    def acelera(self) -> None: pass
    
    @abstractmethod
    def freia(self) -> None: pass


class Carro(Veiculo):    
    def buzina(self) -> None:
        print(f'O carro do modelo {self.modelo} está buzinando.')
        
    def acelera(self) -> None:
        print(f'O carro do modelo {self.modelo} está acelerando.')
    
    def freia(self) -> None:
        print(f'O carro do modelo {self.modelo} está freiando.')
    

class Moto(Veiculo):        

    def buzina(self) -> None:
        print(f'A moto do modelo {self.modelo} está buzinando.')
        
    def acelera(self) -> None:
        print(f'A moto do modelo {self.modelo} está acelerando.')
    
    def freia(self) -> None:
        print(f'A moto do modelo {self.modelo} está freiando.')


class Bicicleta(Veiculo):    

    def buzina(self) -> None:
        print(f'A bicicleta do modelo {self.modelo} está buzinando.')
        
    def acelera(self) -> None:        
        print(f'A bicicleta do modelo {self.modelo} está acelerando.')
    
    def freia(self) -> None:
        print(f'A bicicleta do modelo {self.modelo} está freiando.')


if __name__ == "__main__":
    carro = Carro('Marca1', 'Modelo1', 'Cor1', 100.00, 'Placa1')
    moto = Moto('Marca2', 'Modelo2', 'Cor2', 200.00, 'Placa2')
    bicicleta = Bicicleta('Marca2', 'Modelo3', 'Cor3', 300.00, 'Placa3')
    
    carro.acelera()
    moto.acelera()
    bicicleta.acelera()