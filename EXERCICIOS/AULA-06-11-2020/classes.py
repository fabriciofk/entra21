from abc import ABC, abstractmethod


class Teclado:
    def __init__(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
    
    @staticmethod
    def escrever() -> None: 
        print('O teclado está escrevendo!')


class Veiculo(ABC):
    def __init__(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco

    @abstractmethod
    def andar(self) -> None:
        pass


class Bicicleta(Veiculo):       
    def andar(self):
        print(f'A bicicleta do modelo: {self.modelo} está se movendo')      


class Carro(Veiculo):
    def andar(self):
        print(f'O carro do modelo: {self.modelo} está se movendo')      


class Livro:
    def __init__(self, nome, autor, data_publicacao):
        self.nome = nome
        self.autor = autor
        self.data_publicacao = data_publicacao
    
    @staticmethod
    def ler_livro() -> None:
        print('Você está lendo o livro')        


if __name__ == "__main__":
    fusca = Carro('Fusca', 'Preto', 1000.00)
    print(fusca.modelo)
    fusca.andar()