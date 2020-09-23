hi, mi, hf, mf = map(int, input().split())

th = hf - hi

if th < 0:
    th += 24

tm = mf - mi

if tm < 0:
    tm += 60
    if th == 0:
        th += 23
    else:
        th -= 1

if hi == hf and mi == mf:
    th += 24

print(f'O JOGO DUROU {th} HORA(S) E {tm} MINUTO(S)')
