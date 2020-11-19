import os
from classes import Pessoa, Veiculo
from salvar_banco import database_operations


def select_pragma(table_name: str) -> list:
    query = f'PRAGMA table_info({table_name});'
    pragma = database_operations(query)
    return pragma


def print_pragma(table_name: str) -> None:
    pragma = select_pragma(table_name)

    for campo in pragma:
        if campo == pragma[-1]:
            print(f'{campo[0]} - {campo[1].upper()}')
        else:
            print(f'{campo[0]} - {campo[1].upper()}', end=' | ')


def select_todos(nome_tabela: str) -> list:
    """Retorna uma lista com todos os registros da tabela especificada"""
    query = f'SELECT * FROM {nome_tabela};'

    lista_pessoas = database_operations(query)

    return lista_pessoas


def print_pessoas() -> None:
    """Mostra na tela todas as pessoas cadastradas no banco"""
    lista_pessoas = select_todos('pessoa')

    for pessoa in lista_pessoas:
        print(pessoa)


def print_veiculos() -> None:
    """Mostra na tela todos os veículos cadastradas no banco"""
    lista_veiculos = select_todos('veiculo')

    for veiculo in lista_veiculos:
        print(veiculo)


def apaga_tela() -> None:
    """Apaga a tela do console"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def print_menu(opcoes: dict) -> str:
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
    data_nascimento = input('Digite sua data de nascimento (dd-mm-aaaa): ')
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
    if not select_todos('pessoa'):
        print('Não é possível cadastrar um veículo pois não existe nenhuma pessoa '
              'cadastrada no banco')
    else:
        nome = input('Digite o apelido do carro: ')
        marca = input('Digite a marca do carro: ')
        modelo = input('Digite o modelo do carro: ')
        ano = int(input('Digite o ano do carro: '))
        placa = input('Digite a placa do carro: ')
        print_pessoas()
        proprietario = input('Digite o ID do proprietário do carro: ')
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

    opcao_escolhida = print_menu(menu)

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
    print_pragma('pessoas')
    print_pessoas()
    print('*'*100)
    print('Imprimindo dados da tabela Veiculo:')
    print('*'*100)
    print_pragma('veiculos')
    print_veiculos()
    input('Pressione RETURN para voltar ao menu principal.')


def select_item(nome_tabela: str, ide: int) -> str:
    lista_pragma = select_pragma(nome_tabela)

    query = f'SELECT * FROM {nome_tabela} WHERE {lista_pragma[0][1]} = ?;'

    return database_operations(query, ide)


def atualizar_veiculo() -> None:
    print_pragma('veiculo')
    print_pessoas()

    pragma = select_pragma('veiculo')
    # Dicionário com o ID do campo e o nome do Campo
    pragma_dict = {campo[0]: campo[1] for campo in pragma}

    ide = int(input('Digite o ID do veículo que deseja alterar: '))

    veiculo = select_item('veiculo', ide)

    # Em caso de erro
    if veiculo:
        print(veiculo)

        campo = input('Digite o número do campo que deseja alterar: ')

        for chave, valor in pragma_dict.items():
            if campo == chave:
                novo_valor = input('Digite o novo valor do campo: ')
                query = f'UPDATE veiculo SET {valor} = ? WHERE id_veiculo == ?;'
                database_operations(query, novo_valor)
                print('Dados do veículo atualizados com sucesso!')
                return

        print('Campo informado não existe.')


def atualizar_pessoa() -> None:
    print_pragma('pessoa')
    print_pessoas()

    pragma = select_pragma('pessoa')
    # Dicionário com o ID do campo e o nome do Campo
    pragma_dict = {campo[0]: campo[1] for campo in pragma}

    ide = int(input('Digite o ID da pessoa que deseja alterar: '))

    pessoa = select_item('pessoa', ide)
    print(pessoa)
    input()
    # Em caso de erro
    if pessoa:
        print(pessoa)

        campo = input('Digite o número do campo que deseja alterar: ')

        for chave, valor in pragma_dict.items():
            if campo == chave:
                novo_valor = input('Digite o novo valor do campo: ')
                query = f'UPDATE pessoa SET {valor} = ? WHERE id_pessoa == ?;'
                database_operations(query, novo_valor)
                print('Dados da pessoa atualizados com sucesso!')
                return

        print('Campo informado não existe.')


def atualizar_dados() -> None:
    """Atualiza uma linha no banco de dados"""
    opcoes = {
        '1': 'Atualizar dados de pessoa',
        '2': 'Atualizar dados de veículo'
    }

    escolha = print_menu(opcoes)

    if escolha == '1':
        atualizar_pessoa()
    elif escolha == '2':
        atualizar_veiculo()


def deletar_dados() -> None:
    """Deleta uma linha do banco de dados"""
    print('''1 - Deletar dados do veiculo
    2 - Deletar dados da pessoa''')

    resp = input('\nDigite a operação desejada: ')

    # --Deletar veiculo
    if resp == '1':
        print_veiculos()
        id_veiculo = input('Digite o ID do veículo que você quer remover: ')
        query = """
            DELETE FROM veiculo 
            WHERE id_veiculo = ?
        """
        database_operations(query, id_veiculo)
        print('O veículo foi deletado com sucesso!')

    # ---Deletar pessoa
    elif resp == '2':
        print_pessoas()
        id_pessoa = input('Digite o Id da pessoa que você quer remover: ')

        query_veiculos = 'SELECT id_veiculo FROM veiculo WHERE id_pessoa = ?;'
        id_veiculos = database_operations(query_veiculos, id_pessoa)
        if id_veiculos:
            for ide in id_veiculos:
                query = 'DELETE FROM veiculo WHERE id_veiculo = ?;'
                database_operations(query, ide)

        query = """
            DELETE FROM pessoa 
            WHERE id_pessoa = ?
        """
        database_operations(query, id_pessoa)
        print('A pessoa e seus veículos foram deletados com sucesso!')
    else:
        print('Você digitou uma opção inválida!')


def main():
    while True:
        menu_principal = {
            '1': 'Criar dados',
            '2': 'Ler dados',
            '3': 'Atualizar dados',
            '4': 'Deletar dados',
            '0': 'Sair'
        }

        opcao_escolhida = print_menu(menu_principal)

        # Break do while
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
