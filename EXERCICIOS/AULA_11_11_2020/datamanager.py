from csv import DictWriter, DictReader
from typing import List, Any, Union, Sequence


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
    def __init__(self, file_name: str, field_names: Sequence[str]) -> None:
        self.file_name = file_name
        self.field_names = field_names

    def save_data(self, data_dict: dict) -> None:
        """
        Salva os dados de um objeto no arquivo csv correspondete a sua classe.

        Args:
            data_dict: dicionário com objetos.
            fieldnames: lista com os fieldnames do arquivo.
        """
        try:
            with open(self.file_name, 'x', encoding='utf-8', newline='') as csv_file:
                csv_writer = DictWriter(csv_file, fieldnames=self.field_names)
                csv_writer.writeheader()
                csv_writer.writerow(data_dict)
                print('Dado salvo com sucesso!')
        except FileExistsError:
            with open(self.file_name, 'a', encoding='utf-8', newline='') as csv_file:
                csv_writer = DictWriter(csv_file, fieldnames=self.field_names)
                csv_writer.writerow(data_dict)
                print('Dado salvo com sucesso!')

    def update_data(self, dict_list: List[dict]) -> None:
        """
        Atualiza os dados.

        Args:
            dict_list: lista com os objetos atualizados.
            fieldnames: lista com os fieldnames do arquivo.
        """
        with open(self.file_name, 'w', encoding='utf-8', newline='') as csv_file:
            csv_writer = DictWriter(csv_file, fieldnames=self.field_names)
            csv_writer.writeheader()

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

    def get_data(self) -> List[dict]:
        """
        Obtém todos os dados do arquivo csv informado.

        Returns:
            Retorna todos os dados como uma lista de objetos.

        Raises:
            FileExistsError se o arquivo não existir.
        """                
        with open(self.file_name) as csv_file:            
            csv_reader = DictReader(csv_file)                                   
            
            return list(csv_reader)