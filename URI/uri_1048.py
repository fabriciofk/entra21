salario = float(input())
reajuste = 0
if 0 < salario <= 400:
    reajuste = 15
elif 400 < salario <= 800:
    reajuste = 12
elif 800 < salario <= 1200:
    reajuste = 10
elif 1200 < salario <= 2000:
    reajuste = 7
elif salario > 2000:
    reajuste = 4

reajuste_ganho = salario * (reajuste / 100)
novo_salario = salario + reajuste_ganho

print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste_ganho:.2f}")
print(f"Em percentual: {reajuste} %")