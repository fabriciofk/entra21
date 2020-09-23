while True:

    x = int(input())

    if x == 0:
        break
    else:
        flag = 0
        soma = 0

        while flag < 5:

            if x % 2 == 0:
                soma += x
                flag += 1

            x += 1

        print(soma)