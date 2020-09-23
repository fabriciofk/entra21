testes = int(input())

for teste in range(testes):

    x = int(input())
    soma = 0

    for num in range(x - 1, 0, -1):
        if x % num == 0:
            soma += num

    if soma == x:
        print(f'{x} eh perfeito')
    else:
        print(f'{x} nao eh perfeito')