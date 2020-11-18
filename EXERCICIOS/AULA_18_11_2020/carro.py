class Carro:
    def __init__(self, nome, marca, modelo, ano, placa, proprietario, num_portass, cor, km_rodado, qtd_passageiros, motor, combustivel, meio_locomocao):
        self.nome = nome 
        self.marca =  marca 
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
        self.num_portass, self.cor, self.km_rodado, self.qtd_passageiros, self.motor, self.combustivel, self.meio_locomocao)