testes = int(input())

for teste in range(testes):

    x = int(input())
    flag = False

    for num in range(2, x):
        if x % num == 0:
            flag = True
            break

    if flag:
        print(f'{x} nao eh primo')
    else:
        print(f'{x} eh primo')


