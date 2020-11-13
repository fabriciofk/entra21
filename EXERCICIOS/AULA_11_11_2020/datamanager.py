from csv import DictWriter, DictReader
from typing import List, Callable, Union
from functools import wraps


def data_converter(func: Callable):
    """
    Decorator que converte os dados de uma lista de dicionários str para int e
    float quando possível.
    """
    def data_cast(value: str) -> Union[int, float, str]:
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value

    @wraps(func)
    def wrapper_converter(*args, **kwargs) -> List[dict]:
        dict_list = func(*args, **kwargs)
        for dictionary in dict_list:
            for key, value in dictionary.items():
                dictionary[key] = data_cast(value)

        return dict_list

    return wrapper_converter


class DataWriter:
    def __init__(self, file_name: str, field_names) -> None:
        self.__file_name = file_name
        self.__fieldnames = field_names

    def save_data(self, data_dict: dict) -> None:
        """
        Salva os dados de um objeto no arquivo csv correspondete a sua classe.

        Args:
            data_dict: dicionário com os dados.
        """
        try:
            with open(self.__file_name, 'x', encoding='utf-8', newline='') as csv_file:
                csv_writer = DictWriter(csv_file, fieldnames=self.__fieldnames)
                csv_writer.writeheader()
                csv_writer.writerow(data_dict)
        except FileExistsError:
            with open(self.__file_name, 'a', encoding='utf-8', newline='') as csv_file:
                csv_writer = DictWriter(csv_file, fieldnames=self.__fieldnames)
                csv_writer.writerow(data_dict)

    def update_data(self, dict_list: List[dict]) -> None:
        """
        Atualiza os dados.

        Args:
            dict_list: lista com os dicionários atualizados.
        """
        with open(self.__file_name, 'w', encoding='utf-8', newline='') as csv_file:
            csv_writer = DictWriter(csv_file, fieldnames=self.__fieldnames)
            csv_writer.writeheader()

            for data in dict_list:
                csv_writer.writerow(data)


class DataReader:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    @data_converter
    def get_data(self) -> List[dict]:
        """
        Obtém todos os dados do arquivo csv informado.

        Returns:
            Retorna todos os dados como uma lista.

        Raises:
            FileExistsError se o arquivo não existir.
        """                
        with open(self.file_name) as csv_file:            
            csv_reader = DictReader(csv_file)                                   
            
            return list(csv_reader)


if __name__ == '__main__':
    # print('Testes DataWriter')
    # data_writer = DataWriter('people.csv', ['name', 'age', 'cpf'])
    # data_writer.save_data({'name': 'William', 'age': 20, 'cpf': '110-814-329-69'})
    # data_writer.save_data({'name': None, 'age': None, 'cpf': None})
    # data_writer.update_data([{'name': 'Maria', 'age': 20, 'cpf': '110-814-329-69'},
    #                          {'name': 'William', 'age': 20, 'cpf': '110-814-329-69'}])
    print('Testes DataReader')
    data_reader = DataReader('people.csv')
    data = data_reader.get_data()
    print(data)
    print(type(data[1]['age']))
