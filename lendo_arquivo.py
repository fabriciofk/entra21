import os

current_path = f'{os.getcwd()}\\arquivo.txt'
print(current_path)

with open(current_path, 'w+', encoding='utf8') as arquivo:        
    arquivo.write('Nome: William\n')
    arquivo.write('Idade: 20\n')
    arquivo.write('Tenho 2 cachorros e 1 gato\n')
    arquivo.seek(0,0)
    # next(arquivo)
    # print(arquivo.readline())
    for indice, linha in enumerate(arquivo):
        if indice == 1:
            print(linha.strip())

    