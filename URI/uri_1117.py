flag_valido = 0
soma = 0
while flag_valido <= 2:
    nota = float(input())

    if 0 <= nota <= 10:
        flag_valido += 1
        soma += nota
        if flag_valido == 2:
            media = soma / 2
            print(f'media = {media}')
    else:
        print('nota invalida')