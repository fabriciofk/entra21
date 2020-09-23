t = int(input())

for _ in range(t):
    entradas = input().split()

    pa = int(entradas[0])
    pb = int(entradas[1])
    g1 = float(entradas[2]) / 100
    g2 = float(entradas[3]) / 100

    anos = 0

    while True:
        pa += int(pa * g1)
        pb += int(pb * g2)
        anos += 1

        if pa > pb or anos > 100:
            break

    if anos <= 100:
        print(f'{anos} anos.')
    else:
        print('Mais de 1 seculo.')