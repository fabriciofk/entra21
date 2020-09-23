cod, qtd = map(lambda x: int(x), input().split(" "))

total = 0
if cod == 1:
    total = qtd * 4
elif cod == 2:
    total = qtd * 4.5
elif cod == 3:
    total = qtd * 5
elif cod == 4:
    total = qtd * 2
elif cod == 5:
    total = qtd * 1.5

print(f"Total: R$ {total:.2f}")