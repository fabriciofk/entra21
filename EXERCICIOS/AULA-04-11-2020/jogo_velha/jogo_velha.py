from os import system, name 
from typing import Tuple


def get_config() -> Tuple[str, int]:
    with open('conf.txt') as file:
        palavra = file.readline().strip()
        chances = int(file.readline())

        return palavra, chances

def jogar():   
    palavra, chances = get_config()    
    letras_usadas = []
    while True:
        tentativa_palavra = ""
 
        # for windows 
        if name == 'nt': 
            system('cls') 
        # for mac and linux(here, os.name is 'posix') 
        else:
            system('clear')       

        print("Número de chances: %d - tentativas:" % chances) # interpolação de string
        print(*letras_usadas) # imprime item por item do array
        print("\n")
        print(tentativa_palavra)
        for x in palavra:
            tentativa_palavra += x if x in letras_usadas else "_"
        print(tentativa_palavra + "\n\n")
 
        if tentativa_palavra == palavra:
            print(f"Você ganhou com apenas {chances}!")
            break
    
        chute = input("Digite uma letra:")
        letras_usadas.append(chute)
 
        if not chute in palavra:
            chances -= 1
 
        if chances == 0:
            print("Você perdeu!")
            break
        
 
 
if __name__ == "__main__":
    jogar()