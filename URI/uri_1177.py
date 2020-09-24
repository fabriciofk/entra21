n = []

t = int(input())
flag = False

while True:
    for i in range(t):
        if len(n) < 1000:
            n.append(i)
        else:
            flag = True
            break

    if flag:
        break

for i, valor in enumerate(n):
    print(f'N[{i}] = {valor}')

