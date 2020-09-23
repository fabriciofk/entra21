n = []

for i in range(20):
    n.append(input())

inicio = 0
fim = len(n) - 1

while inicio < fim:

    aux = n[inicio]
    n[inicio] = n[fim]
    n[fim] = aux

    inicio += 1
    fim -= 1

for i, valor in enumerate(n):
    print(f'N[{i}] = {valor}')




