valor = int(input())
valor2 = valor
n100 = valor2 // 100
valor2 -= n100 * 100
n50 = valor2 // 50
valor2 -= n50 * 50
n20 = valor2 // 20
valor2 -= n20 * 20
n10 = valor2 // 10
valor2 -= n10 * 10
n5 = valor2 // 5
valor2 -= n5 * 5
n2 = valor2 // 2
valor2 -= n2 * 2
n1 = valor2

print(f"{valor}")
print(f"{n100} nota(s) de R$ 100,00")
print(f"{n50} nota(s) de R$ 50,00")
print(f"{n20} nota(s) de R$ 20,00")
print(f"{n10} nota(s) de R$ 10,00")
print(f"{n5} nota(s) de R$ 5,00")
print(f"{n2} nota(s) de R$ 2,00")
print(f"{n1} nota(s) de R$ 1,00")