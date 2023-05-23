from math import ceil
h = 2.8
l = float(input('Digite a largura (em metros): '))
c = float(input('Digite o comprimento (em metros): '))
a = 2*(c * h + l * h) - 2.10 * 0.8
tinta = int(input('Digite a quantidade de litros da lata de tinta: '))
print(f'Você precisará de {ceil(a/(tinta*3))} latas de tinta para pintar o aposento.')


