n = int(input())
lista = []
for i in range(n):
    valor = int(input())
    if 10 <= valor <= 20:
        lista.append(valor)

valor_in = len(lista)
valor_out = n - len(lista)

print(f'{valor_in} in')
print(f'{valor_out} out')