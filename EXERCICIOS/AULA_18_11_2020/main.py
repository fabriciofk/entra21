from pessoa import Pessoa
from carro import Carro
from salvar_banco import database_operations


print('1 - Cadastrar pessoa')
nome = input('Digite seu nome: ')
data_nascimento = input('Digite sua data de nascimento: ')
cpf = input('Digite seu CPF: ')
endereco = input('Digite seu endereço: ')
salario = input('Digite seu salario: ')
profissao = input('Digite sua profissão: ')

pessoa = Pessoa(nome, , )

query = 'INSERT INTO pessoa VALUES (?, ?, ?, ?)', (12313,)
database_operations('database.db', query, pessoa.to_tuple())

print('2 - Listar todas as pessoas')
print('3 - Cadastrar carro')
print('4 - Listar todas os carros')