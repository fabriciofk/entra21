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

    def save_data(self, data_dict: dict, fieldnames: List[str]) -> None:
        """
        Salva os dados de um objeto no arquivo csv correspondete a sua classe.

        Args:
            data_dict: dicionário com objetos.
            fieldnames: lista com os fieldnames do arquivo.
        """
        try:
            with open(self.file_name, 'x', encoding='utf-8', newline='') as csv_file:
                csv_writer = DictWriter(csv_file, fieldnames=fieldnames)
                csv_writer.writeheader()
                csv_writer.writerow(data_dict)
        except FileExistsError:
            with open(self.file_name, 'a', encoding='utf-8', newline='') as csv_file:
                csv_writer = DictWriter(csv_file, fieldnames=fieldnames)
                csv_writer.writerow(data_dict)

    def update_data(self, dict_list: List[dict], fieldnames: List[str]) -> None:
        """
        Atualiza os dados.

        Args:
            dict_list: lista com os objetos atualizados.
            fieldnames: lista com os fieldnames do arquivo.
        """
        with open(self.file_name, 'w', encoding='utf-8', newline='') as csv_file:
            csv_writer = DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            # Escrevendo no arquivo
            for data in dict_list:
                csv_writer.writerow(data)


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
