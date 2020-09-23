numeros_positivos = []
for i in range(6):
    valor = float(input())
    if valor > 0:
        numeros_positivos.append(valor)

media = round(sum(numeros_positivos) / len(numeros_positivos), 1)
print(f'{len(numeros_positivos)} valores positivos')
print(media)