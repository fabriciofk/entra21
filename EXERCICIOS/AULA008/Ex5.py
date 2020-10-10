# --- Exercício 5  - Funções
# --- Escreva um programa para cadastro de pessoas e endereços:
# --- o programa deve solicitar os dados de pessoa utilizados na função do ex1
# --- o programa deve solicitar os dados de endereços utilizados na função do
#     ex2
# --- o programa deve passar o id obtido na função do ex1 para a função do ex2
# --- o programa deve mostrar ao final os dados de todos as pessoas cadastradas
#     com seus respectivos endereços utilizando as funções do ex3 e ex4
from funcoes.funcoes_ex8 import Ex1, Ex2, Ex3, Ex4


def show_header(title: str, character: str = '-') -> None:
    print(f'{title.upper():{character}^50}')


def show_footer(character: str = '-') -> None:
    print(f'\n{character:{character}^50}')


def show_menu(title: str, *args: str, character: str = '-') -> None:
    show_header(title, character)

    print(f'\n\t\tEscolha uma opção:')

    for option in args:
        print(f'\t\t{option}')

    show_footer()


def people_register() -> None:
    # Printing registration header
    show_header('Cadastro de Pessoa')

    while True:
        # Collecting person data
        print('\nDados Pessoais')

        name = input('\tDigite o nome: ')
        last_name = input('\tDigite o sobrenome: ')
        age = int(input('\tDigite a idade: '))

        # Adding the person to the list and extracting ID
        try:
            person_id = Ex1.add_person(name, last_name, age)
        except ValueError as err:
            print(err)
            break

        # Collecting address data
        print('\nEndereço')

        street = input('\tDigite o nome da rua: ')
        number = input('\tDigite o número da casa: ')
        complement = input('\tDigite um complemento: ')
        neighborhood = input('\tDigite o bairro: ')
        city = input('\tDigite a cidade: ')
        state = input('\tDigite o estado: ')

        # Adding the address to the list
        try:
            Ex2.add_address(person_id, street, number, complement,
                            neighborhood, city, state)
        except ValueError as err:
            print(err)
            break

        # Printing registration footer
        show_footer()

        register_option = input('Deseja continuar cadastrando? (S/N): ')

        if register_option.upper() == "N":
            break


def show_people_menu() -> None:
    while True:
        # Printing the show people menu
        show_menu('Listagem de Pessoas',
                  '1) Listar todas as pessoas',
                  '2) Listar pessoas por ID',
                  '3) Voltar ao menu principal')
        menu_option = input('Opção Escolhida: ')

        if menu_option == '3':
            break

        if menu_option == '1':
            show_header('Listando todas as pessoas')
            for person in Ex1.people_list:
                Ex3.show_person_by_id(person['id'])
                Ex4.show_address_by_id(person['id'])
        elif menu_option == '2':
            show_header('Listando pessoa pelo ID')
            person_id = int(input('Digite o ID da pessoa: '))

            Ex3.show_person_by_id(person_id)
            Ex4.show_address_by_id(person_id)
        else:
            print('Opção inválida.')

        show_footer()


def main():
    while True:
        # Printing the main menu
        show_menu('Sistema de Cadastro',
                  '1) Cadastrar pessoas',
                  '2) Listar pessoas',
                  '3) Sair')
        main_menu_option = input('Opção escolhida: ')

        # Loop Breaker
        if main_menu_option == '3':
            break

        if main_menu_option == '1':
            people_register()
        elif main_menu_option == '2':
            show_people_menu()
        else:
            print('Opção Inválida.')


if __name__ == '__main__':
    main()





