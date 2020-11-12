from person import Person
from bank import Bank, BankAccount


def add_person():
    while True:
        nome = input('Digite seu nome:')
        idade = input('Digite sua idade:')
        cpf = input('Digite seu CPF:')
        if nome != '' or idade != '' or cpf != '':
            break
        else:
            print('Dados inválidos!')
    
    person = Person(nome, idade, cpf)
    person.save_person()

def add_account():
    while True:
        cpf = input('Digite o CPF:') 
        bank = int(input('Digite número do banco: '))
        agency = int(input('Digite o número da agencia: '))
        balance = float(input('Digite o saldo da conta: '))

        if not(cpf  and bank and agency and balance):
            print('Dado(s) vazio(s)')
        else:
            break

    while True:   
        try:
            account_number = int(input('Digite o número da conta: '))
            break
        except:
            print('Caracter inválido!')

        
    while True:   
        try:
            password = int(input('Digite a senha: '))
            password = str(password)
            list_password = list(password)
            lenght = len(list_password)
            if lenght != 6:
                print('Tamanho da senha inválido!')
            else:
                break
        except:
            print('Use apenas números!')
    
    account = BankAccount(cpf, password, bank, account_number, agency, balance)
    account.save_bankaccount()
    
def make_deposit() -> None:
    while True:
        account = input('Digite o número da conta: ')
        password = input('Digite sua senha: ')
        value = float(input('Digite o valor do depósito: '))

        BankAccount.make_deposit(account, password, value)        


def view_balance(account_number: str, password: str) -> None:
    account = BankAccount.validate_login(account_number, password)

    if account:
        print(f'O saldo da conta [{account_number}] é: {account["balance"]}')
    else:
        print('Não foi possível recuperar o saldo')


def main():    
    pass
    
if __name__ == "__main__":
    main()