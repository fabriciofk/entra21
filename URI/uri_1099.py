n = int(input())

soma_impares = []

for i in range(n):
    x, y = map(int, input().split())

    aux = None
    if y < x:
        aux = x
        x = y
        y = aux

    soma = 0

    for j in range(x + 1, y):
        if j % 2 != 0:
            soma += j

    soma_impares.append(soma)

for valor in soma_impares:
    print(valor)