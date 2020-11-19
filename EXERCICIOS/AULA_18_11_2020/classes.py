from abc import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def to_tuple(self) -> tuple:
        """Retorna uma tupla com todos os atributos da classe"""
        pass


class Pessoa(Base):
    def __init__(self, nome, data_nascimento, cpf, endereco, salario, profissao, email, telefone,
                 nome_reponsavel, sexo, naturalidade, nacionalidade):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.salario = salario
        self.profissao = profissao
        self.email = email
        self.telefone = telefone
        self.nome_reponsavel = nome_reponsavel
        self.sexo = sexo
        self.naturalidade = naturalidade
        self.nacionalidade = nacionalidade

    def to_tuple(self):
        return (self.nome, self.data_nascimento, self.cpf, self.endereco, self.salario,
                self.profissao, self.email, self.telefone, self.nome_reponsavel, self.sexo,
                self.naturalidade, self.nacionalidade)


class Veiculo(Base):
    def __init__(self, nome, marca, modelo, ano, placa, proprietario, num_portass, cor, km_rodado,
                 qtd_passageiros, motor, combustivel, meio_locomocao):
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.proprietario = proprietario
        self.num_portass = num_portass
        self.cor = cor
        self.km_rodado = km_rodado
        self.qtd_passageiros = qtd_passageiros
        self.motor = motor
        self.combustivel = combustivel
        self.meio_locomocao = meio_locomocao

    def to_tuple(self):
        return (self.nome, self.marca, self.modelo, self.ano, self.placa, self.proprietario,
                self.num_portass, self.cor, self.km_rodado, self.qtd_passageiros, self.motor,
                self.combustivel, self.meio_locomocao)
