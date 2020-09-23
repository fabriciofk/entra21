lista = []
while True:
    m, n = map(int, input().split())
    if not (m <= 0 or n <= 0):
        aux = None

        if m > n:
            aux = m
            m = n
            n = aux

        lista.append((m, n))
    else:
        break

for valor in lista:
    m, n = valor
    soma = 0
    for num in range(m, n + 1):
        soma += num
        print(num, end=" ")
    print(f'Sum={soma}')