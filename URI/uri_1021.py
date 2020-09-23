notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

n = float(input())

print('NOTAS:')
for nota in notas:
    qtd_nota = int(n / nota)
    n -= qtd_nota * nota
    print(f'{int(qtd_nota)} nota(s) de R$ {nota:.2f}')

print('MOEDAS:')
for moeda in moedas:
    qtd_moeda = int(round(n, 2) / moeda)
    n -= qtd_moeda * moeda
    print(f'{int(qtd_moeda)} moeda(s) de R$ {moeda:.2f}')



