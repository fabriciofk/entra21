n = int(input())

for _ in range(n):

    x, y = map(int, input().split())

    flag = 0
    soma = 0

    while flag < y:

        if x % 2 != 0:
            soma += x
            flag += 1

        x += 1

    print(soma)

