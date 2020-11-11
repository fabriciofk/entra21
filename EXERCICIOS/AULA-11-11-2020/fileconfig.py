from csv import DictWriter, DictReader


def save_data_into_file(file: str, field: str) -> None:
    pass

def save_data(file: str, data: object) -> None:
    fieldnames = []
    data_dictionary = data.__dict__()

    if file == 'pessoa.csv':
        fieldnames = ['id', 'nome', 'idade', 'cpf']
    elif file == 'conta.csv':
        fieldnames = ['id', 'num_conta', 'senha', 'agencia', 'banco', 'saldo']
    else:
        print('Arquivo não existe!')

    try:        
        with open(file, 'x', encoding='utf-8') as csvfile:
            csv_writer = DictWriter(csvfile, fieldnames=fieldnames)

            csv_writer.writeheader()
            csv_writer.writerow(data_dictionary)
    except FileExistsError:
        with open(file, 'a', encoding='utf-8') as csvfile:
            csv_writer = DictWriter(csvfile, fieldnames=fieldnames)
            csv_writer.writerow(data_dictionary)    
