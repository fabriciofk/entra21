n = int(input())

for i in range(n - 1, 1, -1):
    n *= i

print(n)