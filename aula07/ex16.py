# Exercício 8 utilizando while
while True:
    n = int(input('Digite um número positivo maior que 1: '))
    if n > 1:
        break
primo = True
i = 2
while i != n-1:
    if n % i == 0:
        primo = False
    i += 1
if primo:
    print(f'O número {n} é primo')
else:
    print(f'O número {n} não é primo')
