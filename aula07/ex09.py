e = 0
b = int(input('Digite o valor de B: '))
n = int(input('Digite o valor de N: '))
for i in range(1,n+1):
    e += b**i
print(f'Valor de E: {e}')