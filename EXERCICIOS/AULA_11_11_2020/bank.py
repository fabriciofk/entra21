from datamanager import DataWriter, DataReader
from typing import Tuple, List


class Bank:
    def __init__(self, code: int, name: str) -> None:
        self.code = code
        self.name = name


class BankAccount:
    def __init__(self, person_cpf: str, password: int, bank: int, account_number: int,
                 agency: int, balance: float) -> None:
        self.person = person_cpf
        self.password = password
        self.bank = bank
        self.account_number = account_number
        self.agency = agency
        self.balance = balance    
    
    @staticmethod
    def validate_login(account_number: str, password: str) -> dict:
        data_reader = DataReader('bankaccounts.csv')
        data_list = data_reader.get_data()
                
        for data_dict in data_list:            
            if data_dict['account_number'] == account_number and data_dict['password'] == password:
                return data_dict                

    @classmethod
    def make_deposit(cls, account_number: str, password: str, value: float) -> None:
        target_data = cls.validate_login(account_number, password)

        if target_data:    
            data_reader = DataReader('bankaccounts.csv')
            data_list = data_reader.get_data()

            for data in data_list:
                if data['account_number'] == target_data['account_number']:
                    print(data['balance'])
                    data['balance'] = float(data['balance']) + value     

            field_names = data_list[0].keys()
            data_writer = DataWriter('bankaccounts.csv', field_names) 
            data_writer.update_data(data_list)

    def save_bankaccount(self) -> None:
        field_names = self.to_dict().keys()        
        data_writer = DataWriter('bankaccounts.csv', field_names)
        data_dict = self.to_dict()
        data_writer.save_data(data_dict)

    def to_dict(self):
        return {
            'person': self.person, 
            'password': self.password, 
            'bank': self.bank,
            'account_number': self.account_number,
            'agency': self.agency,
            'balance': self.balance
            }
    