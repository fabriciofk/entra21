n = int(input())
x = 1
for i in range(n):
    for j in range(x, x + 3):
        print(j, end=' ')
    x = j + 2
    print('PUM')