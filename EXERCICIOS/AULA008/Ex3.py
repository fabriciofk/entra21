# --- Exercício 3  - Funções
# --- Escreva uma função para listar pessoas cadastradas:
# --- a função deve retornar todas as pessoas cadastradas na função do ex1
# --- Escreva uma função para exibir uma pessoa específica:
#     a função deve retornar uma pessoa cadastrada na função do ex1 filtrando
#     por id
import Ex1


def show_people() -> None:
    """Prints everyone in the people list"""
    if Ex1.people_list:
        print('Listando pessoas:\n')

        for person in Ex1.people_list:
            print(f'\tPessoa {person["id"]}:\n')
            print(f'\t\tNome: {person["name"]}')
            print(f'\t\tSobrenome: {person["last_name"]}')
            print(f'\t\tIdade: {person["age"]}\n')
    else:
        print('Nenhuma pessoa cadastrada.')


def show_person_by_id(person_id: int) -> None:
    """Prints a person data by its ID"""
    for person in Ex1.people_list:
        if person_id == person['id']:
            print(f'Pessoa {person["id"]}\n')
            print(f'\tNome: {person["name"]}')
            print(f'\tSobrenome: {person["last_name"]}')
            print(f'\tIdade: {person["age"]}\n')

            return

    print('Não existe uma pessoa com o ID informado.')


def main() -> None:
    show_people()
    show_person_by_id(2)


if __name__ == '__main__':
    main()


