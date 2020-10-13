# GLOBALS
addresses_list = []


# Ex2
def address_register(person_id: int,
                     street: str,
                     number: str,
                     complement: str,
                     neighborhood: str,
                     city: str,
                     state: str) -> None:
    """Register an address in the adresses list"""
    global addresses_list

    # Validating parameters
    for key, value in locals().items():
        if value is None or value == '':
            raise ValueError('Erro: Dados de endereço inválidos.')

    address = {
        'person_id': person_id,
        'street': street,
        'number': number,
        'complement': complement,
        'neighborhood': neighborhood,
        'city': city,
        'state': state
    }

    # Adding the address to the list
    addresses_list.append(address)
    print('Endereço cadastrado com sucesso.')


# Ex4
def get_addresses() -> list:
    """Returns the addresses list"""
    return addresses_list


# Ex4
def get_address_by_id(person_id):
    """Returns an address from the addresses list by the person's ID"""
    addresses = get_addresses()

    if addresses:
        for address in addresses:
            if address['person_id'] == person_id:
                return address

    raise IndexError(f'A pessoa com o ID({person_id}) não possui um endereço '
                     f'cadastrado.')
