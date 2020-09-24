n = int(input())
horas, n = divmod(n, 3600)
minutos, n = divmod(n, 60)
print(f"{horas}:{minutos}:{n}")