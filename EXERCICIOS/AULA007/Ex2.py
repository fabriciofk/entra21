# --- Exercício 2  - Funções
# --- Escreva uma função que leia dois números do console
# --- Armazene cada número em uma variável
# --- Realize a divisão entre os dois números e armazene o resultado em uma
#     terceira variável
# --- Imprima o resultado e uma mensagem usando f-string
def division(num1: float, num2: float) -> float:
    try:
        quotient = num1 / num2
        return quotient
    except ZeroDivisionError:
        print('\nNão é possível dividir por zero')


def main() -> None:
    number1 = float(input('Digite o primeiro número: '))
    number2 = float(input('Digite o segundo número: '))

    result = division(number1, number2)

    if result is not None:
        print(f'\n{number1} / {number2} = {result:.2f}')


if __name__ == '__main__':
    main()
