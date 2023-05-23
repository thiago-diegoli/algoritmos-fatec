# Exercício 6 utilizando while
n = int(input('Digite um número: '))
fatorial = 1
i = 0
while i != n:
    i += 1
    fatorial *= i
print(f'O fatorial de {n} é {fatorial}')
