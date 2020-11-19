from datetime import datetime
import os
from classes import Pessoa, Veiculo
from salvar_banco import database_operations


def select_pessoa() -> None:
    query = """
        SELECT * FROM pessoa;
    """

    lista_pessoas = database_operations(query)

    print('ID | Nome | Data nascimento | CPF | Endereço | Salário | Profissão | Email | Telefone | '
          'Nome responsável | Sexo | Naturalidade | Nacionalidade')

    # Printando todas as pessoas
    for pessoa in lista_pessoas:
        print(pessoa)


def select_veiculo() -> None:
    query = """
        SELECT * FROM veiculo;
    """

    lista_veiculos = database_operations(query)

    print('ID | Nome | Marca | Modelo | Ano | Placa | Proprietário | Número de portas | Cor | '
          'KM rodados | Quantidade de passageiros | Motor | Combustível | Meio de locomoção')

    # Printando todos os veícuols
    for veiculo in lista_veiculos:
        print(veiculo)


def apaga_tela() -> None:
    """Apaga a tela do console"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def imprime_menu(opcoes: dict) -> str:
    """Imprime o menu e retorna a opção escolhida pelo usuário"""
    apaga_tela()
    print('*'*100)
    print('Selecione a opção: ')

    for key, opcao in opcoes.items():
        print(f'{key} - {opcao}')

    print('*'*100)

    opcao_escolhida = input('Digite a opção desejada: ')

    return opcao_escolhida


def add_pessoa() -> None:
    """Coleta os dados da pessoa e adiciona o veículo no banco de dados"""
    nome = input('Digite seu nome: ')
    data_nascimento = input('Digite sua data de nascimento (aaaa-mm-dd): ')
    cpf = input('Digite seu CPF: ')
    endereco = input('Digite seu endereço: ')
    salario = float(input('Digite seu salario: '))
    profissao = input('Digite sua profissão: ')
    email = input('Digite seu email: ')
    telefone = input('Digite seu telefone: ')
    nome_responsavel = input('Digite o nome do responsável: ')
    sexo = input('Digite o sexo (M ou F): ')
    naturalidade = input('Digite a naturalidade da pessoa: ')
    nacionalidade = input('Digite a nacionalidade da pessoa: ')

    # Instanciando um objeto pessoa
    pessoa = Pessoa(nome, data_nascimento, cpf, endereco, salario, profissao, email, telefone,
                    nome_responsavel, sexo, naturalidade, nacionalidade)

    # Query para salvar a pessoa
    query = """
                INSERT INTO 
                    pessoa (nome, data_nascimento, cpf, endereco, salario, profissao, email, telefone, nome_responsavel, sexo, naturalidade, nacionalidade)
                VALUES
                    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """

    # Salvando o objeto no banco
    database_operations(query, pessoa.to_tuple())


def add_veiculo() -> None:
    """Coleta os dados do veículo e adiciona o veículo no banco de dados"""
    nome = input('Digite o apelido do carro: ')
    marca = input('Digite a marca do carro: ')
    modelo = input('Digite o modelo do carro: ')
    ano = int(input('Digite o ano do carro: '))
    placa = input('Digite a placa do carro: ')
    proprietario = input('Digite o proprietário do carro: ')
    num_portas = int(input('Digite a quantidade de portas do carro: '))
    cor = input('Digite a cor do carro: ')
    km_rodados = float(input('Digite a quantidade de km_rodados: '))
    qtd_passageiros = int(input('Digite a quantidade de passageiros: '))
    motor = input('Digite o tipo de motor do carro: ')
    combustivel = input('Digite o tipo de combustível: ')
    meio_locomocao = input('Digite o meio de locomoção (TERRESTRE, AÉREO, MARÍTIMO): ')

    # Instanciando o objeto
    veiculo = Veiculo(nome, marca, modelo, ano, placa, proprietario, num_portas, cor, km_rodados,
                      qtd_passageiros, motor, combustivel, meio_locomocao)

    # Query para salvar o veículo
    query = """
        INSERT INTO 
            veiculo (nome, marca, modelo, ano, placa, proprietario, num_portas, cor, km_rodados, qtd_passageiros, motor, combustivel, meio_locomocao)
        VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """

    # Salvando o objeto no banco
    database_operations(query, veiculo.to_tuple())


def criar_dados() -> None:
    """Interface para criação de dados"""
    menu = {
        '1': 'Adicionar pessoa',
        '2': 'Adicionar veículo'
    }

    opcao_escolhida = imprime_menu(menu)

    if opcao_escolhida == '1':
        add_pessoa()
    elif opcao_escolhida == '2':
        add_veiculo()

    print('Cadastro realizado com sucesso!')
    input('Pressione RETURN para voltar ao menu principal.')


def ler_dados() -> None:
    """Mostra todos os dados das tabelas Pessoa e Veículo"""
    apaga_tela()
    print('*'*100)
    print('Imprimindo dados da tabela Pessoa:')
    print('*'*100)
    select_pessoa()
    print('*'*100)
    print('Imprimindo dados da tabela Veiculo:')
    print('*'*100)
    select_veiculo()
    input('Pressione RETURN para voltar ao menu principal.')


def atualizar_dados() -> None:
    """Atualiza uma linha no banco de dados"""
    ...


def deletar_dados() -> None:
    """Deleta uma linha do banco de dados"""
    ...


def main():
    while True:
        menu_principal = {
            '1': 'Criar dados',
            '2': 'Ler dados',
            '3': 'Atualizar dados',
            '4': 'Deletar dados',
            '0': 'Sair'
        }

        opcao_escolhida = imprime_menu(menu_principal)

        if opcao_escolhida == '0':
            break

        if opcao_escolhida == '1':
            criar_dados()
        elif opcao_escolhida == '2':
            ler_dados()
        elif opcao_escolhida == '3':
            atualizar_dados()
        elif opcao_escolhida == '4':
            deletar_dados()


if __name__ == '__main__':
    main()
