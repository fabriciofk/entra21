from datetime import datetime
dia_inicio = input()
momento_inicio = input()
dia_fim = input()
momento_fim = input()

tempo_inicio = datetime.strptime(
    f'{dia_inicio} {momento_inicio}',
    'Dia %d %H : %M : %S'
)

tempo_fim = datetime.strptime(
    f'{dia_fim} {momento_fim}',
    'Dia %d %H : %M : %S'
)

duracao = tempo_fim - tempo_inicio
duracao_dias = duracao.days
duracao_horas, resto = divmod(duracao.seconds, 3600)
duracao_minutos, duracao_segundos = divmod(resto, 60)

print(f'{duracao_dias} dia(s)')
print(f'{duracao_horas} hora(s)')
print(f'{duracao_minutos} minuto(s)')
print(f'{duracao_segundos} segundo(s)')