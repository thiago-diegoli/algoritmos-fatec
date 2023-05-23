n = int(input('Digite um número inteiro: '))
e = 0
for i in range(1,n+1):
    e += 2**i
print(e)