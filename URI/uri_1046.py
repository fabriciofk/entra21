hi, hf = map(lambda x: int(x), input().split(" "))

if hf <= hi:
    hd = hf - hi + 24
else:
    hd = hf - hi

print(f"O JOGO DUROU {hd} HORA(S)")