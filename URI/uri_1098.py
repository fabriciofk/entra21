i = 0
j = 1
while i <= 2:
    auxj = j + i
    for x in range(3):
        if i == 0 or i == 1 or i > 1.8:
            print(f'I={i:.0f} J={auxj:.0f}')
        else:
            print(f'I={i:.1f} J={auxj:.1f}')
        auxj += 1
    i += .2