from datamanager import DataWriter, DataReader


class Person:
    def __init__(self, name: str, age: int, cpf: str) -> None:
        self.name = name
        self.age = age
        self.cpf = cpf

    def save_person(self):
        data_dict = self.to_dict() 
        field_names = data_dict.keys()
        data_writer = DataWriter('people.csv', field_names)               
        data_writer.save_data(data_dict)

    def to_dict(self):
        return {'name': self.name, 'age': self.age, 'cpf': self.cpf}
