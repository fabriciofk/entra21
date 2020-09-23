lista = []
while True:
    x, y = map(int, input().split())

    if x > y:
        lista.append('Decrescente')
    elif x < y:
        lista.append('Crescente')
    else:
        break

for i in lista:
    print(i)