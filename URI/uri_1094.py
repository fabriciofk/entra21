n = int(input())

total = 0
tc = 0
tr = 0
ts = 0

for i in range(n):

    qnt, tipo = input().split()

    qnt = int(qnt)
    total += qnt

    if tipo == 'C':
        tc += qnt
    elif tipo == 'R':
        tr += qnt
    elif tipo == 'S':
        ts += qnt

pc = (tc * 100) / total
pr = (tr * 100) / total
ps = (ts * 100) / total

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {tc}')
print(f'Total de ratos: {tr}')
print(f'Total de sapos: {ts}')
print(f'Percentual de coelhos: {pc:.2f} %')
print(f'Percentual de ratos: {pr:.2f} %')
print(f'Percentual de sapos: {ps:.2f} %')