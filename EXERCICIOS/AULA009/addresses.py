from csv import DictReader, DictWriter


# Ex2
def address_register(person_id: int,
                     street: str,
                     number: str,
                     complement: str,
                     neighborhood: str,
                     city: str,
                     state: str) -> None:
    """Register an address in the adresses list"""

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
    with open('pessoas.csv', 'a', encoding='utf-8') as csvfile:
        fieldnames = address.keys()
        writer = DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow(address)

    print('Endereço cadastrado com sucesso.')


# Ex4
def get_addresses() -> list:
    """Returns the addresses list"""
    addresses = []

    with open('pessoas.csv', 'r', encoding='utf-8') as csvfile:
        csv_reader = DictReader(csvfile)
        for line in csv_reader:
            addresses.append(line)

    print(addresses)
    return addresses


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
