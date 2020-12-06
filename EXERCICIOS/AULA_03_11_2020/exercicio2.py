def cadastrar_notas() -> list:
    notas = []

    for i in range(3):
        nota = float(input(f'Digite a {i+1} nota: '))
        notas.append(nota)        
 
    return notas


def calcular_media(lista_notas: list) -> float:     
    media = sum(lista_notas) / len(lista_notas)
    
    return media


notas = cadastrar_notas()
print(f'Média: {calcular_media(notas):.2f}')