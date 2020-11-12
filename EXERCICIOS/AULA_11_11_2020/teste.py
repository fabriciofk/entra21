from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome: str, sobrenome: str, idade: int, turma: str) -> None:
        self.__nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
    
    @abstractmethod
    def mostra_dados(self) -> None: pass

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value


class Aluno(Pessoa):
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None: 
        super().__init__(nome, sobrenome, idade, None)
    
    def mostra_dados(self) -> None:
        print(f'{self.nome} | {self.sobrenome} | {self.idade}')


if __name__ == "__main__":
    aluno = Aluno('William', 'Círico', 20)
    aluno.mostra_dados()

    aluno.nome = 'Gabriel'
    aluno.mostra_dados() 
    print(aluno.__getattribute__('sobrenome'))
    print(aluno.__dict__)
    print(Aluno.mro())
    