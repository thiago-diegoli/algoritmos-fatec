from random import randint
dado = [1,2,3,4,5,6]
jogadas = []
for i in range(6000):
    jogadas.append(dado[randint(0,5)])
print('Frequência')
for i in range(1,7):
    print(f'Número {i}: {jogadas.count(i)/60:.1f}%')