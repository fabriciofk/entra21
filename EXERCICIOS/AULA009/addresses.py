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

    # Adding the address to the file
    fieldnames = address.keys()

    try:
        with open('data/addresses.csv', 'x', encoding='utf-8') as csvfile:
            csv_writer = DictWriter(csvfile, fieldnames=fieldnames)

            csv_writer.writeheader()
            csv_writer.writerow(address)
    except FileExistsError:
        with open('data/addresses.csv', 'a', encoding='utf-8') as csvfile:
            csv_writer = DictWriter(csvfile, fieldnames=fieldnames)

            csv_writer.writerow(address)

    print('Endereço cadastrado com sucesso.')


# Ex4
def get_addresses() -> list:
    """Returns the addresses list"""
    with open('data/addresses.csv', 'r', encoding='utf-8') as csvfile:
        csv_reader = DictReader(csvfile)
        return list(csv_reader)


# Ex4
def get_address_by_id(person_id: str) -> dict:
    """Returns an address from the addresses list by the person's ID"""
    addresses = get_addresses()

    for address in addresses:
        if address['person_id'] == person_id:
            return address

    raise IndexError(f'A pessoa com o ID({person_id}) não possui um endereço '
                     f'cadastrado.')
