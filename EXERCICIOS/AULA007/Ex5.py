# --- Exercício 5 - Funções
# --- Crie uma função para calculo de raiz
# --- A função deve ter uma variável que determine qual é o indice da
#     raiz(raiz quadrada, raiz cubica...)
# --- Leia um número do console, armazene em uma variável e passe para a função
# --- Realize o calculo da raiz e armazene em uma segunda variável e retorne
# --- Imprima o resultado e uma mensagem usando f-string, fora da função
def root_calculator(rooting: float, index: int) -> float:
    return rooting ** (1 / index)


def main() -> None:
    rooting = float(input('Digite o radicando: '))
    index = int(input('Digite o índice: '))

    root = root_calculator(rooting, index)
    print(f'\n{index}√{rooting} = {root}')


if __name__ == '__main__':
    main()
