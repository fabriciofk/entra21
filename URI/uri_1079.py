n = int(input())

conjunto_notas = []

for conjunto in range(n):
    conjunto_notas.append([])
    n1, n2, n3 = map(float, input().split())
    conjunto_notas[conjunto].append(n1)
    conjunto_notas[conjunto].append(n2)
    conjunto_notas[conjunto].append(n3)

for conjunto in conjunto_notas:
    soma = conjunto[0] * 2 + conjunto[1] * 3 + conjunto[2] * 5
    media = round(soma / 10, 1)
    print(media)