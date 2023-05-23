pares = []
while True:
    n = int(input('Digite um número: '))
    if n == 0:
        break
    if n % 2 == 0:
        pares.append(n)
print(f'A media dos números pares fornecidos equivale a {sum(pares)/len(pares):.1f}')