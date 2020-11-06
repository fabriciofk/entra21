from os import system, name 
from typing import Tuple


palavra = ''
chances = 0

def is_digit(letter: str) -> bool:
    """
        Recebe uma letra e verifica se ela é um dígito

        Attr
    """
    try:
        float(letter)
        return False
    except ValueError:                
        return True
    

def get_config() -> Tuple[str, int]:
    global palavra, chances
    with open('conf.cfg') as file:
        palavra = file.readline().strip()
        chances = int(file.readline())


def limpa_tela() -> None:
    # for windows 
    if name == 'nt': 
        system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else:
        system('clear')   


def has_repeated_letter(letra: str, tentativa_palavra: str) -> bool:
    return letra in tentativa_palavra


def verifica_fim_jogo(tentativa_palavra: str) -> bool:
    global palavra, chances

    if tentativa_palavra == palavra:
            print(f"Você ganhou com apenas {chances}!")
            return True
    
    if chances == 0:
        print("Você perdeu!")
        return True


def print_menu() -> None:
    while True:
        print('1 - Jogar')
        print('2 - Modificar as configurações')
        print('3 - Sair')
        opcao = input('Digite a opção escolhida: ')

        if opcao in ('1', '2', '3'):
            return opcao
        else:
            print('Opção inválida')

def jogar():  
    global palavra, chances 
    get_config()   

    letras_usadas = []
    while True:
        tentativa_palavra = ""
 
        limpa_tela()                    
        print("Número de chances: %d - tentativas:" % chances) # interpolação de string
        print(*letras_usadas) # imprime item por item do array
        print("\n")
        print(tentativa_palavra)
        for x in palavra:
            tentativa_palavra += x if x in letras_usadas else "_"
        print(tentativa_palavra + "\n\n")        
 
        fim_jogo = verifica_fim_jogo(tentativa_palavra)

        if fim_jogo:
            break

        while True:
            chute = input("Digite uma letra:")
            
            chute_valido = is_digit(chute)

            if not chute_valido:            
                print('Dígito inválido')
                continue

            letra_repetida = has_repeated_letter(chute, letras_usadas)        

            if letra_repetida:
                print('Letra repetida') 
            else:
                break                            

        letras_usadas.append(chute)

        if not chute in palavra:
            chances -= 1


def main() -> None:
    menu = print_menu()

    if menu == '1':
        jogar()
        
if __name__ == "__main__":
    main()