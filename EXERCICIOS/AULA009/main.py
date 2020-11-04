from people import person_register, get_person_by_id, get_people
from addresses import address_register, get_address_by_id
import addresses


# Ex5
def main() -> None:
    while True:
        # Collecting person data
        print('Cadastrando pessoa')
        name = input('Nome: ')
        last_name = input('Sobrenome: ')
        age = int(input('Idade: '))

        # Registering person
        try:
            person_id = person_register(name, last_name, age)
        except Exception as err:
            print(err)
            continue

        # Collecting address data
        print('Cadastrando endereço')
        street = input('Rua: ')
        number = input('Número: ')
        complement = input('Complemento: ')
        neighborhood = input('Bairro: ')
        city = input('Cidade: ')
        state = input('Estado: ')

        # Registering address
        try:
            address_register(person_id,
                             street,
                             number,
                             complement,
                             neighborhood,
                             city,
                             state)
        except Exception as err:
            print(err)

        # Loop breaker
        loop_continue = input('Deseja continuar cadastrando? (S/N): ')

        if loop_continue.upper() == 'N':
            break

    # Printing registered people and addresses
    print('PESSOAS CADASTRADAS\n')
    people_list = get_people()

    for person in people_list:
        person_dict = get_person_by_id(person['id'])

        print(f'Pessoa {person_dict["id"]}')
        print(f'\tNome: {person_dict["name"]}')
        print(f'\tSobrenome: {person_dict["last_name"]}')
        print(f'\tIdade: {person_dict["age"]}\n')

        try:
            address_dict = get_address_by_id(person['id'])

            print(f'Endereço do(a) {person_dict["name"]}')
            print(f'\tRua: {address_dict["street"]}')
            print(f'\tNúmero: {address_dict["number"]}')
            print(f'\tComplemento: {address_dict["complement"]}')
            print(f'\tBairro: {address_dict["neighborhood"]}')
            print(f'\tCidade: {address_dict["city"]}')
            print(f'\tEstado: {address_dict["state"]}\n')
        except IndexError as err:
            print(err)


if __name__ == '__main__':
    main()
