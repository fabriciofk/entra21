matriz = []
linha = []

li = int(input())
op = input()

for i in range(12):
    for j in range(12):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha.copy())  # linha[:]
    linha.clear()

resultado = None

if op == 'S':
    resultado = round(sum(matriz[li]), 1)
elif op == 'M':
    resultado = round(sum(matriz[li]) / len(matriz[li]), 1)

print(resultado)



