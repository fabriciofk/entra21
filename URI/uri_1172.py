x = []

for i in range(10):
    num = int(input())

    if num <= 0:
        num = 1

    x.append(num)

for i, valor in enumerate(x):
    print(f'X[{i}] = {valor}')
