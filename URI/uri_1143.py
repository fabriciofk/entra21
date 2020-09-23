n = int(input())
x = 1
for i in range(n):
    for j in range(1, 4):
        if j != 3:
            print(x ** j, end=' ')
        else:
            print(x ** j)
    x += 1