password = ''

while True:   
    try:
        account_number = int(input('Enter the account number: '))
        break
    except:
        print('Invalid character!')

    
while True:   
    try:
        password = int(input('Enter the password: '))
        password = str(password)
        list_password = list(password)
        lenght = len(list_password)
        if lenght != 6:
            print('Invalid password lenght!')
        else:
            break
    except:
        print('Use just numbers!')
      
    