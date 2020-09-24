a, b = map(float, input().split())

if a < b:
    a, b = b, a

if a % b == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
