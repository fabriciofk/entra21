indice = None
maior_valor = 0
for i in range(100):
    valor = int(input())
    if i == 0:
        indice = i + 1
        maior_valor = valor
    elif maior_valor < valor:
        indice = i + 1
        maior_valor = valor

print(maior_valor)
print(indice)