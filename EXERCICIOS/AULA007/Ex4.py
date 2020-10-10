# --- Exercício 4  - Funções
# --- Crie uma função que imprima um cabeçalho de acordo com uma variável de
#     nome da empresa (passada por parametro)
# --- A impressão deve ocorrer via multiplicação de strings
# --- A multiplicação deve ser feita com base em uma variável que contenha o
#     caracter a ser multiplicado
# --- Crie uma segunda função que imprima um rodapé utilizando a mesma técnica
# --- Crie uma chamada para as duas função, para exibir o resultado no console
def print_header_footer(message: str, character: str) -> None:
    length = len(message) + 10
    print(f'{message:{character}^{length}}')


def main() -> None:
    company_name = input('Digite o nome da empresa: ')
    header_character = input('Digite o caractere desejado para o cabeçalho: ')
    footer_message = input('Digite a mensagem exibida no rodapé: ')
    footer_character = input('Digite o caractere desejado para o rodapé: ')

    print('\nCabeçalho gerado:')
    print_header_footer(company_name, header_character)

    print('\nRodapé gerado:')
    print_header_footer(footer_message, footer_character)


if __name__ == '__main__':
    main()
