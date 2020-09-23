n1, n2, n3, n4 = map(lambda x: float(x), input().split(" "))
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + n4) / 10
print(f"Media: {media:.1f}")
if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
elif 5 <= media < 7:
    print("Aluno em exame.")
    nexame = float(input())
    print(f"Nota do exame: {nexame:.1f}")
    media = (media + nexame) / 2
    if media >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media:.1f}")