numeros_pares = []
for i in range(5):
    valor = int(input())
    if valor % 2 == 0:
        numeros_pares.append(valor)

print(f'{len(numeros_pares)} valores pares')