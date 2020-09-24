notas = [100, 50, 20, 10, 5, 2, 1]

valor = int(input())

print(f'{valor}')
for nota in notas:
    qtd_nota, valor = divmod(valor, nota)

    # Formatando a nota (Substituindo . por ,)
    nota_formatada = f'{nota:.2f}'.replace('.', ',')

    print(f"{qtd_nota} nota(s) de R$ {nota_formatada}")
