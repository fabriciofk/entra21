valor = 0

for i in range(2):
    _, quantidade, preco = input().split()
    quantidade = int(quantidade)
    preco = float(preco)
    valor += quantidade * preco

print(f"VALOR A PAGAR: R$ {valor:.2f}")
