a = []
pos = []

for i in range(100):

    valor = float(input())

    if valor <= 10:
        pos.append(i)

    a.append(valor)

for i in pos:
    print(f'A[{i}] = {a[i]:.1f}')
