alfabeto = [chr(i) for i in range(ord('a'), ord('z') + 1)]


def retiraVogais(vogais: tuple) -> tuple:
    vogais_retiradas = []
    for indice, letra in enumerate(alfabeto):
        if letra in vogais:
            vogais_retiradas.append(alfabeto.pop(indice))
    
    return tuple(vogais_retiradas)


vogais_retiradas = retiraVogais(('a', 'e', 'i', 'o', 'u'))


def retira_nome(nome: str) -> set:
    nome_retirado = ''
    for letra_nome in nome:
        if letra_nome in alfabeto:
            indice = alfabeto.index(letra_nome)
            nome_retirado += alfabeto[indice]
        else:
            indice = vogais_retiradas.index(letra_nome)
            nome_retirado += vogais_retiradas[indice]

    conjunto = {nome_retirado}        

    return conjunto


conjunto = retira_nome('william')
conjunto.add(20)
conjunto.add('Mochileiro das Galáxias')
print(conjunto)