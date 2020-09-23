SENHA = '2002'

while True:
    tentativa = input()

    if tentativa == SENHA:
        print('Acesso Permitido')
        break
    else:
        print('Senha Invalida')