n = input('Digite um número inteiro positivo: ')
soma, mult = 0, 1
for i in n:
    soma += int(i)
    mult *= int(i)
print(f'Soma = {soma}')
print(f'Multiplicação = {mult}')