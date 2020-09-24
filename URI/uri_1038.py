precos = [4, 4.5, 5, 2, 1]
cod, qtd = map(int, input().split())

total = precos[cod - 1] * qtd

print(f"Total: R$ {total:.2f}")
