import datamanager


class Person:
    def __init__(self, name: str, age: int, cpf: str) -> None:
        self.name = name
        self.age = age
        self.cpf = cpf

    def save_person(self):
        data_writer = datamanager.DataWriter('people.csv')
        data_writer.save_data(self)
