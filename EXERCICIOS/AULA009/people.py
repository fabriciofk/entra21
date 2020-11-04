from csv import DictWriter, DictReader


# Ex1
def person_register(name: str, last_name: str, age: int) -> int:
    """Register a person in the people list"""

    # Validating parameters
    for key, value in locals().items():
        if value is None or value == '':
            raise ValueError('Erro: Dados da pessoa são inválidos.')

    # Age validation
    if age < 18:
        raise ValueError('Erro: Menor de idade.')

    # Incrementing person's ID
    try:
        people_list = get_people()
        person_id = int(people_list[-1]['id']) + 1
    except FileNotFoundError:
        person_id = 1

    person = {
        'id': person_id,
        'name': name,
        'last_name': last_name,
        'age': age
    }

    # Adding the person to the file
    fieldnames = person.keys()

    try:
        with open('data/people.csv', 'x', encoding='utf-8') as csvfile:
            csv_writer = DictWriter(csvfile, fieldnames=fieldnames)

            csv_writer.writeheader()
            csv_writer.writerow(person)
    except FileExistsError:
        with open('data/people.csv', 'a', encoding='utf-8') as csvfile:
            csv_writer = DictWriter(csvfile, fieldnames=fieldnames)

            csv_writer.writerow(person)

    print('Pessoa cadastrada com sucesso.')

    return person_id


# Ex3
def get_people() -> list:
    """Returns the people list"""
    with open('data/people.csv', 'r', encoding='utf-8') as csvfile:
        csv_reader = DictReader(csvfile)
        return list(csv_reader)


# Ex3
def get_person_by_id(person_id: str) -> dict:
    """Returns a person from the people list by its ID"""
    people_list = get_people()

    for person in people_list:
        if person['id'] == person_id:
            return person

    raise IndexError(f'Pessoa com o ID({person_id}) não está cadastrada.')
