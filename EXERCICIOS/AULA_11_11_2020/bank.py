from __future__ import annotations
from datamanager import DataWriter, DataReader
from typing import List


class Bank:
    def __init__(self, code: int, name: str) -> None:
        self.code = code
        self.name = name


class BankAccount:
    __fieldnames = ['person_cpf', 'password', 'bank', 'agency', 'balance', 'account_number']

    def __init__(self, person_cpf: str, password: int, bank: int, agency: int, balance: float,
                 account_number: int = None) -> None:
        self.__person_cpf = person_cpf
        self.__password = password
        self.__bank = bank
        self.__account_number = account_number or self.__generate_account_number()
        self.__agency = agency
        self.__balance = balance

    @property
    def person_cpf(self):
        return self.__person_cpf

    @property
    def password(self):
        return self.__password

    @property
    def bank(self):
        return self.__bank

    @property
    def account_number(self):
        return self.__account_number

    @property
    def agency(self):
        return self.__agency

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    @staticmethod
    def __generate_account_number() -> int:
        try:
            objects_list = BankAccount.__get_all_from_file()
            last_account_number = objects_list[-1].account_number
            return last_account_number + 1
        except Exception:
            return 1

    @staticmethod
    def __get_all_from_file() -> List[BankAccount]:
        data_reader = DataReader('bankaccounts.csv')
        data_dict_list = data_reader.get_data()
        objects_list = [BankAccount(*data_dict.values()) for data_dict in data_dict_list]

        return objects_list

    @staticmethod
    def __get_bankaccount_from_file(account_number: int) -> BankAccount:
        objects_list = BankAccount.__get_all_from_file()

        for obj in objects_list:
            if obj.account_number == account_number:
                return obj

        print('Conta informada não está registrada no sistema.')

    @staticmethod
    def __is_password_valid(bankaccount: BankAccount, password: int) -> bool:
        if bankaccount.password == password:
            return True

        print('Senha inválida')
        return False

    @staticmethod
    def make_deposit(account_number: int, password: int, value: float) -> None:
        bankaccount = BankAccount.__get_bankaccount_from_file(account_number)

        if bankaccount:
            if BankAccount.__is_password_valid(bankaccount, password):
                bankaccount.balance += value
                object_list = BankAccount.__get_all_from_file()
                for index, obj in enumerate(object_list):
                    if obj.account_number == bankaccount.account_number:
                        object_list[index] = bankaccount
                try:
                    BankAccount.__update_file(object_list)
                    print('Depósito realizado com sucesso!')
                    print(f'Saldo atual: {bankaccount.balance}')
                except Exception:
                    print('Ocorreu um erro ao realizar o depósito.')

    @staticmethod
    def view_balance(account_number: int, password: int) -> None:
        bankaccount = BankAccount.__get_bankaccount_from_file(account_number)

        if bankaccount:
            if BankAccount.__is_password_valid(bankaccount, password):
                print(f'Seu saldo é: {bankaccount.balance}')

    @classmethod
    def __update_file(cls, object_list: List[BankAccount]) -> None:
        dict_list = []
        for obj in object_list:
            dictionary = {
                'person_cpf': obj.person_cpf,
                'password': obj.password,
                'bank': obj.bank,
                'agency': obj.agency,
                'balance': obj.balance,
                'account_number': obj.account_number
            }
            dict_list.append(dictionary)

        data_writer = DataWriter('bankaccounts.csv', cls.__fieldnames)
        data_writer.update_data(dict_list)

    def save_into_file(self):
        data_dict = self.obj_to_dict()
        data_writer = DataWriter('bankaccounts.csv', BankAccount.__fieldnames)
        try:
            data_writer.save_data(data_dict)
            print('Conta cadastrada com sucesso!')
            print(f'Número da conta: {self.__account_number}')
        except Exception as err:
            print(err)
            print('Ocorreu um erro ao cadastrar a conta.')

    def obj_to_dict(self):
        return {
            'person_cpf': self.__person_cpf,
            'password': self.__password,
            'bank': self.__bank,
            'agency': self.__agency,
            'balance': self.__balance,
            'account_number': self.__account_number
            }


if __name__ == '__main__':
    # print('Testando get_all_from_file')
    # data_list = BankAccount.get_all_from_file()
    # for data in data_list:
    #     print(data.person)
    #     print(data.balance)

    # print('Testando get_bankaccount_from_file')
    # bankaccount = BankAccount.get_bankaccount_from_file(3)
    # print(bankaccount.person)
    # print(bankaccount.balance)

    # print('Testando save_into_file')
    # conta1 = BankAccount('121-123-123-11', 1234, 1, 1000, 1000.0)
    # conta1.save_into_file()
    # conta2 = BankAccount('121-123-123-22', 1234, 2, 2000, 2000.0)
    # conta2.save_into_file()
    # conta3 = BankAccount('121-123-123-33', 1234, 3, 3000, 3000.0)
    # conta3.save_into_file()

    # print('Testando update_file')
    # conta1 = BankAccount('121-123-123-11', 1234, 1, 1000, 1000.0, 1)
    # conta2 = BankAccount('121-123-123-22', 1234, 2, 2000, 2000.0, 2)
    # conta3 = BankAccount('121-123-123-33', 1234, 3, 3000, 4000.0, 3)
    # lista = [conta1, conta2, conta3]
    # BankAccount.update_file(lista)

    # print('Testando generate_account_number')
    # print(BankAccount.generate_account_number())

    # print('Testando make_deposit')
    # BankAccount.make_deposit(1, 1234, 10)

    print('Testando view_balance')
    BankAccount.view_balance(1, 1234)
    BankAccount.view_balance(1, 1233)
    BankAccount.view_balance(4, 1234)
