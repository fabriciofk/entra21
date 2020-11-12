from csv import DictWriter, reader
from typing import List, Any, Union
import person
import bank


def data_cast(value: Any) -> Union[int, float, str]:
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            try:
                return str(value)
            except ValueError:
                return value


class DataWriter:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    @staticmethod
    def __set_foreign_key(value_dict: dict, foreign_keys: tuple) -> dict:
        """
                Converte uma lista de str para uma lista de int ou float.

                Args:
                    value_dict: lista de valores a serem convertidos.

                Returns:
                    Se for possível converter para inteiro retorna o valor
                    em inteiro, senão tenta converter para float e retorna
                    o valor, se nenhuma das operações anteriores foi bem-
                    sucedida, retorna a lista de valores em seu estado
                    original.
                """
        typecasted_data = {}
        for key, value in value_dict.items():
            for foreign_key in foreign_keys:
                if hasattr(value, foreign_key):
                    typecasted_data[key] = value.__getattribute__(foreign_key)
            else:
                typecasted_data[key] = value

        return typecasted_data

    def __set_fieldnames(self) -> list:
        """Retorna uma Lista com os fieldnames do arquivo atual."""
        fieldnames = {
            'people.csv': ['name', 'age', 'cpf'],
            'bankaccount.csv': ['person', 'password', 'bank', 'account_number', 'agency', 'balance']
        }

        for file_name, fieldnames_list in fieldnames.items():
            if self.file_name == file_name:
                return fieldnames_list

    def save_data(self, data: object, foreign_key: tuple = None) -> None:
        """
        Salva os dados de um objeto no arquivo csv correspondete a sua classe.

        Args:
            data: objeto.
            foreign_key: chave estrangeira.
        """
        # Armazenando os atributos do objeto como um dicionário.
        data_dictionary = data.__dict__
        # Armazenando os fieldnames de acordo com o objeto.
        fieldnames = self.__set_fieldnames()

        try:
            # Abrindo o arquivo em modo de abertura exclusiva.
            with open(self.file_name, 'x', encoding='utf-8', newline='') as csv_file:
                # Instanciando um DicWriter com o arquivo e o nome dos campos.
                csv_writer = DictWriter(csv_file, fieldnames=fieldnames)
                csv_writer.writeheader()

                # Verificando se existe uma foreign key nos dados.
                if foreign_key:
                    data_dictionary = self.__set_foreign_key(data_dictionary, foreign_key)

                # Escrevendo a linha no arquivo.
                csv_writer.writerow(data_dictionary)
        except FileExistsError:
            # Abrindo o arquivo em modo de update.
            with open(self.file_name, 'a', encoding='utf-8', newline='') as csv_file:
                # Instanciando um DicWriter com o arquivo e o nome dos campos.
                csv_writer = DictWriter(csv_file, fieldnames=fieldnames)

                # Verificando se existe uma foreign key nos dados.
                if foreign_key:
                    data_dictionary = self.__set_foreign_key(data_dictionary, foreign_key)

                print(data_dictionary)
                print(type(data_dictionary))

                # Escrevendo a linha no arquivo.
                csv_writer.writerow(data_dictionary)

    def update_data(self, object_list: List[object]) -> None:
        """
        Atualiza os dados.

        Args:
            object_list: lista com os objetos atualizados.
        """
        with open(self.file_name, 'w', encoding='utf-8', newline='') as csv_file:
            fieldnames = self.__set_fieldnames()
            csv_writer = DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            # Escrevendo no arquivo
            for obj in object_list:
                csv_writer.writerow(obj.__dict__)


class DataReader:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    @staticmethod
    def __data_cast_from_list(value_list: List[str]) -> list:
        """
        Converte uma lista de str para uma lista de int ou float.

        Args:
            value_list: lista de valores a serem convertidos.

        Returns:
            Se for possível converter para inteiro retorna o valor
            em inteiro, senão tenta converter para float e retorna
            o valor, se nenhuma das operações anteriores foi bem-
            sucedida, retorna a lista de valores em seu estado
            original.
        """
        typecasted_list = [data_cast(value) for value in value_list]

        return typecasted_list

    def get_data(self) -> List[Union[person.Person, bank.BankAccount]]:
        """
        Obtém todos os dados do arquivo csv informado.

        Returns:
            Retorna todos os dados como uma lista de objetos.

        Raises:
            FileExistsError se o arquivo não existir.
        """
        # Dicionário com as classes utilizadas para cada arquivo.
        classes = {
            'people.csv': person.Person,
            'bankaccounts.csv': bank.BankAccount
        }

        # Abrindo o arquivo.
        with open(self.file_name) as csv_file:
            # Verificando qual classe será utilizada para instanciar as linhas do arquivo.
            for file_name, class_constructor in classes.items():
                if self.file_name == file_name:
                    # Obtendo os dados do arquivo.
                    csv_reader = reader(csv_file)
                    # Ignorando o cabeçalho.
                    next(csv_reader)

                    # object_list = [class_constructor(*self.data_cast(row)) for row in csv_reader]

                    object_list = []
                    for data_row in csv_reader:
                        # Convertendo os dados do arquivo para o formato certo.
                        typecasted_row = self.__data_cast_from_list(data_row)
                        # Adicionando a linha como um objeto para a lista.
                        object_list.append(class_constructor(*typecasted_row))

                    return object_list
