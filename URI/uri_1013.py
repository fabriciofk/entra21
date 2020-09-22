A, B, C = map(lambda x: int(x), input().split(" "))
maior_ab = (A + B + abs(A - B)) / 2
maior = (maior_ab + C + abs(maior_ab - C)) / 2
print(f"{maior:.0f} eh o maior")