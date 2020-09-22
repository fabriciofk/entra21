pecas = []

for i in range(2):
    string = input()
    pecas.append(string.split(" "))

valor = 0
for peca in pecas:
    valor += int(peca[1]) * float(peca[2])

print(f"VALOR A PAGAR: R$ {valor:.2f}")