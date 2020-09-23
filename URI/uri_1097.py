i = 1
j = 7
while i <= 9:
    auxj = j
    for x in range(3):
        print(f'I={i} J={auxj}')
        auxj -= 1
    i += 2
    j += 2