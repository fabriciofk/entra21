def mostra_impar(lista):
    for j, num in enumerate(lista):
        print(f'impar[{j}] = {num}')
    lista.clear()


def mostra_par(lista):
    for j, num in enumerate(lista):
        print(f'par[{j}] = {num}')
    lista.clear()


pares = []
impares = []

for i in range(15):

    valor = int(input())

    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

    if len(pares) >= 5:
        mostra_par(pares)

    if len(impares) >= 5:
        mostra_impar(impares)

mostra_impar(impares)
mostra_par(pares)


