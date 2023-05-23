matriz = [[int(input(f'Digite um elemento (coluna {i+1}, linha {n+1}): ')) for n in range(5)] for i in range(5)]
media = 0
contador = 0
for i in matriz:
    for n in i:
        if i.index(n) % 2 != 0:
            media += n
            contador += 1
media /= contador
print(f'A média dos elementos nas linhas pares equivale a {media:.1f}')
