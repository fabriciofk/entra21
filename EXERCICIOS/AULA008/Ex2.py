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
from custom_exceptions import InvalidAddress


# GLOBALS
addresses_list = []


def add_address(person_id: int,
                street: str,
                number: str,
                complement: str,
                neighborhood: str,
                city: str,
                state: str
                ) -> None:
    """Adds an address to the addresses list.

    Adds an address to the list if all fields are valid.

    Args:
        person_id: Person's id.
        street: Name of the street.
        number: Number of the house.
        complement: Additional information.
        neighborhood: Name of the neighborhood.
        city: Name of the city.
        state: Name of the state.

    Returns:
        None

    Raises:
        InvalidAddress: If there is an invalid field (None or '').
    """
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

    # Verifying invalid fields
    for value in address.values():
        if value == '' or value is None:
            raise InvalidAddress

    addresses_list.append(address)
    print('Endereço cadastrado com sucesso!')


def main() -> None:
    add_address(1, 'Rua sei lá', '123', 'Casa', 'Velha', 'Blumenau', 'SC')
    add_address(1, 'Rua sei lá', '123', 'Casa', '', 'Blumenau', 'SC')
    print(addresses_list)


if __name__ == '__main__':
    main()


