# --- Exercício 2  - Funções
# --- Escreva uma função para cadastro de endereço:
# --- a função deve receber sete parâmetros, id da pessoa, rua, numero,
#     complemento, bairro, cidade e estado
# --- a função deve salvar os dados de endereço em uma lista com escopo global
# --- a função deve permitir o cadastro apenas de endereços com todos os dados
#     preenchidos
# --- a função deve retornar uma mensagem ao final de acordo com a situação
# --- A função deve ser salva em um arquivo diferente do arquivo principal onde
#     será chamada
addresses_list = [
        {
            'person_id': 1,
            'street': 'Sei lá',
            'number': '123',
            'complement': 'Casa',
            'neighborhood': 'Velha',
            'city': 'Blumenau',
            'state': 'SC'
        },
        {
            'person_id': 2,
            'street': 'José Reuter',
            'number': '1234',
            'complement': 'Casa',
            'neighborhood': 'Velha',
            'city': 'Blumenau',
            'state': 'SC'
        }
]


def add_address(person_id: int,
                street: str,
                number: str,
                complement: str,
                neighborhood: str,
                city: str,
                state: str) -> None:
    global addresses_list

    address = {
        'person_id': person_id,
        'street': street,
        'number': number,
        'complement': complement,
        'neighborhood': neighborhood,
        'city': city,
        'state': state
    }

    flag = False

    for index, value in address.items():
        if value == '' or value is None:
            flag = True
            break

    if not flag:
        addresses_list.append(address)
        print('Endereço cadastrado com sucesso!')
    else:
        raise ValueError('Falha ao cadastrar: Dados de endereço inválidos.')


def main() -> None:
    add_address(1, 'Rua sei lá', '123', 'Casa', 'Velha', 'Blumenau', 'SC')
    print(addresses_list)


if __name__ == '__main__':
    main()


