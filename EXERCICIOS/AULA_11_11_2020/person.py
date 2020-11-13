from datamanager import DataWriter


class Person:
    __fieldnames = ['name', 'age', 'cpf']

    def __init__(self, name: str, age: int, cpf: str) -> None:
        self.name = name
        self.age = age
        self.__cpf = cpf

    def save_into_file(self):
        data_dict = self.obj_to_dict()
        data_writer = DataWriter('people.csv', Person.__fieldnames)
        try:
            data_writer.save_data(data_dict)
            print('Pessoa cadastrada com sucesso!')
        except Exception as err:
            print(err)
            print('Ocorreu um erro ao cadastrar a pessoa.')

    def obj_to_dict(self):
        return {'name': self.name, 'age': self.age, 'cpf': self.__cpf}
