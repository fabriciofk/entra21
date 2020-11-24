import os
from classes import Pessoa, Veiculo
from gerenciar_banco import banco_operacoes


# ========================================================================== #
#                          FUNÇÕES PARA IMPRIMIR MENUS                       #
# ========================================================================== #
def limpa_console() -> None:
    """Limpa a tela do console"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def print_menu(titulo_menu: str, opcoes: dict) -> str:
    """
    Imprime o menu com as opções fornecidas por parâmetro e valida
    se o usuário digitou uma opção válida.

    Args:
        titulo_menu: título do menu.
        opcoes: dicionário com as opções disponíveis.

    Returns:
        Uma string com a opção escolhida pelo usuário.
    """
    limpa_console()
    while True:
        print('=' * 100)
        print(f'{titulo_menu:^100}')
        print('='*100)

        for key, opcao in opcoes.items():
            print(f'\t{key} - {opcao}')

        print('='*100)

        opcao_escolhida = input('Digite a opção desejada: ')

        if opcao_escolhida in opcoes.keys():
            return opcao_escolhida
        else:
            print('Opção inválida.')


def criar_dados() -> None:
    """Interface para criação de dados."""
    menu = {
        '1': 'Registrar pessoa',
        '2': 'Registrar veículo'
    }

    opcao_escolhida = print_menu('CRIAR DADOS', menu)

    if opcao_escolhida == '1':
        criar_pessoa()
    elif opcao_escolhida == '2':
        criar_veiculo()

    input('Pressione RETURN para voltar ao menu principal.')


def ler_dados() -> None:
    """Interface para leitura de dados."""
    opcoes = {
        '1': 'Visualizar pessoas cadastradas',
        '2': 'Visualizar veículos cadastrados'
    }

    opcao_escolhida = print_menu('VISUALIZAR DADOS', opcoes)

    limpa_console()
    if opcao_escolhida == '1':
        if select_todos_registros('pessoa'):
            print('='*100)
            print('Imprimindo todos os registros da tabela Pessoa:')
            print('='*100)
            print_pessoas()
        else:
            print('Não existe nenhuma pessoa cadastrada.')
    elif opcao_escolhida == '2':
        if select_todos_registros('veiculo'):
            print('='*100)
            print('Imprimindo todos os registros da tabela Veiculo:')
            print('='*100)
            print_veiculos()
        else:
            print('Não existe nenhum veículo cadastrado.')

    input('\nPressione RETURN para voltar ao menu principal.')


def atualizar_dados() -> None:
    """Interface para atualização de dados."""
    opcoes = {
        '1': 'Atualizar dados de pessoa',
        '2': 'Atualizar dados de veículo'
    }

    opcao_escolhida = print_menu('ATUALIZAR DADOS', opcoes)

    if opcao_escolhida == '1':
        atualizar_pessoa()
    elif opcao_escolhida == '2':
        atualizar_veiculo()

    input('Pressione RETURN para voltar ao menu principal.')
# ========================================================================== #


# ========================================================================== #
#                       FUNÇÕES PARA SELECIONAR DADOS                        #
# ========================================================================== #
def select_colunas(nome_tabela: str) -> list:
    """
    Selecina todas as colunas de uma tabela.

    Args:
        nome_tabela: nome da tabela.

    Returns:
        Uma lista com todas as informações das colunas de uma tabela.
    """
    query = f'PRAGMA table_info({nome_tabela});'

    colunas = banco_operacoes(query)

    return colunas


def select_todos_registros(nome_tabela: str) -> list:
    """
    Seleciona todos os registros de uma tabela.

    Args:
        nome_tabela: nome da tabela.

    Returns:
        Uma lista com todos os registros da tabela.
    """
    query = f'SELECT * FROM {nome_tabela};'

    lista_registros = banco_operacoes(query)

    return lista_registros


def select_registro(nome_tabela: str, id_registro: str) -> tuple:
    """
    Seleciona um registro da tabela informada pelo ID.

    Args:
        nome_tabela: nome da tabela.
        id_registro: ID do registro.

    Returns:
        Uma tupla com as informações do registro.

    Raises:
        IndexError: Se o registro com o ID informado não existir.
    """
    id_tabela = select_colunas(nome_tabela)[0][1]

    query = f'SELECT * FROM {nome_tabela} WHERE {id_tabela} = ?;'

    registro = banco_operacoes(query, (id_registro,))[0]

    return registro
# ========================================================================== #


# ========================================================================== #
#                        FUNÇÕES PARA PRINTAR DADOS                          #
# ========================================================================== #
def print_colunas(nome_tabela: str) -> None:
    """
    Printa o índice da coluna e a coluna separada por | de todas as colunas na
    tabela informada.

    Args:
        nome_tabela: nome da tabela.
    """
    colunas_info = select_colunas(nome_tabela)
    colunas = [f'{info[0]} - {info[1].upper()}' for info in colunas_info]

    string_colunas = ' | '.join(colunas)
    print(string_colunas)


def print_pessoas() -> None:
    """Printa todas as pessoas cadastradas no banco."""
    lista_pessoas = select_todos_registros('pessoa')

    print_colunas('pessoa')
    for pessoa in lista_pessoas:
        print(*pessoa, sep=', ')


def print_veiculos() -> None:
    """Printa todos os veículos cadastradas no banco."""
    lista_veiculos = select_todos_registros('veiculo')

    print_colunas('veiculo')
    for veiculo in lista_veiculos:
        print(*veiculo, sep=', ')
# ========================================================================== #


# ========================================================================== #
#                       FUNÇÕES PARA CRIAR DADOS                             #
# ========================================================================== #
def criar_pessoa() -> None:
    """Coleta os dados da pessoa e adiciona o veículo no banco de dados"""
    limpa_console()
    print('=' * 100)
    print(f'{"REGISTRANDO PESSOA":^100}')
    print('=' * 100)
    nome = input('Digite o nome da pessoa: ').upper()
    data_nascimento = input('Digite a data de nascimento da pessoa (dd-mm-aaaa): ')
    cpf = input('Digite o CPF da pessoa: ')
    endereco = input('Digite o endereço da pessoa: ').upper()
    salario = float(input('Digite o salario da pessoa: '))
    profissao = input('Digite a profissão da pessoa: ').upper()
    email = input('Digite o email da pessoa: ').upper()
    telefone = input('Digite o telefone da pessoa: ')
    nome_responsavel = input('Digite o nome do responsável (Se houver): ').upper()

    if not nome_responsavel:
        nome_responsavel = 'MAIOR DE IDADE'

    sexo = input('Digite o sexo (M ou F): ').upper()
    naturalidade = input('Digite a naturalidade da pessoa: ').upper()
    nacionalidade = input('Digite a nacionalidade da pessoa: ').upper()

    # Instanciando um objeto pessoa
    pessoa = Pessoa(nome, data_nascimento, cpf, endereco, salario, profissao, email, telefone,
                    nome_responsavel, sexo, naturalidade, nacionalidade)

    # Query para salvar a pessoa
    query = 'INSERT INTO pessoa (nome, data_nascimento, cpf, endereco, salario, profissao, ' \
            'email, telefone, nome_responsavel, sexo, naturalidade, nacionalidade) ' \
            'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'

    # Salvando o objeto no banco
    banco_operacoes(query, pessoa.to_tuple())
    print('Pessoa cadastrada com sucesso!')


def criar_veiculo() -> None:
    """Coleta os dados do veículo e adiciona o veículo no banco de dados"""
    limpa_console()
    print('=' * 100)
    print(f'{"REGISTRANDO VEÍCULO":^100}')
    print('='*100)
    if not select_todos_registros('pessoa'):
        print('Não é possível cadastrar um veículo pois não existe nenhuma pessoa '
              'cadastrada no banco.')
    else:
        nome = input('Digite o apelido do veículo: ').upper()
        marca = input('Digite a marca do veículo: ').upper()
        modelo = input('Digite o modelo do veículo: ').upper()
        ano = int(input('Digite o ano do veículo: '))
        placa = input('Digite a placa do veículo: ').upper()

        while True:
            print_pessoas()

            id_pessoa = input('Digite o ID do proprietário do veículo: ')

            try:
                select_registro('pessoa', id_pessoa)
                break
            except IndexError:
                print('ID informado não está cadastrado.')

        num_portas = int(input('Digite a quantidade de portas do veículo: '))
        cor = input('Digite a cor do veículo: ').upper()
        km_rodados = float(input('Digite a quantidade de km_rodados: '))
        qtd_passageiros = int(input('Digite a quantidade de passageiros: '))
        motor = input('Digite o tipo de motor do veículo: ').upper()
        combustivel = input('Digite o tipo de combustível: ').upper()
        meio_locomocao = input('Digite o meio de locomoção (TERRESTRE, AÉREO, MARÍTIMO): ').upper()

        # Instanciando o objeto
        veiculo = Veiculo(nome, marca, modelo, ano, placa, id_pessoa, num_portas, cor, km_rodados,
                          qtd_passageiros, motor, combustivel, meio_locomocao)

        # Query para salvar o veículo
        query = 'INSERT INTO veiculo (nome, marca, modelo, ano, placa, id_pessoa, num_portas, ' \
                'cor, km_rodados, qtd_passageiros, motor, combustivel, meio_locomocao) ' \
                'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'

        # Salvando o objeto no banco
        banco_operacoes(query, veiculo.to_tuple())
        print('Veículo cadastrado com sucesso!')

# ========================================================================== #


# ========================================================================== #
#                      FUNÇÕES PARA ATUALIZAR DADOS                          #
# ========================================================================== #
def atualizar_veiculo() -> None:
    if not select_todos_registros('veiculo'):
        print('Não existe nenhum veículo cadastrado.')
        return

    print_veiculos()

    ide = input('Digite o ID do veículo que deseja alterar: ')
    try:
        veiculo_selecionado = select_registro('veiculo', ide)
        limpa_console()
        print('Veículo selecionado:')
        print_colunas('veiculo')
        print(*veiculo_selecionado, sep=', ')

        campo = input('Digite o número do campo que deseja alterar: ')

        colunas = select_colunas('veiculo')
        colunas_dict = {str(campo[0]): campo[1] for campo in colunas}

        for chave, valor in colunas_dict.items():
            if campo == chave:
                novo_valor = input('Digite o novo valor do campo: ')
                query = f'UPDATE veiculo SET {valor} = ? WHERE id_veiculo = ?;'
                banco_operacoes(query, (novo_valor, ide))
                print('Dados do veículo atualizados com sucesso!')
                return

        print('Campo informado não existe.')
    except IndexError:
        print('Não existe um veículo cadastrado com esse ID.')


def atualizar_pessoa() -> None:
    if not select_todos_registros('pessoa'):
        print('Não existe nenhuma pessoa cadastrada.')
        return

    print_pessoas()

    ide = input('Digite o ID da pessoa que deseja alterar: ')
    try:
        pessoa_selecionada = select_registro('pessoa', ide)
        limpa_console()
        print('Pessoa selecionada:')
        print_colunas('pessoa')
        print(*pessoa_selecionada, sep=', ')

        campo = input('Digite o índice do campo que deseja alterar: ')

        colunas = select_colunas('pessoa')
        colunas_dict = {str(campo[0]): campo[1] for campo in colunas}

        for chave, valor in colunas_dict.items():
            if campo == chave:
                novo_valor = input('Digite o novo valor do campo: ')
                query = f'UPDATE pessoa SET {valor} = ? WHERE id_pessoa = ?;'
                banco_operacoes(query, (novo_valor, ide))
                print('Dados da pessoa atualizados com sucesso!')
                return

        print('Campo informado não existe.')
    except IndexError:
        print('Não existe uma pessoa cadastrada com esse ID.')
# ========================================================================== #


# ========================================================================== #
#                         FUNÇÃO PARA DELETAR DADOS                          #
# ========================================================================== #
def deletar_dados() -> None:
    """Deleta um regisro do banco de dados"""
    opcoes = {
        '1': 'Deletar dado da tabela pessoa',
        '2': 'Deletar dado da tabela veículo'
    }

    resp = print_menu('DELETAR DADOS', opcoes)

    limpa_console()
    # ---Deletar pessoa
    if resp == '1':
        if select_todos_registros('pessoa'):
            print_pessoas()
            id_pessoa = input('Digite o ID da pessoa que você quer remover: ')

            try:
                # Verificando se a pessoa com o ID informado existe
                select_registro('pessoa', id_pessoa)

                # Deletando todos os veículos associados a pessoa
                query_select_veiculos = 'SELECT id_veiculo FROM veiculo WHERE id_pessoa = ?;'
                lista_veiculos = banco_operacoes(query_select_veiculos, id_pessoa)
                if lista_veiculos:
                    query_delete = 'DELETE FROM veiculo WHERE id_veiculo = ?;'
                    for veiculo in lista_veiculos:
                        banco_operacoes(query_delete, veiculo)

                # Deletando o registro da pessoa selecionada do banco de dados
                query_delete = """
                                            DELETE FROM pessoa 
                                            WHERE id_pessoa = ?
                                        """
                banco_operacoes(query_delete, id_pessoa)
                print('A pessoa e seus veículos foram deletados com sucesso!')
            except IndexError:
                print('Não existe uma pessoa cadastrada com o ID informado.')
        else:
            print('Não é possível realizar a operação: Nenhuma pessoa cadastrada.')

    # ---Deletar veículo
    elif resp == '2':
        if select_todos_registros('veiculo'):
            print_veiculos()
            id_veiculo = input('Digite o ID do veículo que você quer remover: ')

            try:
                # Verificando se o veículo com o ID informado existe
                select_registro('veiculo', id_veiculo)

                # Deletando o veículo do banco de dados
                query_delete = """
                                        DELETE FROM veiculo 
                                        WHERE id_veiculo = ?
                                    """
                banco_operacoes(query_delete, id_veiculo)
                print('O veículo foi deletado com sucesso!')
            except IndexError:
                print('Não existe um veículo cadastrado com o ID informado.')
        else:
            print('Não é possível realizar a operação: Nenhum veículo cadastrado.')
    else:
        print('Você digitou uma opção inválida!')

    input('Pressione RETURN para voltar ao menu principal.')

# ========================================================================== #


def main():
    while True:
        menu_principal = {
            '1': 'Criar dados',
            '2': 'Ler dados',
            '3': 'Atualizar dados',
            '4': 'Deletar dados',
            '0': 'Sair'
        }

        opcao_escolhida = print_menu('CRUD', menu_principal)

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
