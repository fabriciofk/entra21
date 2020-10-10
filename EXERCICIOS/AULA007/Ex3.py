# --- Exercício 3  - Funções
# --- Crie uma função que leia três números float
# --- Armazene cada valor lido em uma variável
# --- Calcule a média entre os três números e armazene em uma quarta variável
# --- Imprima a média e uma mensagem usando f-string (módulo 3)
def avg(*args: float) -> float:
    numbers_sum = sum(args)
    numbers_quantity = len(args)
    average = numbers_sum / numbers_quantity

    return average


def main() -> None:
    number1 = float(input('Digite o primeiro número: '))
    number2 = float(input('Digite o segundo número: '))
    number3 = float(input('Digite o terceiro número: '))

    average = avg(number1, number2, number3)

    print(f'\nMédia = {average:.2f}')


if __name__ == '__main__':
    main()
