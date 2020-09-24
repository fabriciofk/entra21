x = float(input())

n = [x]

for i in range(1, 100):
    n.append(n[i - 1] / 2)

for i, valor in enumerate(n):
    print(f'N[{i}] = {valor:.4f}')