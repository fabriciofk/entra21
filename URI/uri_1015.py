from math import sqrt
x1, y1 = map(lambda x: float(x), input().split(" "))
x2, y2 = map(lambda x: float(x), input().split(" "))
distancia = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
print(f"{distancia:.4f}")