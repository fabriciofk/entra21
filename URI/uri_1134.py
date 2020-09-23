tipo_combustivel = None
contadores = {
    'alcool': 0,
    'gasolina': 0,
    'diesel': 0
}
while tipo_combustivel != '4':
    tipo_combustivel = input()
    if tipo_combustivel == '1':
        contadores['alcool'] += 1
    elif tipo_combustivel == '2':
        contadores['gasolina'] += 1
    elif tipo_combustivel == '3':
        contadores['diesel'] += 1

print('MUITO OBRIGADO')
print(f'Alcool: {contadores["alcool"]}')
print(f'Gasolina: {contadores["gasolina"]}')
print(f'Diesel: {contadores["diesel"]}')