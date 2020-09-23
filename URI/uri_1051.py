salario = float(input())

ir = 0
if 2000 < salario <= 3000:
    salario -= 2000
    ir += salario * .08
elif 3000 < salario <= 4500:
    salario -= 3000
    ir += 1000 * .08
    ir += salario * .18
elif salario > 4500:
    salario -= 4500
    ir += 1000 * .08
    ir += 1500 * .18
    ir += salario * .28

if ir:
    print(f'R$ {ir:.2f}')
else:
    print('Isento')