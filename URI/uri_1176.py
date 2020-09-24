def fib(n):
    """Função para calcular o N-ésimo item na sequência de Fibonnaci"""
    v = [0, 1]

    if n > 1:
        for i in range(2, n + 1):
            f = v[i - 1] + v[i - 2]
            v.append(f)

    return v[n]


def main():
    # Quantidade de testes
    testes = int(input())

    # Repetindo para cada teste
    for _ in range(testes):

        n = int(input())
        f = fib(n)
        print(f'Fib({n}) = {f}')


if __name__ == '__main__':
    main()




