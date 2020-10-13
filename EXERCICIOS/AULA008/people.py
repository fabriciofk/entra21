# GLOBALS
people_list = []
person_count = 0


# Ex1
def person_register(name: str, last_name: str, age: int) -> int:
    """Register a person in the people list"""
    global people_list, person_count

    # Validating parameters
    for key, value in locals().items():
        if value is None or value == '':
            raise ValueError('Erro: Dados da pessoa são inválidos.')

    # Age validation
    if age < 18:
        raise ValueError('Erro: Menor de idade.')

    # Incrementing person's ID
    person_count += 1

    person = {
        'id': person_count,
        'name': name,
        'last_name': last_name,
        'age': age
    }

    # Adding the person to the list
    people_list.append(person)
    print('Pessoa cadastrada com sucesso.')

    return person_count


# Ex3
def get_people() -> list:
    """Returns the people list"""
    return people_list


# Ex3
def get_person_by_id(person_id: int) -> dict:
    """Returns a person from the people list by its ID"""
    people_list = get_people()

    if people_list:
        for person in people_list:
            if person['id'] == person_id:
                return person

    raise IndexError(f'Pessoa com o ID({person_id}) não está cadastrada.')
