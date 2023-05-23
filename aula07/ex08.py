while True:
    n = int(input('Digite um número positivo maior que 1: '))
    if n > 1:
        break
primo = True
for i in range(2,n):
    if n % i == 0:
        primo = False
if primo:
    print(f'O número {n} é primo')
else:
    print(f'O número {n} não é primo')
