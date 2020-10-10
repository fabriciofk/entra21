# --- Exercício 2  - Variáveis
# --- Crie um menu para um sistema de cadastro de funcionários
# --- O menu deve ser impresso com a função format()
# --- As opções devem ser variáveis do tipo inteiro
# --- As descrições das opções serão:
# ---    Cadastrar funcionário
# ---    Listar funcionários
# ---    Editar funcionário
# ---    Deletar funcionário
# ---    Sair
# --- Além das opções o menu deve conter um cabeçalho e um rodapé
# --- Entre o cabeçalho e o menu e entre o menu e o rodapé deverá ter
#     espaçamento de 3 linhas
# --- Deve ser utilizado os caracteres especiais de quebra de linha e de
#     tabulação
def cad_func():
    print('Cadastrando funcionário')


def list_func():
    print('Listando funcionário')


def edit_func():
    print('Editando funcionário')


def del_func():
    print('Removendo funcionário')


while True:
    opcao_selecionada = input('Menu:\n\n\n\t1) Cadastrar funcionário\n\t'
                              '2) Listar funcionário\n\t3) Editar funcionário\n\t'
                              '4) Deletar funcionário\n\t0) Sair\n\n\nOpcão escolhida: ')

    opcoes = {
        '1': cad_func,
        '2': list_func,
        '3': edit_func,
        '4': del_func
    }

    if opcao_selecionada == '0':
        break

    for opcao, funcao in opcoes.items():
        if opcao_selecionada == opcao:
            funcao()

    print()
