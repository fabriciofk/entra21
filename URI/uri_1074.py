n = int(input())

x = []

for i in range(n):
    valor = int(input())
    if valor == 0:
        x.append('NULL')
    else:
        if valor % 2 == 0:
            x.append('EVEN')
        elif valor % 2 != 0:
            x.append('ODD')

        if valor > 0:
            x[i] += ' POSITIVE'
        elif valor < 0:
            x[i] += ' NEGATIVE'

for valor in x:
    print(valor)