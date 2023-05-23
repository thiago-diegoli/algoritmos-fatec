n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
soma = n1 + n2
print(f'A soma dos números equivale a {soma}')
if soma > 1000:
    print('A soma é maior que 1000')
elif soma < 1000:
    print('A soma é menor que 1000')