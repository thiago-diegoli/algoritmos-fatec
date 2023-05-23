horario = float(input('Digite um horario: '))
horas = int(horario)
minutos = (horario - horas) * 100 + horas * 60
print(f'O horário em minutos: {minutos:.0f}')