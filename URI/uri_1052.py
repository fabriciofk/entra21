from datetime import datetime
mes = input()

mes = datetime.strptime(mes, '%m')
mes_escrito = mes.strftime('%B')

print(mes_escrito)
