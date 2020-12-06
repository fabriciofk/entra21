import pathlib


lista_produtos = [
    {
        'nome': 'playstation 5',
        'valor': 4199.00
    },
    {
        'nome': 'iPhone X',
        'valor': 5949.15
    },
    {
        'nome': 'galaxy Z',
        'valor': 8109.00
    },
    {
        'nome': 'iPad 7',
        'valor': 3377.00
    }
]
    
def desconto(valor: float) -> float:
    if valor > 100 and valor <= 200:
        valor -= valor * .02
    elif valor > 200 and valor <= 500:
        valor -= valor * .05
    elif valor > 500:
        valor -= valor * .1    
    
    return valor


lista_produtos.sort(key=lambda k: k['nome'])
total_produtos = sum((produto['valor'] for produto in lista_produtos))
maior = max(lista_produtos, key=lambda k: k['valor'])

print(f'Lista ordenada: {lista_produtos}')
print(f'Total dos produtos: {total_produtos:.2f}')
desconto = desconto(total_produtos)
print(f'Valor com desconto: {desconto:.2f}')
print(f'Produto com o maior valor: {maior}')


# Salvando em arquivos
current_path = f'{pathlib.Path(__file__).parent.absolute()}\\arquivo.txt'

try:
    with open(current_path, 'w', encoding='utf8') as arquivo:        
        arquivo.write(f'Produtos: {lista_produtos}\n')
        arquivo.write(f'Total dos produtos: {total_produtos:.2f}\n')
        arquivo.write(f'Valor com desconto: {desconto:.2f}\n')
        arquivo.write(f'Produto com o maior valor: {maior}\n')
except Exception as err:
    print(err)
