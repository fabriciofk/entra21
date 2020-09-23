n = [int(input())]

for i in range(1, 10):
    valor = n[i - 1] * 2
    n.append(valor)

for i, valor in enumerate(n):
    print(f'N[{i}] = {valor}')

