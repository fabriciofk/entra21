opcao = 0
flag = 0

while opcao != 2:

    opcao = 0
    soma = 0
    flag = 0

    while flag < 2:

        while True:
            nota = float(input())

            if 0 <= nota <= 10:
                flag += 1
                soma += nota
                break
            else:
                print('nota invalida')

    media = soma / 2
    print(f'media = {media:.2f}')

    while opcao < 1 or opcao > 2:
        print('novo calculo (1-sim 2-nao)')
        opcao = int(input())



