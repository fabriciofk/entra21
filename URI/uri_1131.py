opcao = None
quantidade = 0
vitorias_inter = 0
vitorias_gremio = 0
empates = 0
while opcao != '2':
    quantidade += 1
    inter, gremio = map(int, input().split())
    if inter > gremio:
        vitorias_inter += 1
    elif inter < gremio:
        vitorias_gremio += 1
    else:
        empates += 1
    print('Novo grenal (1-sim 2-nao)')
    opcao = input()

print(f'{quantidade} grenais')
print(f'Inter:{vitorias_inter}')
print(f'Gremio:{vitorias_gremio}')
print(f'Empates:{empates}')
if vitorias_inter > vitorias_gremio:
    print('Inter venceu mais')
elif vitorias_inter < vitorias_gremio:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')