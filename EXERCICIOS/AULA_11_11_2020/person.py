import datamanager


class Person:
    def __init__(self, name: str, age: int, cpf: str) -> None:
        self.name = name
        self.age = age
        self.cpf = cpf

    def save_person(self):
        data_writer = datamanager.DataWriter('people.csv')
        data_dict = self.to_dict()
        fieldnames = list(data_dict.keys())

        data_writer.save_data(data_dict, fieldnames)

    def to_dict(self):
        return {'name': self.name, 'age': self.age, 'cpf': self.cpf}


if __name__ == '__main__':
    pessoa1 = Person('William', 20, '123-456-789-10')
