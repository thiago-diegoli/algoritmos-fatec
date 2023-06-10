n = int(input('Digite um número inteiro positivo: '))
while n:
    digito = n % 10
    n = n // 10
    print(digito, end='')
