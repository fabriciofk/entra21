from person import Person
from bank import BankAccount


def add_person():
    print('Cadastrando Pessoa')
    while True:
        nome = input('Digite seu nome: ')
        idade = int(input('Digite sua idade: '))
        cpf = input('Digite seu CPF: ')
        if nome or idade or cpf:
            break
        else:
            print('Dados inválidos! Por favor, digite novamente.')
    
    person = Person(nome, idade, cpf)
    person.save_into_file()


def add_account():
    print('Cadastrando Conta')
    while True:
        cpf = input('Digite o CPF: ')
        bank = int(input('Digite número do banco: '))
        agency = int(input('Digite o número da agencia: '))
        balance = float(input('Digite o saldo da conta: '))

        if not(cpf and bank and agency and balance):
            print('Dado(s) vazio(s)')
        else:
            break

    while True:   
        try:
            password = input('Digite a senha: ')
            if len(password) != 6:
                print('Tamanho da senha inválido!')
            else:
                password = int(password)
                break
        except:
            print('Use apenas números!')
    
    account = BankAccount(cpf, password, bank, agency, balance)
    account.save_into_file()


def make_deposit() -> None:
    print('Fazer Depósito')
    while True:
        account = int(input('Digite o número da conta: '))
        password = int(input('Digite sua senha: '))
        value = float(input('Digite o valor do depósito: '))

        if account and password and value:
            break
        else:
            print('Dados inválidos! Por favor digite novamente.')

    BankAccount.make_deposit(account, password, value)


def view_balance() -> None:
    print('Visualizar Saldo')
    while True:
        account = int(input('Digite o número da conta: '))
        password = int(input('Digite sua senha: '))

        if account and password:
            break
        else:
            print('Dados inválidos! Por favor digite novamente.')

    BankAccount.view_balance(account, password)


def main():
    menu_options = {
        '1': add_person,
        '2': add_account,
        '3': view_balance,
        '4': make_deposit
    }

    while True:
        menu_option = input('-----------------------------------------------------------\n'
                            '|            Digite a operação desejada                   |\n'
                            '-----------------------------------------------------------\n'
                            '|            1 - Cadastrar Pessoa                         |\n'
                            '-----------------------------------------------------------\n'
                            '|            2 - Cadastrar Conta                          |\n'
                            '-----------------------------------------------------------\n'
                            '|            3 - Visualizar Saldo                         |\n'
                            '-----------------------------------------------------------\n'
                            '|            4 - Fazer um depósito                        |\n'
                            '-----------------------------------------------------------\n'
                            '|           0 - Sair                                      |\n'
                            '-----------------------------------------------------------\n'
                            'Opção desejada: ')

        if menu_option == '0':
            print('Encerrando o programa.')
            break

        for option, func in menu_options.items():
            if menu_option == option:
                func()


if __name__ == "__main__":
    main()
