from configparser import ConfigParser
from typing import List, Tuple
import os


SIMBOLOS = '!"#$%&\'()*+,./:;<=>?@[]^_`{|}~'


def get_config() -> Tuple[str, int]:
    """Obtém as configurações do jogo através do arquivo config.cfg.

    Returns:
        Caso o arquivo de configuração exista, retorna uma tupla que
        corresponde a palavra e as chances do jogador, senão retorna
        os valores DEFAULT.
    """
    try:
        # Abrindo o arquivo de configuração em modo de leitura.
        with open('config.cfg', encoding='utf8') as config_file:
            # Instanciando um ConfigParser.
            config = ConfigParser()
            # Definindo o arquivo que vai ser lido.
            config.read_file(config_file)
            # Verificando se existe a seção USER_SPECIFIED no arquivo de
            # configuração.
            if config.has_section('USER_SPECIFIED'):
                # Obtendo os valores da seção USER_SPECIFIED.
                word = config.get('USER_SPECIFIED', 'word')
                chances = config.getint('USER_SPECIFIED', 'chances')
            else:
                # Obtendo os valores da seção DEFAULT.
                word = config.get('DEFAULT', 'word')
                chances = config.getint('DEFAULT', 'chances')

            return word, chances
    except FileNotFoundError:
        # Imprimindo as mensagens de erro.
        print('Não existe um arquivo de configuração.')
        print('Serão utilizados valores DEFAULT.')
        # Pausa para o usuário poder ler as mensagens.
        input('Digite qualquer tecla para continuar: ')
        # Criando o arquivo com dados DEFAULT.
        set_config()
        # Abrindo o arquivo de configuração em modo de leitura.
        with open('config.cfg') as config_file:
            # Instanciando o ConfigParser.
            config = ConfigParser()
            # Lendo o arquivo de configurações.
            config.read_file(config_file)
            # Obtendo os valores do arquivo.
            word = config.get('DEFAULT', 'word')
            chances = config.getint('DEFAULT', 'chances')

            return word, chances


def clear_screen() -> None:
    """Limpa o console.

    Verifica qual o sistema operacional e executa o comando necessário
    para limpar o console naquele sistema.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def is_valid_guess(guess: str, letters_used: List[str]) -> bool:
    """Valida o chute.

    Verifica se o chute é um digito, símbolo ou se ele já foi digitado.

    Args:
        guess: chute.
        letters_used: letras já utilizadas.

    Returns:
        False se for um dígito, já tiver sido utilizado ou for um símbolo,
        senão retorna True.
    """
    # Definindo as validações que seram feitas.
    validations = [
        {
            'validation_name': 'is_digit',
            'validation': guess.isdigit(),
            'error_message': 'o chute é um número'
        },
        {
            'validation_name': 'already_used',
            'validation': guess in letters_used,
            'error_message': 'letra já usada'
        },
        {
            'validation_name': 'is_symbol',
            'validation': guess in SIMBOLOS,
            'error_message': 'caractere inválido'
        },
        {
            'validation_name': 'invalid_lenght',
            'validation': len(guess) != 1,
            'error_message': 'só é permitido um caractere por chute'
        }
    ]
    # Fazendo todas as validações e imprimindo a mensagem de erro.
    for validation in validations:
        if validation['validation']:
            print(f'Erro ({validation["validation_name"]}): '
                  f'{validation["error_message"]}.')
            return False

    return True


def game_over_check(valid_guesses: str, word: str, chances: int) -> bool:
    """Verifica se o jogo acabou.

    O jogo acaba quando o usuário acertar a palavra, ou as chances chegarem
    a zero.

    Args:
        valid_guesses: palavra formada pelo usuário.
        word: palavra-chave do jogo.
        chances: quantidade de chances restantes.

    Returns:
        True caso o jogo tenha acabado, False caso contrário.
    """
    if valid_guesses == word:
        clear_screen()
        print(f'A palavra era: {word}.')
        print(f'Você ganhou com {chances} chance(s) sobrando!')
        input('Pressione RETURN para voltar ao menu principal.')
        return True

    if chances == 0:
        clear_screen()
        print(f'A palavra era: {word}.')
        print('Suas chances acabaram. Você perdeu :(')
        input('Pressione RETURN para voltar ao menu principal.')
        return True


def play() -> None:
    """Função responsável por controlar o jogo."""
    word, chances = get_config()
    letters_used = []
    while True:
        clear_screen()
        valid_guesses = ''

        # Printando o jogo.
        print(f'Chances disponíveis: {chances}.')
        print(*letters_used, end='\n\n')
        print(valid_guesses)
        for letter in word:
            valid_guesses += letter if letter in letters_used else '_'
        print(valid_guesses, end='\n\n')

        # Verificando se o jogo acabou.
        game_over = game_over_check(valid_guesses, word, chances)

        if game_over:
            break

        # Obtendo o valor do chute.
        while True:
            guess = input('Digite uma letra: ').lower()

            clear_screen()

            # Verificando se o chute é válido.
            if is_valid_guess(guess, letters_used):
                break

        # Adicionando o chute na lista de chutes.
        letters_used.append(guess)

        # Diminuindo as chances caso o chute seja inválido.
        if guess not in word:
            chances -= 1


def main_menu() -> str:
    """Imprime o menu principal.

    Returns:
        A opção escolhida pelo usuário.
    """
    menu_options = {
        '1': 'Jogar',
        '2': 'Modificar as configurações',
        '3': 'Sair'
    }

    while True:
        print('*' * 30)
        print('Escolha uma opção:')
        for option, value in menu_options.items():
            print(f'{option} - {value}')

        print('*' * 30)
        choosed_option = input('Digite a opção desejada: ')

        if choosed_option in menu_options.keys():
            return choosed_option
        else:
            clear_screen()
            print('Opção inválida.')


def set_config(word: str = None, chances: str = None) -> None:
    """Modifica as configurações do jogo.

    Se os parâmetros forem passados, cria uma seção USER_SPECIFIED no
    arquivo com esses valores, caso contrário só cria os valores
    DEFAULT.

    Args:
        word: palavra do jogo.
        chances: quantidade de chances.
    """

    # Instanciando um ConfigParser.
    config = ConfigParser()
    # Definindo os valores DEFAULT do arquivo.
    config['DEFAULT'] = {
        'word': 'python',
        'chances': '3'
    }
    # Verificando se os parâmetros foram passados.
    if word and chances:
        # Criando a seção USER_SPECIFIED e adicionando os atributos.
        config['USER_SPECIFIED'] = {
            'word': word,
            'chances': chances
        }

    # Escrevendo os valores no arquivo.
    with open('config.cfg', 'w', encoding='utf8') as config_file:
        config.write(config_file)


def main() -> None:
    while True:
        # Recebe a opção do menu principal.
        menu_option = main_menu()
        clear_screen()
        # Controle de fluxo do programa.
        if menu_option == '1':
            play()
        elif menu_option == '2':
            print('Modificando as configurações.')
            word = input('Digite a palavra desejada: ').lower()
            changes = input('Digite a quantidade de chances desejada: ')
            set_config(word, changes)
        else:
            print('Obrigado por jogar!')
            break


if __name__ == '__main__':
    main()
