while True:
    soma = 0
    m = int(input('Digite o valor de M: '))
    n = int(input('Digite o valor de N: '))
    if m < 0 or n < 0:
        print('Os números devem ser positivos')
    elif n >= m:
        print('M deve ser maior que N')
    else:
        for i in range(n, m+1):
            soma += i
        print(f'A soma de todos números entre (e incluindo) {n} e {m} equivale a {soma}')

