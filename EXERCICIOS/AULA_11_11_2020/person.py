from datamanager import DataWriter, DataReader


class Person:
    def __init__(self, name: str, age: int, cpf: str) -> None:
        self.name = name
        self.age = age
        self.cpf = cpf

    def save_person(self):
        field_names = self.to_dict().keys()
        data_writer = DataWriter('people.csv', field_names)
        data_dict = self.to_dict()        
        data_writer.save_data(data_dict)

    def to_dict(self):
        return {'name': self.name, 'age': self.age, 'cpf': self.cpf}
    
    def get_people(self):
        data_reader = DataReader('people.csv')
        people_list = data_reader.get_data()
        print(people_list)
