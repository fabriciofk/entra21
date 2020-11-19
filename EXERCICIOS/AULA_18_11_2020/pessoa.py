class Pessoa:
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
