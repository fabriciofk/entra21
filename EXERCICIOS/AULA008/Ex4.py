# --- Exercício 4  - Funções
# --- Escreva uma função para listar endereços cadastrados:
# --- a função deve retornar todos os endereços cadastrados na função do ex2
# --- Escreva uma função para exibir um endereço específico:
#     a função deve retornar um endereço cadastrado na função do ex2 filtrando
#     por id da pessoa
import Ex1
import Ex2


def show_addresses() -> None:
    """Prints all the adresses in the adresses list"""
    if Ex2.addresses_list:
        print('Listando Endereços\n')

        for address in Ex2.addresses_list:
            print(f'\tID Pessoa: {address["person_id"]}')
            print(f'\tRua: {address["street"]}')
            print(f'\tNúmero: {address["number"]}')
            print(f'\tComplemento: {address["complement"]}')
            print(f'\tBairro: {address["neighborhood"]}')
            print(f'\tCidade: {address["city"]}')
            print(f'\tEstado: {address["state"]}\n')
    else:
        print('Nenhum endereço cadastrado.')


def show_address_by_id(person_id: int) -> None:
    """Prints a single address by the person's ID"""
    for address in Ex2.addresses_list:
        if person_id == address['person_id']:
            person_name = Ex1.people_list[person_id - 1]["name"]

            print(f'Listando endereço do(a) {person_name}\n')

            print(f'\tRua: {address["street"]}')
            print(f'\tNúmero: {address["number"]}')
            print(f'\tComplemento: {address["complement"]}')
            print(f'\tBairro: {address["neighborhood"]}')
            print(f'\tCidade: {address["city"]}')
            print(f'\tEstado: {address["state"]}\n')

            return

    print('Não existe um endereço cadastrado para a pessoa informada.')


def main() -> None:
    show_addresses()
    show_address_by_id(2)
    show_address_by_id(3)


if __name__ == '__main__':
    main()
