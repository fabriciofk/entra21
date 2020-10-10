# --- Exercício 1  - Funções - 1
# --- Escreva uma função que imprima um cabeçalho
# --- O cabeçalho deve ser escrito usando a multiplicação de carácter
# --- O cabeçalho deve conter o nome de uma empresa, que será uma variável
# --- Realize a chamada da função na ultima linha do seu programa
def print_header(company_name: str) -> None:
    dash_quantity = len(company_name) + 10
    print(f'{company_name:-^{dash_quantity}}')


def main() -> None:
    company_name = input('Digite o nome da empresa: ')

    print('\nCabeçalho gerado:\n')
    print_header(company_name)


if __name__ == '__main__':
    main()
