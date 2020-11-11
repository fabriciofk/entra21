from __future__ import annotations

# Associação -  Quando uma classe possui um objeto de outra classe.
# Agregação - Quando uma classe possui vários objetos de outra classe.
# Composição - Quando uma classe é dona de um objeto de outra classe.

class Veiculo:
    def __init__(self, modelo: str, marca: str, cor: str) -> None:
        self.__modelo = modelo
        self.__marca = marca
        self.__cor = cor
        self.__passageiros = []
    
    def adiciona_passageiro(self, passageiro: Pessoa):
        self.__passageiros.append(passageiro)
    
    def remove_passageiros(self, passageiro: Pessoa):        
        try:
            self.__passageiros.remove(passageiro)
        except ValueError:
            print('Passageiro informado não está presente no veículo!')

    def listar_passageiros(self):
        for passageiro in self.__passageiros:
            print(passageiro)


class Pessoa:
    def __init__(self, nome: str, idade: int, cpf: str) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf

    def falar(self) -> None:
        print(f'{self.__nome} disse Oi!')

    def __str__(self):
        return self.__nome


if __name__ == "__main__":
    pessoa1 = Pessoa('William', 20, '123-213-123-21')
    pessoa2 = Pessoa('João', 20, '123-213-123-21')
    carro = Veiculo('C3', 'Renault', 'Preto')
    carro.adiciona_passageiro(pessoa1)
    carro.adiciona_passageiro(pessoa2)
    carro.listar_passageiros()
    carro.remove_passageiros(pessoa1)
    carro.listar_passageiros()
