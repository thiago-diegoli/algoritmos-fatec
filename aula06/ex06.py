nota = int(input('Digite quantas questões acertou na prova: '))
if nota < 50:
    conceito = 'D'
elif nota < 70:
    conceito = 'C'
elif nota < 81:
    conceito = 'B'
else:
    conceito = 'A'
print(f'Sua nota final será {conceito}')