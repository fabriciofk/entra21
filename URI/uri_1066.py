numeros_pares = []
numeros_impares = []
numeros_positivos = []
numeros_negativos = []
for i in range(5):
    valor = int(input())
    if valor > 0:
        numeros_positivos.append(valor)
    if valor < 0:
        numeros_negativos.append(valor)
    if valor % 2 != 0:
        numeros_impares.append(valor)
    if valor % 2 == 0:
        numeros_pares.append(valor)

print(f'{len(numeros_pares)} valor(es) par(es)')
print(f'{len(numeros_impares)} valor(es) impar(es)')
print(f'{len(numeros_positivos)} valor(es) positivo(s)')
print(f'{len(numeros_negativos)} valor(es) negativo(s)')