dias = int(input())
anos, dias = divmod(dias, 365)
meses, dias = divmod(dias, 30)
print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")