# --- Exercício 1  - Funções
# --- Escreva uma função para cadastro de pessoa:
#     a função deve receber três parâmetros, nome, sobrenome e idade
# --- a função deve salvar os dados da pessoa em uma lista com escopo
#     global
# --- a função deve permitir o cadastro apenas de pessoas com idade igual ou
#     superior a 18 anos
# --- a função deve retornar uma mensagem caso a idade informada seja menor
#     que 18
# --- caso a pessoa tenha sido cadastrada com sucesso deve ser retornado
#     um id
# --- A função deve ser salva em um arquivo diferente do arquivo principal onde
#     será chamada
person_count = 2
people_list = [
    {
        'id': 1,
        'name': 'William',
        'last_name': 'Círico',
        'age': 20
    },
    {
        'id': 2,
        'name': 'Patrícia',
        'last_name': 'Carvalho',
        'age': 23
    },
]


def add_person(name: str, last_name: str, age: int) -> int:
    global person_count, people_list
    if age >= 18:
        person_count += 1

        person = {
            'id': person_count,
            'name': name,
            'last_name': last_name,
            'age': age
        }
        people_list.append(person)
        print(people_list)
        print('Pessoa cadastrada com sucesso!')

        return person_count
    else:
        raise ValueError('Falha ao cadastrar: Idade menor do que 18 anos.')


def main() -> None:
    print(add_person('William', 'Círico', 20))
    print(people_list)

    add_person('Joana', 'Souza', 14)
    print(people_list)


if __name__ == '__main__':
    main()


