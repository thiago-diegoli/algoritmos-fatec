from random import randint
dado = [1,2,3,4,5,6]
jogadas = []
for i in range(30000):
    jogadas.append(dado[randint(0,5)]+dado[randint(0,5)])
print('Frequência')
for i in range(2,13):
    print(f'Soma = {i}: {jogadas.count(i)/300:.1f}%')
if jogadas.count(7) > 5000:
    print('A soma de 7 aparece mais de 1/6 das jogadas')
else:
    print('A soma de 7 não aparece mais de 1/6 das jogadas')
