import person
import datamanager


class Bank:
    def __init__(self, code: int, name: str) -> None:
        self.code = code
        self.name = name


class BankAccount:
    def __init__(self, person_obj: person.Person, password: int, bank: Bank, account_number: int,
                 agency: int, balance: float) -> None:
        self.person = person_obj
        self.password = password
        self.bank = bank
        self.account_number = account_number
        self.agency = agency
        self.balance = balance

    def make_deposit(self, value: float) -> None:
        """
        Verifica se o valor do depósito é válido, caso seja,
        atualiza o saldo.

        Args:
            value: valor do depósito.
        """
        if value > 0:
            self.balance += value
            print('Depósito efetuado com sucesso!')
            print(f'Saldo atual: {self.balance}')
        else:
            print('Valor do depósito é inválido')

    def save_bankaccount(self) -> None:
        data_writer = datamanager.DataWriter('bankaccounts.csv')
        data_writer.save_data(self, ('cpf', 'bank'))
