from functools import reduce
from typing import List
import operator


# 1)
def calcula_comissao(valor_venda: float) -> float:
    comissao = 0
    if 0 < valor_venda < 30_000:
        comissao = 0
    elif 30_000 <= valor_venda < 50_000:
        comissao = 1.5
    elif 50_000 <= valor_venda < 100_000:
        comissao = 2.5
    elif valor_venda >= 100_000:
        comissao = 3.5
    return comissao


def valor_total(valor: float, comissao: float) -> float:
    valor_tot = valor + (valor * (comissao / 100))
    return valor_tot


valor = float(input("Digite o valor da venda: "))
print(valor_total(valor, calcula_comissao(valor)))


# 2)
def calcula_media(*args: float) -> float:
    med = round(sum(args) / len(args), 2)
    return med


def situacao(media: float) -> str:
    if 0 < media < 5:
        return f"Média {media} | Situação: Reprovado"
    elif 5 <= media < 6.5:
        return f"Média {media} | Situação: Recuperação"
    elif 6.5 <= media < 9:
        return f"Média {media} | Situação: Aprovado"
    elif media >= 9:
        return f"Média {media} | Situação: Aprovado"
    else:
        return f"Média Inválida"


def cad_notas() -> list:
    notas = []
    for i in range(4):
        notas.append(float(input("Digite uma nota: ")))
    return notas


notas = cad_notas()
media = calcula_media(*notas)
print(situacao(media))


# 3)
def soma(*args: float) -> float:
    return sum(args)


def subtracao(*args: float) -> float:
    return reduce(operator.sub, args)


def multiplicacao(*args: float) -> float:
    return reduce(operator.mul, args)


def divisao(*args: float) -> float:
    try:
        return reduce(operator.floordiv, args)
    except ZeroDivisionError:
        return "Erro! Divisão por zero!"


def media(*args: float) -> float:
    med: float = round(sum(args) / len(args), 2)
    return med


def cad_numeros(quantidade) -> List[float]:
    lista: List[float] = []
    for i in range(quantidade):
        lista.append(float(input("Digite um número: ")))
    return lista


opcao = input("""
Escolha uma opção: 
A) Soma
B) Subtração
C) Média
D) Multiplicação
E) Divisão

Opção escolhida:
""")
numeros: List[float] = []
if opcao == 'A' or opcao == 'a':
    numeros = cad_numeros(2).copy()
    resultado = soma(*numeros)
    print(f"Resultado da Soma: {resultado}")
elif opcao == 'B' or opcao == 'b':
    numeros = cad_numeros(2).copy()
    resultado = subtracao(*numeros)
    print(f"Resultado da Subtração: {resultado}")
elif opcao == 'C' or opcao == 'c':
    numeros = cad_numeros(4).copy()
    resultado = media(*numeros)
    print(f"Resultado da Média: {resultado}")
elif opcao == 'D' or opcao == 'd':
    numeros = cad_numeros(2).copy()
    resultado = multiplicacao(*numeros)
    print(f"Resultado da Multiplicação: {resultado}")
elif opcao == 'E' or opcao == 'e':
    numeros = cad_numeros(2).copy()
    resultado = divisao(*numeros)
    print(f"Resultado da Divisão: {resultado}")
else:
    print("Opção Inválida!!")


# 4)
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

if a < (b + c) and b < (a + c) and c < (a + b):
    if a == b and a == c:
        print("Triângulo Esquilátero")
    elif a == b or a == c or b == c:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Não é um triângulo")

