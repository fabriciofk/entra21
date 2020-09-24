valores_positivos = []

for i in range(6):
    valor = float(input())
    if valor > 0:
        valores_positivos.append(valor)

print(f'{len(valores_positivos)} valores positivos')